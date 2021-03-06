<h1 align="center">
  <br>
  <a href="https://github.com/Meeharaj/BombIT"><img src="https://th.bing.com/th/id/R.47b3de4a7ed7017a1d7a638a9b3d9c34?rik=xPCUJVDuetrAuw&riu=http%3a%2f%2fis4.mzstatic.com%2fimage%2fthumb%2fPurple%2fv4%2f65%2f9d%2fb6%2f659db685-ad0d-4d41-47b9-31c633efd6fe%2fsource%2f600x600bb.jpg&ehk=08V9cb8GKek3EnXbrvMj7nguC%2ffJw%2fDX12ICAfTCbvQ%3d&risl=&pid=ImgRaw/BombIT.png" alt="BombIT"></a>
  <br>
  BombIT v2.1b
  <br>
</h1>


<p align="center">A free and open-source SMS/Call bombing application</p>

## NOTE:


> **Due to the overuse of script, a bunch of APIs have been taken offline. It is okay if you do not receive all the messages.**


- The application requires active internet connection to contact the APIs
- You would not be charged for any SMS/calls dispatched as a consequence of this script
- For best performance, use single thread with considerable delay time
- Always ensure that you are using the latest version of BombIT and have Python 3
- This application must not be used to cause harm/discomfort/trouble to others
- By using this, you agree that you cannot hold the contributors responsible for any misuse

## Compatibility
Check your Python version by typing in
```shell script
$ python --version
```
If you get the following
```shell script
Python 3.8.3
```
or any version greater than or equal to 3.4, this script has been tested and confirmed to be supported. For obsolete versions of Python (eg 2.7), use discretion while executing the script as it has not been tested there.

## Features

- Over 15 integrated messaging and calling APIs included with JSON
- Unlimited (with abuse protection) and super-fast bombing with multithreading
- Possibility of international API support (APIs are offline)
- Flexible with addition of newer APIs with the help of JSON documents
- Actively supported by the developers with frequent updates and bug-fixes
- Intuitive auto-update feature and notification fetch feature included
- Recently made free and open-source for community contributions
- Modular codebase and snippets can be easily embedded in other program


## Usage:

### Install by PIP (Recommended)

Before continuing make sure following requirements are satisfied:

- Python version greater than or equal to 3.4 is installed
- pip is installed for Python 3

Install `BombIT` package by running:

```shell script
pip3 install BombIT
```

Run BombIT by just typing:
```shell script
tbomb
```

### Install from GIT

#### NOTE 

Git installation methods are not universal and are likely to differ between distributions so installing Git as per the given instructions below may not work. Please check out how to install Git for your Linux distribution [here](https://git-scm.com/). Commands below provide instructions for Debian-based systems.

>Running `BombIT.sh` as sudo miscofigures files ownership. It is recommended not to run it as sudo

Run these commands to clone and run BombIT.

#### For Termux

To use the bomber type the following commands in Termux:
```shell script
pkg install git -y 
pkg install python -y 
git clone https://github.com/Meeharaj/BombIT.git
cd BombIT
./BombIT.sh
```

#### For iSH

To use the application, type in the following commands in iSH.
```shell script
apk add git
apk add python3
apk add py3-pip
apk add ruby
gem install toilet
git clone https://github.com/Meeharaj/BombIT.git
cd BombIT
pip3 install -r requirements.txt
chmod +x BombIT.sh
./BombIT.sh
```

#### For Debian-based GNU/Linux distributions

To use the application, type in the following commands in GNU/Linux terminal.
```shell script
sudo apt install git
git clone https://github.com/Meeharaj/BombIT.git
cd BombIT
bash BombIT.sh
```

#### For MacOS

To use the application, type in the following commands in MacOS terminal:

##### Install Brew

```shell script
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
````

##### Install dependencies:

```shell script
brew install git
brew install python3
sudo easy_install pip
sudo pip install --upgrade pip
git clone https://github.com/Meeharaj/BombIT.git
cd BombIT
bash BombIT.sh
```


##### Missing Tools on MacOS

The package `toilet` cannot be installed yet on macOS. But TBomb does still work.

### Demonstrative Video:

- Watch Indian Bombing Method [here](https://youtu.be/9KWkwsr_QGw)  
- Watch International Bombing Method [here](https://youtu.be/JqsHkyIcnPM).  


  

### TODO:

- [x] Make Code More Readable and Extensible
- [x] Add Mail Spam Module
- [x] Add Mail Spam APIs
- [x] Add Update Feature using git
- [x] Add Update Feature without git (download zip and extract)
- [x] Split code into multiple files (after Deprecation)

##contact us
- https://www.instagram.com/meeharaj_j
## FAQ

- Poor internet connection:

```Check your internet connection and try pinging any remote address to confirm.```

- Do you support "X" Country?

```Most Countries are supported for SMS and only India for calls. The SMS delivery rate might be different for different countries.```

- Can you add support for "X" Country?

```We do what we can, but we cannot promise. Please stay tuned for future support. If you are ready to help then maybe we can do faster.```

- Why is the limit so low?

```Due the amount of requests, the APIs can die. To prevent a bigger outtake of BombIT, it has been limited.``` 

- Help, i got the error that the requirements aren't installed, even when the installer has successfully reached the main menu

The Easy Method:

```pip3 install BombIT```

Then execute by simply running

``BombIT``

The Git Method:  
Clone the repo and Switch to the BombIT Directory and execute this command:  
```pip3 install -r requirements.txt```

- Help, i can't execute BombIT.sh!

Run BombIT Directly with
```python3 bomber.py```

- VPN? Proxy's? 

```No, BombIT can fail due the high response time or API restrictions.```

- Protection ?

```Use OTP Blockers and activate DND.```

- Call Bombing does not work!

``` It does only work for indian numbers. Other Country's are not supported yet.```


Last Update: 15.05.2021

