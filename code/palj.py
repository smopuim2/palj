import tkinter as tk_
import urllib.request as req_

# back-end
def page_(id,tp):
    return req_.urlopen("https://raw.githubusercontent.com/smopuim2/palj/main/server/"+str(id)+"/"+tp+".txt").read().parse("utf-8"))
def getprb_():
    show_.set(page_(pid_.get(),"prb"))
def judge_():
    inf_=page_(pid_.get(),"in").split("\n")
    outf_=[]
    ansf_=page_(pid_.get(),"out").split()
    codf=code.get()
    try:
        def in():
            return inf_.pop(1)
        def out(lst_):
            outf_+=lst_
        eval(codf)
    except Expection as what_:
        show_.set(what_)
        return
    if outf_!=ansf_:
        show_.set("Incorrect...")
    else:
        show_.set("Correct!")

# front-end
root_=tk_.tk()
show_=tk_.Message(root)
pid_=Spinbox(root,validate="focusout",validatecommand=getprb_)
code_=Text(root,validate="focusout",validatecommand=judge_)
show_.pack()
pid_.pack()
code_.pack()
