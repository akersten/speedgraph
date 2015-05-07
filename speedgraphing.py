import os

if os.environ.get('RAN_VIA_INIT') != "YES":
    print('Please run speedgraphing.py via the wrapper script, speedgraphing.sh.')
    exit(1)

print('Alright.')
