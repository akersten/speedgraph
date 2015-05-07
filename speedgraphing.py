import os

if os.environ.get('RAN_VIA_INIT') != "YES":
    print('Please run speedgraphing.py via the wrapper script, speedgraphing.sh.')
    exit(1)

print('''
        *----------------*
        | Speedgraphing! |
        *----------------*
        ''')

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

