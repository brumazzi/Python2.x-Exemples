#!/usr/bin/env python

class TAG:
    COMMENT = "1"
    VAR_TYPE = "2"
    TEXT = "3"
    RWORD = "4"

text = None

try:
    from Tkinter import *
except:
    from tkinter import *

def check_str(str1, str2, pos):
    for x in range(len(str2)):
        if str2[x] != str1[pos+x]:
            return False

    return True

def onclick():
    pass

def key_down(evt):
    t = text.get("1.0",END)
    line = 1
    left = 0
    x=0
    buff = 1
    bs = False
    si = 0;
    while x < len(t):
        if check_str(t, "void ", x):
            text.tag_add(TAG.VAR_TYPE, "%i.%i" %(line,left), "%i.%i" %(line,left+4))
            buff = 4
        elif check_str(t, "int ", x):
            text.tag_add(TAG.VAR_TYPE, "%i.%i" %(line,left), "%i.%i" %(line,left+3))
            buff = 3
        elif check_str(t, "char ", x):
            text.tag_add(TAG.VAR_TYPE, "%i.%i" %(line,left), "%i.%i" %(line,left+4))
            buff = 4
        elif check_str(t, "return ", x):
            text.tag_add(TAG.RWORD, "%i.%i" %(line,left), "%i.%i" %(line,left+6))
            buff = 6
        elif check_str(t, "const ", x):
            text.tag_add(TAG.VAR_TYPE, "%i.%i" %(line,left), "%i.%i" %(line,left+5))
            buff = 5
        if t[x] == '"':
            bs = not bs
            if bs:
                si = left
            if not bs:
                text.tag_add(TAG.TEXT, "%i.%i" %(line,si), "%i.%i" %(line,left+1))
        if(t[x] == '\n'):
            line += 1
            left = -1

        left += buff
        x += buff
        buff = 1

    return True

root = Tk()
svar = StringVar()
text = Text(root)
text.bind('<Key>', key_down)
text.tag_config(TAG.COMMENT, foreground="blue")
text.tag_config(TAG.VAR_TYPE, foreground="green")
text.tag_config(TAG.TEXT, foreground="red")
text.tag_config(TAG.RWORD, foreground="yellow")

text.pack()

mainloop()
