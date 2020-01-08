# Setup

## Install Python 3 and Pip3
* sudo apt update
* sudo apt install python3 python3-pip

## Install virtualenv tools
* sudo pip3 install virtualenv virtualenvwrapper

## Configure virtualenvwrapper
* export WORKON_HOME=$HOME/.virtualenvs
* source /usr/local/bin/virtualenvwrapper.sh
* If you get any error refer to this webpage: https://virtualenvwrapper.readthedocs.io/en/latest/install.html#shell-startup-file

##  Virtualenv commands
* create a new virtualenv: mkvirtualenv env
* exit from virtualenv: deactivate

## Install the requirements
* pip3 install -r requirements.txt