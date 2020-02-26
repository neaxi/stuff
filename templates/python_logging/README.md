

# What and Why
Purpose of this template is to have working example of logging in one place, incl. commonly used advanced applications and a quick GOTO/grab when you need to add logging to your project.

## Resources
### Oficial
[Python3 docs - Logging HOWTO](https://docs.python.org/3/howto/logging.html) - main documentation  
[Python3 docs - Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html) - practical examples  
[Python3 docs - logging.config — Logging configuration](https://docs.python.org/3/library/logging.config.html)

### Tutorial
[Real Python - Logging in Python](https://realpython.com/python-logging/) - entry level tutorial  
[Real Python - Python Logging: A Stroll Through the Source Code](https://realpython.com/python-logging-source-code/) - deep dive

____
# The code samples
## `basic_main.py`
 - minimal viable setup
 - three lines enabling utilization of logging in any of your library
```python
import logging
logging.basicConfig(format='[%(levelname)s] %(name)s: %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)
```

___
## `advanced_main.py`
* Contains following samples:  
    - logger configuration loaded from a dictionary
    - `-d/--debug` as the command line option
    - Loggers
    - Formatters
    - Handlers

### logger configuration loaded from a dictionary
Why? To keep the logging config outside of the actual script code in a dedicated file. 
```python
import logging.config 
from setup_logging import DEFAULT_LOGGING

logging.basicConfig()
logging.config.dictConfig(DEFAULT_LOGGING)
```
### `-d/--debug` as the command line option
Why? To have one simple CLI switch to printout additional info, which is otherwise hidden from the user. Option is processed by the argparse and logging level modified accordingly.
We're changing logging level only for `handler[0]` (`stdio_default` which is utilized for stdio). Import specific or FileHandlers are not modified!
```python
import setup_cli_args

parser = setup_cli_args.setup_parser()
args = parser.parse_args()

logging.getLogger().handlers[0].setLevel(args.log_level)
```
### Loggers
They're determining Level of log messages and to which handlers will be a LogRecord sent. Each logger can have one or more handlers. We can also do library/import specific loggers.  
  
Example  
We want DEBUG messages from the whole application but only WARNING from the `specific_module_import` library. The `propagate` attribute ensures a LogRecord wont be processed also by the default logger resulting in multiple outputs.
```python
'': {
    'level': logging.DEBUG,
    'handlers': ['stdio_default', 'file'],
},
'submodule_specific_import': {
    'level': 'INFO',
    'handlers': ['stdio_extensive'],
    # propagate attribute is True for a Logger instance by default
    'propagate': False
},
```

### Formatters
Determines in which format will be the LogRecords printed out. We can define multiple formatters and assign a different one to different logging Handlers.  
In order to prevent confusion caused by national customs, it's strongly recommended to adhere to ISO 8601 standard when processing time and date.  
Full list of the formatting attributes - [Py3 docs - Logging attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes)

```py
date_format = '%Y-%m-%dT%H:%M:%S%z'    # ISO 8601

'standard': {
    'format': '[%(asctime)s] [%(levelname)s] %(message)s',
    'datefmt': date_format
}
```
### Handlers
Where the magic happens. They're receiving LogRecords from loggers, filter per their own level, apply formatting given by associated formatter and send the record to appropriate output defined by their class.  
Available output classes:
 - StreamHandler - standard input/output; stdout, stderr
 - FileHandler - writting into logfiles (append / overwrite)
 - SMTPHandler - sending emails
 - HTTPHandler - sending logs to a server using GET/POST
  

**Beware of multiple FileHandlers writting into the same file.**  
 - [Logging IS NOT process safe](https://realpython.com/python-logging-source-code/#preliminary-2-logging-is-thread-safe-but-not-process-safe)  
 - Logging IS thread safe. The records in a logfile won't be sorted chronologically. One handler must wait for the other to release lock on the logfile, so the other can perform write operations. 
 - Additional FileHandlers attempting to access the same logfile must be set to 'append' mode otherwise they'll overwrite changes from previous Handler.

**Q:** Why do we have separate log level on loggers and on handlers?  
**A:** Lets say we have one logger. With following conditions:
 - Show the user INFO and above
 - Write a runtime logfile including DEBUG messages
 - Report CRITICAL and FATAL over HTTP/API (not covered in the repo code)  

The logger will be getting all the messages as it is set to DEBUG. Then each handler will filter the arriving records based on their own severity INFO/DEBUG/CRITICAL.
```py
'formatters': {
    'brief': {
        'format': '%(asctime)s %(levelname)s %(message)s'
    },
    'json': {
        'format': '{ "loggerName":"%(name)s", "timestamp":"%(asctime)s", "fileName":"%(filename)s", "message":"%(message)s"}',
    },
},
'loggers': {
    'default': {
        'handlers': ['console', 'logfile', 'http_reports'],
        'level': 'logging.DEBUG',
    }
}
'handlers': {
    'console': {
        'class': 'logging.StreamHandler',
        'level': 'INFO',
        'formatter': 'brief',
    },
    'logfile': {
        'class': 'logging.StreamHandler',
        'level': 'DEBUG',
        'formatter': 'brief',
        'filename': path_to_file,
        'mode': 'w',
    },
    'http_reports': {
        'class': 'logging.HTTPSHandler',
        'level': 'CRITICAL',
        'formatter': 'json',
        'url': 'https://URL/rest/error_reporting',
    },
},
```