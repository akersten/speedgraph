#!/bin/bash

# Check that utilities we need are present.
echo -n "Checking utilities..."
command -v wget >/dev/null || { echo "wget is required but not present. Please install the wget utility."; exit 1; }
command -v chmod >/dev/null || { echo "chmod- is required but not present. Please install the chmod utility."; exit 1; }
echo " OK"

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

# Tell our python script that things should be alright and we can skip some sanity checks that are
# already covered here.
export RAN_VIA_INIT=YES

# Rock and roll.
python speedgraphing.py
