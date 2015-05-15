import os, subprocess, time, re
import matplotlib.pyplot as plt

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


print('[', time.strftime('%H:%M:%S'), '] Starting tests...')

valuesOverTime = [] # This will be an array of tuples for plotting: (minutesSinceMidnight, [ping, download, upload])
currentDay = time.localtime().tm_yday # If this changes, clear the valuesOverTime array (new, blank graph for each day)
 
# Continously spawn speedtest processes and save/graph the output.
while True:
    # Figure out the name of today's file.
    todaysFilename = time.strftime('%Y.%m.%d')
    
    # Update the symbolic links of the `today` files
    os.symlink(todaysFilename + '.png', 'output/tmp.png')
    os.symlink(todaysFilename + '.txt', 'output/tmp.txt')
    os.rename('output/tmp.png', 'output/today.png')
    os.rename('output/tmp.txt', 'output/today.txt')

    # Start the speedtest process.
    res = subprocess.Popen(['./speedtest-cli', '--simple'], stdout=subprocess.PIPE)

    # The output looks like this:
    ## Ping: xx.x ms
    ## Download: xx.x MBit/s
    ## Upload: xx.x MBit/s
    # So we'll just use regex on the middle thing (space separated) to extract the value.
    values = []
    for line in res.stdout.readlines():
        try:
            # Extract the middle part of each line as our numeric value.
            values.append(re.search('.* ([^ ]*) .*', line.decode('utf-8')).group(1))
        except IndexError:
            # If that group didn't exist, the output didn't look like what we expected.
            print('[', time.strftime('%H:%M:%S'), '] Problem parsing output:', line)
            continue

    # Update values in the valuesOverTime array. Clear it if it's a new day.
    if currentDay != time.localtime().tm_yday:
        currentDay = time.localtime().tm_yday;
        valuesOverTime = []

    mpm = time.localtime().tm_hour * 60 + time.localtime().tm_min
    valuesOverTime.append( (mpm, values) )

    valuesOverTime

    # Format output and append it to a text file.
    outputLine = ''
    if len(values) == 3:
        outputLine = '[ ' + time.strftime('%H:%M:%S') + ' ] Ping: ' + values[0] + ' Down: ' + values[1] + ' Up: ' + values[2]
    else:
        outputLine = '[ ' + time.strftime('%H:%M:%S') + ' ] Parse error'

    print(outputLine)
    with open('output/' + todaysFilename + '.txt', 'a') as f:
        f.write(outputLine + '\n')

    # Generate the graph and save it over the old one for today.
    
    

    time.sleep(60 * interval)
