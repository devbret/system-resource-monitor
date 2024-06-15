# System Resource Monitor

![Live reporting on nine different system performance metrics.](https://hosting.photobucket.com/images/i/bernhoftbret/screenshot-of-system-monitor.png)

Monitor the live performance of your computer in the browser, using Python and JavaScript.

## Set Up

### Programs Needed

-   [Git](https://git-scm.com/downloads)
-   [Python](https://www.python.org/downloads/) (When installing on Windows, make sure you check the ["Add python 3.xx to PATH"](https://hosting.photobucket.com/images/i/bernhoftbret/python.png) box.)

### Steps

1. Install the above programs.
2. Open a shell window (For Windows open PowerShell, for MacOS open Terminal & for Linux open your distro's terminal emulator).
3. Clone this repository using `git` by running the following command; `git clone https://github.com/devbret/system-resource-monitor`.
4. Navigate to the repo's directory by running; `cd system-resource-monitor`.
5. Install the needed dependencies for running the script by using the following command: `pip install -r requirements.txt`.
6. Run the script with the command `python3 app.py`. Open the link that the Flask server generates for you, this will bring you to the system resource monitoring app.
7. You can now see nine different measurements being updated every second in their respective graph(s).
