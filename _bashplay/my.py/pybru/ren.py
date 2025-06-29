def delren(fn,delfe,nfe,delchl,delchr):
    fnx=fn
    if delfe:
        if "." in fnx:
            z=fnx.split(".")
            fnx=z[0]
        else:
            class NoFileExtension(Exception):
                    pass
            try:
                raise NoFileExtension
            except NoFileExtention:
                print(f'''File {fnx} in <filename>:
                          {fnx}
                          File ren.py in delren, in line 2:
                          fnx=fn
                          File ren.py in delren, in line 4 and 6:
                          if "." in fnx:
                          else:
                          File ren.py in delren, in line 7 and 8:
                          class NoFileExtension(Exception):
                            pass
                          File ren.py in delren, in line 9 and 10:
                          try:
                            raise NoFileExtension
                          NoFileExtensionError: {fnx} doesn't have an extension''')
    if nfe != "":
        fnx2=fnx
        fnx2+="."
        fnx2+=nfe
        fnx=fnx2
    if int(delchl)!=0:
        x=1
        fnr=fnx
        while int(delchl)>x:
            fnr-=fnr[0]
            x+=1
        fnx=fnr
    if int(delchr)!=0:
        x=1
        fnr2=fnx
        while x<int(delchr):
            fnr[len(fnr)-1]=""
            x+=1
        fnx=fnr
    return fnx
def adren(fn,lfx,rfx,adnumbffe,adnumaffe,nfn):
    fnx=fn
    fnx+=rfx
    lf=lfx
    lf+=fnx
    fnx=lf
    z=fnx.split(".")
    fnx2=z[0]
    fnx2+=str(adnumbffe)
    if nfn!="":
        fnx2=nfn
    fnx2+="."
    fnx2+=z[1]
    fnx=fnx2
    fnx+=adnumaffe
    return fnx
def perms(perms,fn):
    return f"chmod {perms} {fn}"
