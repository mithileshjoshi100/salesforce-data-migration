## Python Installetion steps 🐍
Download Python installer: Visit the official Python website (https://www.python.org/downloads/) an
1. Download Python installer: Visit the official Python website (https://www.python.org/downloads/) and download the latest stable version of Python for your operating system. Choose either Python 3.x or Python 2.x (Note: Python 2 is no longer actively maintained, so it is recommended to use Python 3).

2. Run the installer: Once the download is complete, run the Python installer. Follow the instructions provided by the installer to install Python on your system.

3. Add Python to PATH (Windows only): During the installation, you might see an option to "Add Python x.x to PATH." Make sure to check this option, as it allows you to use Python from the command prompt or terminal without specifying the full path.

4. Verify the installation: After the installation is complete, open a new command prompt (Windows) or terminal (macOS/Linux) and type:
    ```
    python --version
    ```

    It should display the Python version you installed. Additionally, you can type python and press Enter to enter the Python interactive shell.



## One-time setup ✅
1. Install Python 🐍
2. Open the project folder 📂
3. Open the terminal/powershell in the project folder and run the command:

    ```
    pip install -r requirements.txt
    ```
4. Done with setup!! 🎉

## How to use 🚀
1. Verify credentials in the file: config\credentials\ ✅<br>
```\config\credentials\```
2. Add user emails in the python file: app\data_extraction\user_emails.py  ✉️<br>```app\data_extraction\user_emails.py```
3. Open the terminal/powershell in the project folder and run the command:
    ```
    python main_gui.py
    ```
4. Check logs here (clear old logs before fresh execution): 📜<br>
    ``logs\basic.log``
5. Trace data files: <br>
    Extracted files: ``data\extraction_data`` 📂<br>
    Inserted files with new ids: ``data\insertion_data`` 📂

Feel free to connect if you have any questions! 🤗



