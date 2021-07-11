


import os
import shutil
import sys
import subprocess
import string
import random
import json
import re
import time
import argparse
import zipfile
from io import BytesIO

from concurrent.futures import ThreadPoolExecutor, as_completed

from utils.decorators import MessageDecorator
from utils.provider import APIProvider

try:
    import requests
    from colorama import Fore,style
except ImportError:
    print("\tSome dependencies could not be imported (possibly not installed)")
    print(
           "Type 'pip3 install -r requirements.txt' to"
           "install all required packages")
    sys.exit(1)


def readisdc():
    with open("isdcodes.json") as file:
        isdcodes = json.load(file)
    return isdcodes


def get_version():
    try:
        return open(".version","r").read().strip()
    except Exception:
        return '1.0'


def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def bann_text():
    clr()
    logo = """  
     ██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
     ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
     ██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
     ██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
     ██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
     ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝     
                                                    """


    if ASCII_MODE:
        logo = ""
    version = "version: "+__VERSION__ 
    contributors = "contributors:  "+" ".join(__CONTRIBUTORS__)
    print(random.choice(ALL_COLORS) + logo + RESET_ALL)
    mesgdcrt.successMessage(version)
    mesgdcrt.sectionMessage(contributors)
    print()


def cheak_intr():
    try:
        requests.get("https://motherfuckingwebsite.com")
    except Exception:
        bann_text()
        mesgdcrt.FailureMessage("poor internate connection detected") 
        sys.exit(2)


def format_phone(num):
    num= [n for n in num if n in string.digits]
    return ''.join(num).strip()


def do_zip_update():
    success = False
    if DEBUG_MODE:
        zip_url = "https://github.com/Meeharaj/BombIT/archive/dev.zip"
        dir_name = "TBomb-dev"
    else:
        zip_url = "https://github.com/Meeharaj/BombIT/archive/master.zip"
        dir_name = "BombIT-master"
    print(ALL_COLORS[0]+"downloading ZIP....."+ RESET_ALL)
    response = requests.get(zip_url)
    if response.status_code == 200:
        ZIP_CONTENT = RESPONSE.CONTENT
        try:
            with zipfile.ZipFile(BytesIO(zip_content)) as zip_file:
                for member in zip_file.namelist():
                    filename = os.path.split(member)
                    if not filename[1]:
                       continue
                    new_filename = os.path.join(
                        filename[0].replace(dir_name,"."),
                        filename[1])
                    source = zip_file.open(member)
                    target = open(new_filename,"wb")
                    with source, target:
                         shutil.copyfileobj(source,target)
            SUCCESS = True
        except Exception:
            mesgdcrt.FailureMessage("Error occured while extracting !!")
    if success:
        mesgdcrt.SuccessMessage("bomber updated to the latest version ")
        mesgdcrt.genralMessage(
            "please run the script again to load the letest version" )
    else:
        mesgdcrt.FailureMessage("unable to update bomber.")
        mesgdcrt.WarningMessage(
            "grab the letest one ")

    sys.exit()


def do_git_update():
    success = False
    try:
        print(ALL_COLOR[0]+"updating "+RESET_ALL,end='')
        process = suprocess.popen("git cheakout.&&git pull ",
                                   shell = True,
                                   stdout = subprocess.PIPE,
                                   stderr = subprocess.STDOUT)
        while proccess:    
                print (ALL_COLORS[0]+'.'+RESET_ALL,end='')
                time.sleep(1)
                returncode = process.poll()
                if returncode is not None:
                    break
        success = proccess.returncode 
    except Execption:
        success = False
    print("\n")

    if success :
        mesgdcrt.successMessage("bomber was updated to the latest version ")
        mesgdcrt.GenrelMessage(
             "please run the script again to load the latest version " )
    else :
        mesgdcrt.FailureMessage("unable to update Bomber,")
        mesgdcrt.WarningMessage("make sure to install 'git' ")
        mesgdcrt.GenraleMessage("the eun command :")
        print(
            "git cheakout . && "
            "git pull https://github.com/Meeharaj/BombIT.git HEAD" )
        sys.exit() 


def update():
    if shutil.which('git'):
        do_git_update()
    else :
        do_zip_update()


def cheak_for_updates():
    if DEBUG_MODE:
        mesgdcrt.WarningMessage(
            "DEBUG MODE Enabled! Auto update cheak is disabled." )
        return 
    mesgdcrt.SectionMessage("cheeaking for updates")
    fver = request.get(
        "https://raw,githubusercontent.com/Meeharaj/BombIT/master/.version"
    ).text.strip()
    if fver != ___VERSION__:
        mesgdcrt.WarningMessage("An update is available")
        mesgdcrt.GenralMessage("Starting update......")
        update()
    else:
        mesgdcrt.SuccessMessage("BombIT  is up-to-date")
        mesgdcrt.generalMessage("Starting Bomber")


def notifying():
    try:

        if DEBUG_MODE:
            url = "https://github.com/Meeharaj/BombIT/raw/dev/.notify"
        else:
            url = "https://github.com/Meeharaj/BombIT/raw/master/.notify"
        noti = requests.get(url).upper()
        if len(noti)>10:
            mesgdcrt.SectionMessage("NOTIFICATION:+noti")
            print()
    except Exception:
        pass

def get_phone_info():
    while True:
        target = ""
        cc = input(mesgdcrt.CommandMessage(
            "Enter your country code (without+):" ))
        cc = format_phone(cc)
        if not country_codes.get(cc,False):
            mesgdcrt.Message(
                "The country code ({cc}) that you have entered"
                "is invalid of unsupported".format(cc=cc))
            continue
        target = input(mesgdcrt.CommandMessage(
            "Enter the target number :+" + cc+ " "))
        target = format_phone(target)
        if ((len(target)<= 6)or (len(target)>=12)):
            mesgdcrt.WarningMessage(
                "The phone number ({target})".format(target=target) + 
                "that you have entered is invalid")
            continue
        return(cc,target)


def get_mail_info():
    mail_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    while True:
        target = input(mesgdcrt.CommandMessage("Enter target maail: "))
        if not re.search(mail_regex,target,re.IGNORECASE):
            mesgdcrt.WarningMessage(
                "the mail ({target})".format(target=target) +
                "that you have entered is invalid" )
            continue
        return target


def pretty_print(cc,target,success,failed):
    requested = success+failed
    mesgdcrt.SectionMessage("Bombing is in progress - please be patient")
    mesgdcrt.GenrelMessage(
        "please stay connected to the internet during Bombing" )
    mesgdcrt.GenralMessage("target        : " + cc +" " + target)
    mesgdcrt.GenralMessage("sent          : " + str(requested))
    mesgdcrt.GenralMessage("successful    : " + str(success))                              
    mesgdcrt.GenralMessage("Failed        : " + str(failed))
    mesgdcrt.WenralMessage(
        "this tool was made for fun and research purposes only")
    mesgdcrt.SuccsessMessage("BombiT is created by meeharaj")


def Workernode(mode,cc,target,count,delay,max_threads):

    api = APIprovider(cc,target,mode,delay=delay)
    clr()
    mesgdcrt.SectionMessage("Gearing up the Bomber - Please be patient")
    mesgdcrt.GenralMessage(
        "Please stay connected to the internet during bombing")
    mesgdcrt.GenralMessage("API Version        : " + api.api_version)            
    mesgdcrt.GenralMessage("Target             : " + cc + target)
    mesgdcrt.GenralMessage("Amount             : " + str(count))
    mesgdcrt.GenralMessage("Threads            : " + str(max_threads) + "thrads")
    mesgdcrt.GenralMessage("Delay              : " + str(delay)+
                            "seconds")
    mesgdcrt.WarningMessage(
        "this tool made for fun and rechearch purpose only")
    print()
    input(mesgdcrt.CommandMessage(
        "press [CTRL+Z] to suspend the bomber or [ENTER] to resume it"))

    if len(APIProvider.api_provider )== 0:
        mesgdcrt.FailureMessage("Your country/target is not supported yet")
        mesgdcrt.GenralMessage("Feel free to reach out to us")
        input(mesgdcrt.CommandMessage("press [ENTER] to exit")) 
        bann_text()
        sys.exit()

    success, failed = 0,0
    while success < count:
        with ThreadPoolExecutor(max_workers=max_threads) as excutor:
            jobs = []
            for i in range(count-success):
                jobs.append(executor.submit(api.hit))                                  

            for job in as_completed(jobs):
                result = job.result()
                if result is None:
                    mesgdcrt.FailureMessage(
                        "Bombing li,it for your target has been reached ")
                    mesgdcrt.GenerelMessage("try Again Later !!") 
                    input(mesgdcrt.CommandMessage("press [ENTER] to exit"))
                    bann_text()
                    sys.exit()
                if result:
                    success += 1
                else:
                    failed +=  1
                clr()
                pretty_print(cc,target,success,failed)
    print("\n")
    mesgdcrt.SuccessMessage("Bombing Completed!")
    time.sleep(1.5)
    bann_text()
    sys.exit()


def selectnode(mode="sms"):
    mode = mode.lower().strip()
    try:
        clr()
        bann_text()
        cheak_intr()
        cheak_for_updates()
        notifyen()

        max_limit = {"sms": 500,"call": 15,"mail":200}
        cc, tsrget = "",""
        if mode in ["sms","call"]:
            cc,target = get_phone_info()
            if cc != "91":
                max_limit.update({"sms": 100})
        elif mode == "mail":
            target = get_mail_info()
        else:
            raise KeyboardInterrupt

        limit = max_limit[mode]
        while True :
            try:
                message = ("Enter number of {type}".format(type=mode.upper())+
                            " to send (max {limit}): ".format(limit=limit))
                count = int(input(mesgdcrt.CommandMessage(message)).strip())      
                if count > limit or count == 0:
                    mesgdcrt.WarningMessage("you have requested " + str(count)
                                                + " {type}".format(
                                                    type=mode.upper()))
                    mesgdcrt.GeneralMessage(
                        "Automatically  capping the value"
                        "to {limit}".format(limit=limit))
                    count = limit
                delay = float(input(
                    mesgdcrt.CommandMessage("Enter delay time(in seconds): "))
                    .strip())
                #delay= 0 
                max_thread_limit = (count//10) if (count//10) > 0 else 1
                max_threads = int(input(
                    mesgdcrt.CommandMessage(
                        "Enter number of Thread (recommended : {max_limit}): "
                        .format(max_limit=max_thread_limit)))
                    .strip())
                max_thread = max_threads if (
                    max_threads > 0 ) else max_thread_limit
                if (count < 0 or delay < 0 ):
                    raise Exception 
                break
            except KeyboardInterrupt as ki:
                raise ki
            except Exception :
                mesgdcrt.FailureMessage("Read Instructions carefully !!!!")
                print()

        Workernode(mode, cc, target, count,delay, max_threads)
    except KeyboardInterrupt:
        mesgdcrt.WarningMessage("Received INTR call - Exiting....")
        sys.exit()


mesgdcrt = MessageDecorator("icon")   
if sys.version_info[0] !=3:
    mesgdcrt.FailureMessage("BombIT will work only in python v3")
    sys.exit()

try:
    country_codes = readisdc()["isdcodes"]
except FileNotFoundError:
    update()


__VERSION__ = get_version()
__CONSTRIBUTORS__ = ["meeharaj jay (WHITE Force)"]

ALL_COLORS = [fore.GREEN, fore.RED, fore.YELLOW, fore,BLUE, 
              fore.MAGENTA, fore.CYAN, fore.WHITE]
RESET_ALL = Style.RESET_ALL

ASCII_MODE = False
DEBUG_MODE = False

description = """BombIT = your Friendly Spammer Application

BombIT can be used for many purpose whice includes - 
\t Exposing the vulnerable APIs over Internet
\t Friendly spamming
\t Testing your spam detector and more .......

BombIT is not intented for malicious uses.
"""
 
parser = argparse.ArgumentParser(description=description,
                                   epilog='coded by WHITE Force !!!!')
parser.add_argument("-sms", "--sms", action="store_true",
                     help="start BombIT with sms Bomb mode ")
parser.add_argument("-call","--call", action="store_true",
                      help="Start BombIT with call Bomb mode")
parser.add_argument("-mail", "--mail", action="store_true",
                      help="start BombIT with mail Bomb mode")
parser.add_argument("-ascii", "--ascii", action="store_teur",
                     help="show only characters of standerd ASCII set")
parser.add_argument("-u", "--update", action="store_true",
                      help="update BombIT ")
parser.add_argument("-c", "--constributors", action="store_true",
                     help="show current BombIT constributors")
parser.add_argument("-v", "--version", action="store_ture",
                     help="show current BombIT version")


if __name__ == "__main__":
    args = parser.parse_args()
    if args.ascii:
        ASCII_MODE = True
        mesgdcrt = MessageDecorator("start")
    if args.version:
        print("version :",__VERSION__)
    elif args.constributors:
        print("constributors:"," ",join(__CONSTRIBUTORS__))
    elif args.update:
        update()
    elif args.mail:
        selectnode(mode="mail")
    elif args.call:
        selectnode(mode="call")
    elif args.sms:
        selectnode(mode="sms")
    else:
        choice = ""
        avail_choice = {
            "1": "SMS",
            "2": "CALL",
            "3": "MAIL"
        }
        try:
            while (choice not in avail_choice):
                clr()
                bann_text()
                print("Available option:\n")
                for key, value in avail_choice.items():
                    print("[{key} ] {value} BOMB ".format(key=key,
                                                           value=value))
                print()
                choice = input(mesgdcrt.CommandMessage("Enter choice : "))
            selectnode(mode=avail_choice[choice].lower())
        except KeyboardInterrupt:
            mesgdcrt.WarningMessage("Received INTR call - Exiting......")
            sys.exit()
    sys.exit()            



















            

