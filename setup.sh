#!/usr/bin/env bash
# _*_ utf-8 _*_
# @uthor : Aman Raj
# Filename : local (setup.sh)
# File Modified : 09/01/2023



# Python, Python-pip

function internet_check () {
  wget -q --tries=10 --timeout=20 --spider https://google.com
  if [ $? -eq 0 ]; then
    printf '\033[0;37m[\033[0;32mok\033[0;37m] Internet Connection\n'
  else
    printf '\033[0;37m[\033[0;31mFailed\033[0;37m] Internet Connection\n'
    exit 0

  fi
}

function os () {
  DISTRO=$(cat /etc/*-release | tr [:upper:] [:lower:] | grep -Poi '(debian|ubuntu)' | uniq)

if [ -z $DISTRO ]; then
    DISTRO='unknown'
    printf "\033[0;37m[\033[0;31mFailed\033[0;37m] OS Detected\n"
else
  printf "\033[0;37m[\033[0;32m$DISTRO\033[0;37m] OS Detected\n"
fi

}

function python3_pkg () {
  pkg="python3"
  status="$(dpkg-query -W --showformat='${db:Status-Status}' "$pkg" 2>&1)"

  if [ ! $? = 0 ] || [ ! "$status" = installed ]; then
    printf "\033[0;37m[\033[0;31mFailed\033[0;37m] $pkg Package\n"
    xterm -T "Installing" -geometry 100x30 -e "sudo apt install -y $pkg"
  else
    printf "\033[0;37m[\033[0;32mok\033[0;37m] $pkg Package\n"
  fi
}

function python3_pip_pkg () {
  pkg="python3-pip"
  status="$(dpkg-query -W --showformat='${db:Status-Status}' "$pkg" 2>&1)"

  if [ ! $? = 0 ] || [ ! "$status" = installed ]; then
    printf "\033[0;37m[\033[0;31mFailed\033[0;37m] $pkg Package\n"
    xterm -T "Installing" -geometry 100x30 -e "sudo apt install -y $pkg"
  else
    printf "\033[0;37m[\033[0;32mok\033[0;37m] $pkg Package\n"
  fi
}

function gcc_pkg () {
  pkg="gcc"
  status="$(dpkg-query -W --showformat='${db:Status-Status}' "$pkg" 2>&1)"

  if [ ! $? = 0 ] || [ ! "$status" = installed ]; then
    printf "\033[0;37m[\033[0;31mFailed\033[0;37m] $pkg Package\n"
    xterm -T "Installing" -geometry 100x30 -e "sudo apt install -y $pkg"
  else
    printf "\033[0;37m[\033[0;32mok\033[0;37m] $pkg Package\n"
  fi
}

function banner() {
    printf "\033[0;32m\t\t\t"
    figlet Predictor Panel
    printf "\t\t\033[1;34m[Version : 0.1]\033[0m\n"
}

function figlet_pkg () {
  pkg="figlet"
  status="$(dpkg-query -W --showformat='${db:Status-Status}' "$pkg" 2>&1)"

  if [ ! $? = 0 ] || [ ! "$status" = installed ]; then
    printf "\033[0;37m[\033[0;31mFailed\033[0;37m] $pkg Package\n"
    xterm -T "Installing" -geometry 100x30 -e "sudo apt install -y $pkg"
  else
    printf "\033[0;37m[\033[0;32mok\033[0;37m] $pkg Package\n"
  fi
}

function Xterm () {
  pkg="xterm"
  status="$(dpkg-query -W --showformat='${db:Status-Status}' "$pkg" 2>&1)"

  if [ ! $? = 0 ] || [ ! "$status" = installed ]; then
    printf "\033[0;37m[\033[0;31mFailed\033[0;37m] $pkg Package\n"
    sudo apt install -y $pkg
  else
    printf "\033[0;37m[\033[0;32mok\033[0;37m] $pkg Package\n"
  fi
}

if [ "$(whoami)" == "root" ]; then
  printf '\e[0;32mChecking Your System && \e[0;32m'
  echo "$(tput setaf 2)"Checking Necessary Repos..... "$(tput sgr0)"
  printf "\n"
  Xterm
  sleep 0.1
  figlet_pkg
  sleep 0.1
  sudo apt-get install gnome-terminal -y
  printf '\n'
  sleep 0.1
  clear
  banner
  printf '\n\n\n'
  os
  internet_check
  python3_pkg
  python3_pip_pkg
  gcc_pkg
  chmod +x requirements.txt
  xterm -T "Installing" -geometry 100x30 -e "sudo python3 -m pip install -r requirements.txt"
  printf "\033[0;37m[\033[0;31mInstalled Module From\033[0;37m] requirements.txt\n"

else
  printf '\e[0;32mChecking Your System \e[0;32m'
  printf '\n'
  echo "$(tput setaf 1)"Sorry Installing only on root"$(tput sgr0)"
  kill "$!"
fi