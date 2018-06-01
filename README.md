# Raspberry Pi Garden Controller
A Python web server application for controlling up to 6 GPIOs from your browser. For your garden, the GPIOs would be wired to a relay or a solenoid valve that could control the water.
## Installation
1. Format your SD card and install the latest version of [Raspbian](https://www.raspberrypi.org/downloads/raspbian/).
2. Connect your pi to the same WiFi you will also be controlling it from and I also recommend changing your keyboard layout to US. (Preferences -> Mouse and Keyboard Settings). Also, you will probably need more space on your SD card for installing updates and packages so open the console and run `sudo raspi-config` and then navigate to Advanced Options -> Expand Filesystem then reboot.
3. After the reboot, open the console again and run the following three commands to make sure your pi is up to date and to install Flask:
    ```
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install python-flask
    ```
4. Now run the following command to clone the files into your home directory:
    ```
    git clone https://github.com/CarsonChild/pi-gpio-controller
    ```
5. Now enter the directory and run the app:
    ```
    cd pi-gpio-controller
    cd webapp
    sudo python garden.py
    ```
6. Now in a browser on another device (Such as a smartphone or laptop), navigate to [RaspberryPiIPAddress]:5000/garden 
   - This should look something like 192.168.1.29:5000/garden 
   - If you don't know your pi's IP address, type `hostname -I` in the terminal.
7. You should see 6 buttons, an input bar and another button. If a button is blue, then that pin will turn on for that interval when "Water" is pressed otherwise it will stay off.

## Wiring 
In the webapp, Button 1 corrosponds with GPIO17, Button 2 to GPIO18, Button 3 to GPIO27, Button 4 to GPIO22, Button 5 to GPIO23, and Button 6 to GPIO24. The GPIOs should be hooked up to the switch on your relay or solenoid valve. A map of the GPIOs on Raspberry Pis 2 and 3 is seen below.
![Map of GPIO pins](https://i.stack.imgur.com/Ct2JG.png)
