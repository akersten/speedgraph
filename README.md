# speedgraph
A toolkit for graphing network speed over time

## Overview

Graphing the network speed over time is a useful metric for diagnosing network congestion issues. This toolkit generates network-speed-over-time graphs at a specified interval.

## Technologies

This project is an amalgamation of existing utilities and tools - the glue is shell script and python.

## Setup

```
chmod +x speedgraphing.sh
./speedgraphing.sh
```

### Dependencies

* Python3
* `python-matplotlib` package ([or from source:](http://matplotlib.org/downloads.html))
* [speedtest-cli](https://github.com/sivel/speedtest-cli) (automatically downloaded if not present)
* `grep`, `chmod`, `wget`

### Usage

* When running the script, the user is prompted for a test interval (default 3 minutes)
* Raw data and generated png graphs are presented in `./output`
* The format of the data is text files and pngs (`yyyy.mm.dd.txt` and `.png`) containing that day's speeds
* The text output is also emitted on stdout
* Files named `today.txt` and `today.png` will be dynamically symlinked to the current day's file

## Contributors

[Alex Kersten](http://kersten.email)

