# Basic Wateringhole things
## Overview

The Malicious File Downloader is a simple Flask web application that demonstrates how a malicious file can be disguised as a necessary plugin for viewing website content. The application prompts the user to download a file, simulating a plugin installation, and then redirects the user to a page with a working video.

## Installation
### Prerequisites

    Python 3.x installed on your system. You can download it from here.

### Installation Steps

    Clone or download this repository to your local machine.

    Navigate to the project directory in your terminal or command prompt.

    Create a virtual environment (optional but recommended):

    bash

python -m venv venv

### Activate the virtual environment:

    On Linux:

    bash

source venv/bin/activate

On Windows:

bash

    venv\Scripts\activate

Install the required dependencies:

bash

    pip install -r requirements.txt

## Usage
### Running the Application

    Ensure you are in the project directory with the virtual environment activated.

    Run the Flask application:

    bash

    python run.py

    Open a web browser and navigate to http://127.0.0.1:5000/.

### Testing

    Once the application is running, you will see the homepage with a prompt to download the plugin.

    Click on the "Click here to re-download the plugin" link to simulate downloading the plugin.

    After the download starts, a prompt will appear asking if you have run the downloaded file. Click "Yes" to proceed to the working video page, or click "No" to wait for the next prompt.

    If you clicked "No," another prompt will appear after 10 seconds. Repeat steps 3 and 4 until you click "Yes" or manually close the browser tab.

## Stopping the Application

To stop the Flask application, simply press Ctrl + C in the terminal or command prompt where the application is running.
Compatibility

    The application has been tested on both Linux and Windows environments.

## Credits

This application was created for educational purposes.
## License 

This project is licensed under the MIT License.