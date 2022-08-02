#!/bin/bash

# when apt upgrade installed new linux headers system failed to boot due to vbox service startup fail
# or because header installation failed half-way due to low disk space (insufficient VBox drive size)
# following script aims to automate the fix

# expected to launch from recovery shell (should have root) 

SEP='=%.0s' {1..80}

function header () {
    echo "$SEP"
    echo "$1"
    echo "$SEP"
}

# fail if not root
# needs root - installing packages and extensions/additions
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi



# cleanup to free up some disk space
header "Cleaning up space"
apt autoremove -y
apt purge -y

# get fresh packages
header "Refreshing packages"
apt update

# find current kernel header version
headers="linux-headers-$(uname -r)"

# reinstall headers for the current kernel
header "Reinstalling $headers"
apt install --reinstall "$headers" -y

# rebuild VBox 
header "Rebuilding VBox"
/sbin/rcvboxadd quicksetup all

# reinstall VBox tools
# https://linuxconfig.org/install-virtualbox-guest-additions-on-linux-guest
header "Reinstalling VBox additions"
apt install build-essential dkms -y 

# assumes the Additions image was inserted; mount it
mkdir -p /mnt/cdrom
mount /dev/cdrom /mnt/cdrom
/mnt/cdrom/VBoxLinuxAdditions.run


header "DONE"
