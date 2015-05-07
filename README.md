# speedgraph
A toolkit for graphing network speed over time

## Overview

Graphing the network speed over time is a useful metric for diagnosing network congestion issues. This toolkit automates the setup and execution of freely-available utilities to ease the process of generating network-speed-over-time graphs.

## Technologies

This project is an amalgamation of existing utilities and tools - the glue is shell script and python.

## Setup

```
chmod +x speedgraphing.sh
./speedgraphing.sh
```
The `speedgraphing` script will check that all dependencies are in-place, and will try to download 3rd party requirements if they are not present.


### Dependencies

* Python
* [speedtest-cli](https://github.com/sivel/speedtest-cli) (automatically downloaded if not present)

## Contributors

[Alex Kersten](http://kersten.email)

