# ytplconverter  
Simple youtube playlist converter made for a friend  
Made by Stephmoon with help from the pytube and moviepy  

This was made for people who do not have reliable yt converter or do not have yt premium. This program was made to handle albums, since multiple videos may be converted into audio files into one Folder. Though keep in mind that the quality of the videos will be based on the quality they are on YouTube. Since this program is made to be accessible to anyone, there is a section on this readme which acts a tutorial.  

## Requirements:  
> This List all the required packages that will need to be imported. All packages here may have to be installed if they have not already previously been installed. Through the pip command, you may install each one of these packages (pip command may change whether you are on mac or windows).  
```  
pip install [package name] 
*for macOS
```  
```  
py -m pip install [package name] 
python -m pip install [package name]
*either for windows
```  
* tqdm  
* pytube  
* moviepy  
* eyed3  

## Setup:  
### (SECTION FOR THOSE WHO'VE NEVER RUNNED PYTHON FILES)  
> If you have never runned Python Files on any Compiler before, then a couple of things may need to be downloaded before hand. You will need to download Python3 and some Compiler or IDE. Below is a provided tutorial on installing Python and Sublime to run the code. While there are many ways to run the code, my recommendation is to use Sublime with Terminus.  

* Download Python3: You can download Python from either the Microsoft Store or the Python Website. You must download the latest version of Python3. And keep track of where you downloaded Python to, since that may be important for troubleshooting. Navigate to the downloads, and download the latest version for your system.  
> https://www.python.org/  

* Download SublimeText3: You can download the Latest Version of SublimeText from their Website. Download the Latest Version for your System. There are many other text editors out there but I prefer Sublime. Other text editors include VScode and Notepad++.
> https://www.sublimetext.com/  

* (Extra Step) Hello World: To Check that Sublime and Python are both working, please create small file with the following code below. Save this file as 'helloworld.py' and then run the file from Sublime. Sublime can run the file with the following shortcuts: **command+B** (macOS) or **control+B** (windows). It may ask you how you would like to build the system, select Python. The Code will work if your terminal prints 'hello world'.  
``` py  
print('hello world')
```  

* Install Terminus: Terminus is a Package on Sublime which allows you to run your command line through your text editor. To install Terminus you will need to install the Package Control. Using the shortcut **command+shift+P** (macOS) or **control+shift+P** (windows). This will open the Command Palette, after this type **Install Package Control** and press *enter*. After that the Package Control will be installed. Open the Command Palette again and type **Package Control: Install Package** (you may need to wait a couple seconds). Once you see options load, tpye **Terminus** and select it. This will install Terminus onto Sublime. Reset your Sublime once this finishes.
> Once Terminus is Installed, you will need to configure it for your System. On Sublime, go to **Preferences > Package Settings > Terminus** (on macOS this can be found by selecting Sublime Text from the top bar). You will need to select Command Palette and Key Bindings. Both of these wil open different files which allow you to configure the terminal, please paste the following code into the each of the respective files:  

This is for the Command Palette  
```  
[
   {
        "caption": "Terminal (panel)",
        "command": "terminus_open",
        "args"   : {
           "cmd": "bash",
           "cwd": "${file_path:${folder}}",
           "title": "Command Prompt",
           "panel_name": "Terminus"
        }
   },
] 
```  
This is for the Key Bindings  
```  
[
   {
       "keys": ["alt+1"],
       "command": "terminus_open",
       "args" : {
           "cmd": "bash",
           "cwd": "${file_path:${folder}}",
           "panel_name": "Terminus"
       }
   }
] 
```  
*You may need to replace bash with cmd.exe if you are on windows. You can test whether Terminus works by pressing alt+1 (windows) or options+1 (macOS), the terminal at the bottom of sublime should open up. If you do not know what your terminal looks like when you open it up, please open it from your desktop (either called terminal or command prompt)*  

* Install the Packages and Run Code: Once Terminus has been set up, you can now install the required packages and run the program. To install the packages you will need pip, to download pip you will need to download the following file and then use the following commands in the directory of the file (recommend putting the file into some folder, then opening that folder on sublime. Once you open the file on sublime you can open up Terminus and use the commands without any issue).  
> https://bootstrap.pypa.io/get-pip.py  

Once the file has been downloaded; open the terminal on sublime and install pip with the following commands:  
```  
python -m ensurepip --upgrade
python get-pip.py
*for macOS
```  
```  
py -m ensurepip --upgrade
py get-pip.py
*for windows
```  
*On macOS, you may need to replace python with python3 in the command*  
Once pip has been installed you may start installing the packages. To install packages use the following commands (based on your system), and replace *package name* with the name of any of the packages from **Requirements** (at the top of the page).  
```  
pip install [package name]
*for macOS
```  
```  
py -m pip install [package name] 
python -m pip install [package name]
*either for windows
```  
Once that has been completed, your sublime should be ready to run the program. To install packages use the following commands (based on your system), the terminal will ask you to enter the playlist from youtube (please enter the url, either the playlist or a video from the playlist will work). It will begin to download the video, and once it finishes it will ask you for another playlist. You can continue this until you are finished, to which you can exit by entering anything besides the url (this will bring up an error).  
```  
python ytplconverter.py
*for macOS
```  
```  
py ytplconverter.py
*for windows
```  

*Thank you for using the program. If you have any questions, either contact me on discord or raise an issue in the github. Unsure whether I will be updating this since it was a small project*  
