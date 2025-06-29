#To install,
unzip "modpy.zip"
for i in "modpy.py" "mf"
do mv $i "/$HOME/.local/share/python3.8/site-packages"
done
zenity --info --text="Installation done!" --title="Modpy install"
