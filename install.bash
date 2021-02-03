clear
sleep 1
apt-get update -y          # Update
apt-get autoremove         # Auto Remove
clear
echo "Installing Python2"
sleep .5
clear
pkg install python2
clear
echo "Installed Python2."
sleep .5
clear
pkg install pip # Installing Pip
echo "Pip installed" # Telling User that installing is done
sleep .5
clear

echo "Installing pysocks"
sleep .5
clear
pip install pysocks        # Installing pysocks
clear
sleep .5
echo "Installed pysocks"   # Teling User that installing is done
sleep .5
clear

chmod +x spammer.py     # Giving permission to spammer.py
sleep .5
clear
echo "Installation completed. You can run script with 'python2 spammer.py' command. Don't forget to give Star from Github."