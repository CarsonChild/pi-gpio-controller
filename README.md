# Raspberry Pi Garden Controller
A Python web server application for controlling up to 6 GPIOs from your browser. For your garden, the GPIOs would be wired to a relay or a solenoid valve that could control the water.
## Installation
1. Format your SD card and install the latest version of [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)
2. Open the console and run the following two commands:
    ```
    sudo apt-get update
    sudo apt-get upgrade
    ```
3. Now run the following command to clone the files:
    ```
    cd ~
    git clone https://github.com/CarsonChild/pi-gpio-controller/tree/master/webapp
    ```
4. Now enter the directory and run the app:
    ```
    cd webapp
    sudo python garden.py
    ```
5. Now in a browser on another device (Such as a smartphone or laptop), navigate to [RaspberryPiIPAddress]:5000/garden 
   - This should look something like 192.168.1.29:5000/garden 
   - If you don't know your pi's IP address, type `hostname -I` in the terminal.
6. You should see 6 buttons, an input bar and another button. If a button is blue, then that pin will turn on for that interval otherwise it will stay off.
