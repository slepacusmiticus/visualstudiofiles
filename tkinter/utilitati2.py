#pagina menu unde poti schimba numarul maxim de persoane pe luna
#e nevoie de asa ceva(max nr persoane) ori mai bine lasat la liber

#read file, if empty, or it doesn't exist, ask to create one. 
#first page list of persons in the home, ask do you want 
# to change/edit if yes create list populated with old names(if exist)
#btn to add new entry(person)
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import simpledialog

def name():
    name='Grigore'
    # MyGUI.refresh()
    # MyGUI.add_item(name)
    return name
    # #persoana=Varr()
    # pers1=Pers()
    # pers1.add_item("grigore")
    # # frame1.destroy()
    # # frame2.destroy()
    # # frame3.destroy()
    # print(pers1.items)
    # create_frames()



master=Tk()




master.geometry('300x300')


def refresh_list():
    #global new_List
    USER_INP = simpledialog.askstring(title="The new person",
                                  prompt="What's the new name?:")
    default_list.append(USER_INP)
    #check for duplicate names
    print(default_list)
    
    
    for windw in master.winfo_children():
        windw.destroy()
    
    draw_screen(default_list)

def delete_fr_list():
    USER_INP2 = simpledialog.askinteger(title="Delete the n-th person",
                                  prompt="What's the position/nr you want to delelte?:")
    USER_INP2=USER_INP2-1                              
                                  
    print(USER_INP2)
    default_list.pop(USER_INP2)
    print(default_list)
    
    for windw in master.winfo_children():
        windw.destroy()
    draw_screen(default_list)

def draw_screen(list):
    print(list)

    persoane=list
    frame1=Frame(master)
    frame2=Frame(master)
    frame3=Frame(master)
    frame1.grid(row=0, sticky="ew")
    frame2.grid(row=1, sticky="nsew")
    frame3.grid(row=2, sticky="ew")
        
        
    mylabel=Label(frame1, text='Lista pers:')
    mylabel.grid(row=0,column=0)

        #persoane=self.persoane
    i=1
    for each in persoane:
        L1 = Label(frame2, text="Pers_"+str(i)+':')
        L1.grid(row=i,column=0, sticky=W)
        E1 = Entry(frame2)
        E1.insert(END,persoane[i-1])
        E1.grid(row=i, column=1,sticky=W)
        i=i+1
    #separator
    btn1=Button(frame3,text='Add new',command=refresh_list) 
    btn1.grid(row=0,column=1)
    btn2=Button(frame3,text='Del a pers',command=delete_fr_list) 
    btn2.grid(row=0,column=2)
    btn2=Button(frame3,text='Save new list') 
    btn2.grid(row=0,column=3)
    
def run_util():
    global default_list
    default_list=['Miti','Davis', 'Rebeca','Andrei', 'Nur', 'Dumitru']
    
    draw_screen(default_list)

run_util()
#MyGUI.draw_gui
master.mainloop()

