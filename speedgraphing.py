import os, subprocess, time, re

# Check that we ran the init script.
if os.environ.get('RAN_VIA_INIT') != "YES":
    print('Please run speedgraphing.py via the wrapper script, speedgraphing.sh.')
    exit(1)

print('''
        *----------------*
        | Speedgraphing! |
        *----------------*
        ''')

# Parse the user input for the polling interval.
interval_input = ''
interval = 3

query = True
while query:
    interval_input = input('Test interval in minutes [3]: ')
    if interval_input == '':
        query = False
    else:
        try:
            interval_parsed = int(interval_input)
            if interval_parsed <= 0:
                query = True
            else:
                query = False
                interval = interval_parsed
        except ValueError:
            query = True


# Continously spawn speedtest processes and save/graph the output.
while True:
    print('[', time.strftime('%H:%M:%S'), '] Running speedtest...')
    res = subprocess.Popen(['./speedtest-cli', '--simple'], stdout=subprocess.PIPE)

    # The output looks like this:
    ## Ping: xx.x ms
    ## Download: xx.x MBit/s
    ## Upload: xx.x MBit/s
    # So we'll just use regex on the middle thing (space separated) to extract the value.
    values = []
    for line in res.stdout.readlines():
        values.append(re.search('.* ([^ ]*) .*', line.decode('utf-8')).group(1))

    print('Ping:', values[0], 'Down:', values[1], 'Up:', values[2])

    print('[', time.strftime('%H:%M:%S'), '] Waiting', interval, 'minutes...')
    time.sleep(60 * interval)
