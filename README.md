# System Resource Monitor

![Live reporting on nine different system performance metrics.](https://hosting.photobucket.com/bbcfb0d4-be20-44a0-94dc-65bff8947cf2/14d36487-6993-4f3e-aaeb-ac43b520fc7a.png)

A real-time system resource monitoring dashboard built with Flask, psutil, D3.js and JavaScript which continuously tracks and visualizes key machine performance metrics with a cyberpunk-styled interface.

## Overview

The Flask backend exposes an `/api/resource` endpoint for gathering live system data using the psutil library, then returns the data as JSON. On the frontend, D3.js renders multiple animated line charts which update every second, maintaining a rolling window of recent values to display trends over time. Together, the backend and frontend create a visually engaging, continuously updating performance dashboard for monitoring system health in real time.

## Set Up

Below are instructions for setting this app on your computer.

### Programs Needed

- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/)

### Steps

1. Install the above programs
2. Open a terminal
3. Clone this repository using `git` by running the following command: `git clone git@github.com:devbret/system-resource-monitor.git`
4. Navigate to the repo's directory by running: `cd system-resource-monitor`
5. Install the needed dependencies for running the script by using the following command: `pip install -r requirements.txt`
6. Run the script with the command `python3 app.py`
7. Open the link that the Flask server generates for you, this will bring you to the system resource monitoring app
8. You can now see nine different measurements being updated every second in their respective graph(s)
