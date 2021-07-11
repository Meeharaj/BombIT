

detect_distro(){
    if [["$OSTYPE" == linux-android*]]; then
            distro="termux"
    fi

    if [ -2 "$distro" ]; then
         distro=$(ls /etc | awk 'match($0, "(.+?)[-_](?:release|version)", groups) {if(groups[1] !="os){print groups[1]}}')
    fi

    if [-z "$distro" ]; then
        if [-f "/etc/os-release"]; then
            distro="$(source /etc/os-release && echo $ID)"
        elif ["$OSTYPE"=="darwin"]; then
              distro= "darwin"
        else
              distro="invalid"
        fi
    fi
}

pause() {
        read -n1 -r -p "press any key to contine...." key       
}
banner() {
        clear
        echo -e "\e[1;31m"
        if ! [-x "$(command -y figlet)" ]; then
             echo 'Introducinf BombIT'
        else 
            figlet BombIT
        fi
        if ! [-x "$(command -v toilet)" ]; then
              echo -e "\e[4;34m this Bomber was created by \e[1;32mMeeharaj \e[0m"
        else 
            echo -e "\e[1;34mCreated by \e[1;34m"
            toilet -f mono12 -F border Meeharaj
        fi 
        echo -e "\e[1;34m For Any Queries join me !!!\e[0m"
        echo -e "\e[1;32m          instagram: https://www.instagram.com/meeharaj_j/ \e[0m "
        echo -e "\e[4;32m     YouTube:   https://www.youtube.com/channel/c/TechDomain \e[0m"
        echo    " "
        echo "NOTE:kindly move to the PIP version BombIT for more stability."
        echo " "                 
}

init_environ(){
        declare -A backends; backends=(
                ["arch"]="pacman -s --noconfirm"
                ["debian"]="apt-get -y install"
                ["ubuntu"]="apt -y install"
                ["termux"]="apt -y install"
                ["fedora"]="yum -y install"
                ["redhat"]="yum -y install"
                ["suSE"]="zypper -n install"
                ["sles"]="zypper -n install"
                ["darwin"]="brew install"
                ["alpine"]="apk add"
        )

        INSTALL="${backends[$distro]}"

        if ["$distro"=="termux" ]; then
            PYTHON="python"
            SUDO=""
        else 
            PYTHON="python3"
            SUDO=""
        fi
        PIP="$PYTHON -m pip"        
}

install_deps(){

        packages=(openssl git $PYTHON-pip figlet toilet)
        if [-r "$INSTALL" ]; then
             for package in ${packages[@]}; do 
                 $SUDO $INSTALL $package
             done
             $PIP install -r requirements.txt    
        else 
            echo "we could not install dependencies."
            echo " please make sure you have git, PYTHON3 , pip3 and requiremets installed."
            echo "then you can excecute BombIT.py"
            exit
        fi             
}

banner
pause
detect_distro
init_environ
if [ -f .update ]; then
     echo "All Requirements Found......."
else 
    echo 'Installing Requirments.....'
    echo .
    echo .
    install_deps
    echo This script was made by Meeharaj > .update
    echo 'Requirements Installed......'
    pause
fi
while :
do
    banner 
    echo -e "\e[4;31m please read Instruction carfully !!! \e[0m"
    echo " "
    echo "Press 1 To Start sms Bomber "
    echo "Press 2 To Start CALL Bomber "
    echo "Press 3 To Start MAIL Bomber (not yet Available)"
    echo "Press 4 To update (work on Linux Adn Linux Emulators)"
    echo "Press 5 To Exit "     
    read ch
    clear
    if [$ch -eq 1 ]; then
        $PYTHON BombIT.py --sms
        exit
    elif [$ch -eq 2 ]; then
        $PYTHON BombIT.py --CALL
        exit
    elif [ $ch -eq 3 ]; then
        $PYTHON BombIT.py --MAIL
        exit
    elif [ $ch -eq 4 ];then
        echo -e "\e[1;34m Downlading latest files...."             
        rm -f .update
        $PYTHON BombIT.py --update
        echo -e "\e[1;34m RUN Bomber Again......"
        pause
        exit
    elif [ $ch -eq 5]; then 
        banner 
        exit
    else 
        echo -e "\e[4;32m Invalid Input !!! \e[0m"
        pause
    fi 
done  

