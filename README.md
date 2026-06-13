# System Resource Monitor

![Live reporting on nine different system performance metrics.](https://hosting.photobucket.com/bbcfb0d4-be20-44a0-94dc-65bff8947cf2/14d36487-6993-4f3e-aaeb-ac43b520fc7a.png)

A real-time system resource monitoring dashboard built with Flask, psutil, D3.js and JavaScript which continuously tracks and visualizes key machine performance metrics with a cyberpunk-styled interface.

## Application Overview

The Flask backend provides an `/api/resource` endpoint which collects system resource data with the `psutil` library and returns it as JSON. On the frontend, JavaScript fetches the JSON data from the backend and uses D3.js to render line charts for each measurement. The charts update repeatedly in the browser and keep a rolling window of recent values, creating a live dashboard for viewing system resource activity over time.

## Basic Setup Instructions

Below are instructions for setting up this app on a Linux computer.

### Programs Needed

- [Git](https://git-scm.com/downloads)

- [Python](https://www.python.org/downloads/)

### Steps

1. Install the above programs

2. Open a terminal

3. Clone this repository: `git clone git@github.com:devbret/system-resource-monitor.git`

4. Navigate to the repo's directory: `cd system-resource-monitor`

5. Create a virtual environment: `python3 -m venv venv`

6. Activate the virtual environment: `source venv/bin/activate`

7. Install the needed dependencies: `pip install -r requirements.txt`

8. Run the Python script `python3 app.py`

9. Open the application in a browser: `http://localhost:5000`

10. When finished, stop the Flask server: `CTRL + C`

11. Exit the virtual environment: `deactivate`

## Other Considerations

This project repo is intended to demonstrate an ability to do the following:

- Monitor key system resources on a Linux computer and display them as a dashboard via their browser of choice

- Use `Flask`, Python, `psutil`, JavaScript and D3.js to visualize live system performance data

- Help users quickly view and track their computer’s resource usage through an automatically updating web interface

If you have any questions or would like to collaborate, please reach out either on GitHub or via [my website](https://bretbernhoft.com/).
