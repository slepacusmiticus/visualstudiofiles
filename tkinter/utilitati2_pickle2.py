#pagina menu unde poti schimba numarul maxim de persoane pe luna
#e nevoie de asa ceva(max nr persoane) ori mai bine lasat la liber

#read file, if empty, or it doesn't exist, ask to create one. 
#first page list of persons in the home, ask do you want 
# to change/edit if yes create list populated with old names(if exist)
#btn to add new entry(person)

#TO DO included in list at the bottom of the names page below it the save the new name list.
#      add edit btn for a name


#FIX needed
#openng the file delets the last character ot the last name

import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import simpledialog




master=Tk()

master.geometry('300x300')

def saveNameList():
    print('from save ',asd1)
    with open("namelist.txt",'w')as f:
        for item in asd1:
            f.write("%s\n" % item)
    print('names saved/writen in list')
    draw_screen(asd1)

def refresh_list():
    #global new_List
    USER_INP = simpledialog.askstring(title="The new person",
                                  prompt="What's the new name?:")
    if USER_INP != '':
        default_list.append(USER_INP)
        #check for duplicate names
        print(default_list)
    
    
        for windw in master.winfo_children():
            windw.destroy()
        
        draw_screen(default_list)
    else:
        print("Name wasn't provided!")

def delete_fr_list():
    USER_INP2 = simpledialog.askinteger(title="Delete the x-th person",
                                  prompt="What's the position/nr you want to delete?:")
    USER_INP2=USER_INP2-1                              
                                  
    print(USER_INP2)
    default_list.pop(USER_INP2)
    print(default_list)
    
    for windw in master.winfo_children():
        windw.destroy()
    draw_screen(default_list)

def draw_screen(list):
    #delete by nmae not just by index(checkif there's more than one with same name)
    print(list)

    persoane=list
    frame1=Frame(master)
    frame2=Frame(master)
    frame3=Frame(master)
    frame4=Frame(master)
    frame1.grid(row=0, sticky="ew")
    frame2.grid(row=1, sticky="nsew")
    frame3.grid(row=2, sticky="nsew")
    frame4.grid(row=3, sticky="ew")
        
        
    mylabel=Label(frame2, text='Modifica list pers:')
    mylabel.grid(row=0,column=0)
    
        #persoane=self.persoane
    global asd1
    asd1=[]
    i=1
    #name_var = StringVar()
    for each in persoane:
        L1 = Label(frame3, text="Pers_"+str(i)+':')
        L1.grid(row=i, column=0, sticky=W)
        E1 = Entry(frame3)

        E1.insert(END, persoane[i-1])
        E1.grid(row=i, column=1,sticky=W)
        i=i+1
        asd= E1.get()
        asd1.append(asd)
    print('QQQQQQQQQ',asd1)

    #separator
    with open('/home/dumitru/Dropbox/visualstudiofiles/tkinter/namelist.txt','r')as f:
        nms = [line.strip() for line in f.readlines()]

    #nms=default_list
    print(nms)
    #### daca lista e empty imi da s2 ca referenced before assignement;  for empty namelist.txt  do XXX  if nms='' nms='nobody'
    if not nms:
        nms='List_empty'
    for element in nms:
        s2 = ' '.join(nms)
    print(s2)
    s1='Pe lista: '
    strg= s1+s2
    mlb=Label(frame1, text=strg)
    mlb.grid(row=0,column=1)
    #separator

    btn1=Button(frame4,text='Add new',command=refresh_list) 
    btn1.grid(row=0,column=1)
    btn2=Button(frame4,text='Del a pers',command=delete_fr_list) 
    btn2.grid(row=0,column=2)
    btn2=Button(frame4,text='Save name list',command=saveNameList) 
    btn2.grid(row=0,column=3)
    
def run_util():
    global default_list
    default_list=[]
    #default_list=['Miti','Davis', 'Rebeca','Andrei', 'Nur', 'Dumitru']
    with open(r'/home/dumitru/Dropbox/visualstudiofiles/tkinter/namelist.txt','r')as nf:
        for line in nf:
            x=line[:-1]
            default_list.append(x)
    print(default_list)
    draw_screen(default_list)

run_util()
#MyGUI.draw_gui
master.mainloop()

