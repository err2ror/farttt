#!/bin/bash
#To install,
for i in "modpy.py" "mf"
do sudo mv $i "/usr/local/lib/python3.11/dist-packages/"
done
zenity --info --text="Installation done!" --title="Modpy install"
