# Setting Up the Jetson

>**Created:** 10/26/2019
>
>**Updated:** 04/05/2023
>
>**Author:** Jack Kolb
>
>**Updated By:** Joshua Shabun

**Relevancies:** Linux, Jetson TX2 Developer Kit

Once the Jetson is flashed and working, there are a few things you should do to set it up for general use. This is for Ubuntu 18.04, although it should work for future versions.

## In the initial setup:
* Make the username “ucr”
* Make the computer name “seadragon”
* Make the password “seadragon”

## After the initial setup:
1. Remove requiring password on reset, so that it can be booted up without needing a mouse/keyboard/monitor:
    * Settings → User Accounts → ucr → Automatic Login = ON
2. Remove locking the screen due to inactivity:
    * Settings → Brightness and Lock → Turn screen off when inactive for = Never
    * Settings → Brightness and Lock → Lock = OFF
    * Settings → Brightness and Lock → Require password when waking = OFF
3. Enable shut down when the POWER button is pressed:
    * Follow the Knowledge Base document “Power Off on Power Button Press”
4. Pin the Terminal app to the Launcher (side bar):
    * Open terminal, right click it on the side bar, click Lock to Launcher
5. Connect ethernet to a laptop, enable connecting from laptop
    * Right click the wifi icon → Edit Connections → Wired connection 1 → (gear) → IPv4 Settings → Method = Shared to other computers, save
    * Reconnect the ethernet cable, the laptop will show “Ethernet Connected” when clicking the WiFi icon
6. See the Jetson’s IP address by running `arp -a` on your laptop. The IP address with `seadragon` is the Jetson’s IP address.
    ```console
    jack@apollo:~$ arp -a
    seadragon (10.42.0.1) at 00:04:4b:8c:e4:65 [ether] on enx00e4c680274
    c-some-5-v524.wnet.ucr.edu (10.28.92.1) at 00:de:fb:19:12:42 [ether] on wlp4s0
    jack@apollo:~$
    ```
7. Test is out by SSHing into the Jetson
    * `ssh ucr@10.42.0.1`
    * If you receive an error about **SOMEONE MAY BE DOING SOMETHING NASTY**, it means your computer is already set up to another Jetson with that IP address, so the signature is different. Simply remove the signature by:
        
        `ssh-keygen -f "/home/[YOUR USER]/.ssh/known_hosts" -R "10.42.0.1"`

8. Clone the software git repository
    
    `git clone https://github.com/robosub-ucr/___________`
