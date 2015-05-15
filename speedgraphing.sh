#!/bin/bash

# Check that utilities we need are present.
echo -n "Checking utilities..."
command -v wget >/dev/null || { echo "wget is required but not present. Please install the wget utility."; exit 1; }
command -v chmod >/dev/null || { echo "chmod is required but not present. Please install the chmod utility."; exit 1; }
command -v grep >/dev/null || { echo "grep is required but not present. Please install the grep utility."; exit 1; }
echo " OK"

# Check Python version
echo -n "Checking Python version... "
command -v python3 >/dev/null || { echo " Python3 is required but not present. Please install Python3."; exit 1; }

if python3 --version | grep -q "Python 2."; then
	echo "Python3 is required but only Python2 was found. Please install Python3."
	exit 1
fi

# Check for speedtest-cli and grab it if it's not present.
echo -n "Checking for speedtest-cli..."
if [ -e "speedtest-cli" ];
then
    echo " OK"
else
    echo " not found, downloading..."
    if    wget -O speedtest-cli https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest_cli.py --no-verbose; 
    then
        echo "OK"
        chmod +x speedtest-cli
    else
        echo "Problem downloading speedtest-cli -- download it manually?"
        exit 1
    fi
fi

# Check that the output directory exists and create it if it doesn't
echo -n "Checking for output directory..."
if [ -e "output/" ];
then
    echo " OK"
else
    if mkdir output;
    then
        echo " created."
    else
        echo " problem creating output directory! Please: chmod u+w ."
        exit 1
    fi
fi

# Tell our python script that things should be alright and we can skip some sanity checks that are
# already covered here.
export RAN_VIA_INIT=YES

# Rock and roll.
python3 speedgraphing.py
