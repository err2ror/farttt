x=0
y=open("popup5.sh","w")
while x<600000:
    y.write("""zenity --error --text=hi --title=hi
""")
    x+=1
