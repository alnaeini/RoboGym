# RoboGym

A Virtual Training Gym for Autonomous Vehicle using Deep Reinforcement Learning 

You can find presentation sildes [here](https://docs.google.com/presentation/d/1V8KX64MdBqVPu6P0uukhF9grdG7qMSG2hCiIBCJgtTI/edit#slide=id.g649c3cfac8_2_127). 


# Requirement

The RoboGym package works on Linux, Mac and Windows.

I recommend using a following instruction for training. 

In the terminal, First create and activate conda virtual environment as: 

    ```
    conda create -n RoboGym python=3.6
    
    conda activate RoboGym
    ```
Secondly, in directory /Packages use following command:

    ```
    pip install -e .
    
    ```
Third, in directory /Robogym_training/animalai_train , use the following command:

    ```
    pip install -e .
 
    ```

Finally download the environment for your system:

| OS | Environment link |
| --- | --- |
| Linux |  [download v1.0.0](https://drive.google.com/drive/u/0/folders/1D9zrjEp6Z2azDcy4FcOQmr0L-l8e4dhS) |
| MacOS |  [download v1.0.0](https://drive.google.com/drive/u/0/folders/1gcBqT9-5m0STPPncCkz1gDbeQdZ693Wm) |
| Windows | [download v1.0.0](https://drive.google.com/drive/u/0/folders/18KtalJT_bPaTXmUyBAqIl4w8wTzYf8hm)  |


You can now unzip the content of the archive to the `env` folder and you're ready to go! Make sure the executable 
`RoboGym.*` is in `env/`. On linux you may have to make the file executable by running `chmod +x env/RoboGym.x86_64`. 


# Training on Amazon Web Service

This section is a summary of practical sections from [here](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md) 

This page contains instructions for setting up an EC2 instance on Amazon Web Service for training ML-Agents environments.



#### Install and setup Xorg:

    ```sh
    # Install Xorg
    $ sudo apt-get update
    $ sudo apt-get install -y xserver-xorg mesa-utils
    $ sudo nvidia-xconfig -a --use-display-device=None --virtual=1280x1024

    # Get the BusID information
    $ nvidia-xconfig --query-gpu-info

    # Add the BusID information to your /etc/X11/xorg.conf file
    $ sudo sed -i 's/    BoardName      "Tesla K80"/    BoardName      "Tesla K80"\n    BusID          "0:30:0"/g' /etc/X11/xorg.conf

    # Remove the Section "Files" from the /etc/X11/xorg.conf file
    # And remove two lines that contain Section "Files" and EndSection
    $ sudo vim /etc/X11/xorg.conf
    ```

#### Update and setup Nvidia driver:

    ```sh
    # Download and install the latest Nvidia driver for ubuntu
    # Please refer to http://download.nvidia.com/XFree86/Linux-#x86_64/latest.txt
    $ wget http://download.nvidia.com/XFree86/Linux-x86_64/390.87/NVIDIA-Linux-x86_64-390.87.run
    $ sudo /bin/bash ./NVIDIA-Linux-x86_64-390.67.run --accept-license --no-questions --ui=none

    # Disable Nouveau as it will clash with the Nvidia driver
    $ sudo echo 'blacklist nouveau'  | sudo tee -a /etc/modprobe.d/blacklist.conf
    $ sudo echo 'options nouveau modeset=0'  | sudo tee -a /etc/modprobe.d/blacklist.conf
    $ sudo echo options nouveau modeset=0 | sudo tee -a /etc/modprobe.d/nouveau-kms.conf
    $ sudo update-initramfs -u
    ```

#### Restart the EC2 instance:

    ```sh
    sudo reboot now
    ```

#### Make sure there are no Xorg processes running:

   ```sh
   # Kill any possible running Xorg processes
   # Note that you might have to run this command multiple times depending on
   # how Xorg is configured.
   $ sudo killall Xorg

   # Check if there is any Xorg process left
   # You will have a list of processes running on the GPU, Xorg should not be in
   # the list, as shown below.
   $ nvidia-smi

   # Thu Jun 14 20:21:11 2018
   # +-----------------------------------------------------------------------------+
   # | NVIDIA-SMI 390.67                 Driver Version: 390.67                    |
   # |-------------------------------+----------------------+----------------------+
   # | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
   # | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
   # |===============================+======================+======================|
   # |   0  Tesla K80           On   | 00000000:00:1E.0 Off |                    0 |
   # | N/A   37C    P8    31W / 149W |      0MiB / 11441MiB |      0%      Default |
   # +-------------------------------+----------------------+----------------------+
   #
   # +-----------------------------------------------------------------------------+
   # | Processes:                                                       GPU Memory |
   # |  GPU       PID   Type   Process name                             Usage      |
   # |=============================================================================|
   # |  No running processes found                                                 |
   # +-----------------------------------------------------------------------------+

   ```

#### Start X Server and make the ubuntu use X Server for display:

    ```console
    # Start the X Server, press Enter to come back to the command line
    $ sudo /usr/bin/X :0 &

    # Check if Xorg process is running
    # You will have a list of processes running on the GPU, Xorg should be in the list.
    $ nvidia-smi

    # Make the ubuntu use X Server for display
    $ export DISPLAY=:0
    ```

#### Ensure the Xorg is correctly configured:

    ```sh
    # For more information on glxgears, see ftp://www.x.org/pub/X11R6.8.1/doc/glxgears.1.html.
    $ glxgears
    # If Xorg is configured correctly, you should see the following message

    # Running synchronized to the vertical refresh.  The framerate should be
    # approximately the same as the monitor refresh rate.
    # 137296 frames in 5.0 seconds = 27459.053 FPS
    # 141674 frames in 5.0 seconds = 28334.779 FPS
    # 141490 frames in 5.0 seconds = 28297.875 FPS
    ```   

## Training on EC2 instance

1. In the Unity Editor, load a project containing an ML-Agents environment (you
   can use one of the example environments if you have not created your own).
2. Open the Build Settings window (menu: File > Build Settings).
3. Select Linux as the Target Platform, and x86_64 as the target architecture
(the default x86 currently does not work).
4. Check Headless Mode if you have not setup the X Server. (If you do not use
Headless Mode, you have to setup the X Server to enable training.)
5. Click Build to build the Unity environment executable.
6. Upload the executable to your EC2 instance within `ml-agents` folder.
7. Change the permissions of the executable.

    ```sh
    chmod +x <your_env>.x86_64
    ```
8. (Without Headless Mode) Start X Server and use it for display:

    ```sh
    # Start the X Server, press Enter to come back to the command line
    $ sudo /usr/bin/X :0 &

    # Check if Xorg process is running
    # You will have a list of processes running on the GPU, Xorg should be in the list.
    $ nvidia-smi

    # Make the ubuntu use X Server for display
    $ export DISPLAY=:0

9. Run Python file 
    
    ```sh
    $ cd /RoboGym_training
    $ python RoboGym.py
    ```
   
