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

build_prompt() {
    # red if root, green if other
    if [[ ${EUID} == 0 ]] ; then
            clr='31'
    else
            clr='32'
    fi

    time='\[\e[0;${clr}m\]\A\[\e[m\] '                    # red timestamp
    chroot='${debian_chroot:+($debian_chroot)}'           # show if we're in chroot
    #user='\[\e[${clr}m\]\u@\[\e[m\]'                      # current user / green
    hostname='\[\e[1;${clr}m\]\h\[\e[m\]:'                # hostname
    cwd='\[\e[01;34m\]\w\[\e[m\]'                         # current work dir
    if command -v git &> /dev/null
    then
        git='\[\e[1;33m\]$(__git_ps1)\[\e[m\] '               # git branch
    else
        git=''
    fi
    prompt='\[\e[1;${clr}m\]\$\[\e[m\] '                  # actual prompt
    
    out=$time$chroot$user$hostname$cwd$git$prompt
    
    export PS1=$out
}
#color shell
force_color_prompt=yes
color_prompt=yes

if [ "$color_prompt" = yes ]; then
    build_prompt
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi

PATH=/usr/sbin:/sbin:/usr/etc:$PATH
export PS1 PATH


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
#export http_proxy=http://proxy:8080
#export https_proxy=https://proxy:8080
