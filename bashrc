# If not running interactively, don't do anything
[ -z "$PS1" ] && return

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# enable programmable completion features (if not already enabled in /etc/bash.bashrc)
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi


# PS1 Prompt \A \u@\h:\w $ 
# Green for user
PS1='\[\e[0;32m\]\A\[\e[m\] \[\e[0;32m\]\u@\h\[\e[m\]:\[\e[1;34m\]\w\[\e[m\] \[\e[1;32m\]\$\[\e[m\] \[\e[0;37m\]'

# Red for /root/.bashrc
# PS1='${debian_chroot:+($debian_chroot)}\[\e[0;31m\]\A\[\e[m\] \[\033[01;31m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

PATH=/usr/sbin:/sbin:/usr/etc:$PATH
export PS1 PATH

#color shell
force_color_prompt=yes

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=100000
HISTFILESIZE=200000


# Aliases
alias ll="ls -l --color=auto"
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias ls='ls --color=auto'

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi


# set the proxy variables whenever you start the shell
export http_proxy=http://proxy:8080
export https_proxy=https://proxy:8080
