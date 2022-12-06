import tkinter as tk
from tkinter import ttk, OptionMenu, StringVar

def howmuchisXpercentofY(a,b):

    ans=a/100*b
    print(f'what is {a}% of {b}?')

    return ans

def XiswhatpercentofY(a,b):

    ans=(a/b)*100
    print(f'{a} is what % of {b}')
    return ans

def YisPpercentofANS(a,b):
    b1=b/100
    ans=(a/b1)
    print(f'So, {a} is what % of {b}')
    return ans

def whatpercentofXisY(a,b):
    ans=(b/a)*100
    print(f'What percentage of {a} is {b}')
    return ans

def PpercentofwhatisY(a,b):
    ans=b*(a/100)
    print(f'how much {a}% af {b} is?')
    return ans

optiuni=['one','two','three']
root=tk.Tk()
root.geometry("400x200")
root.title('Percentage calcualtor')

frame1=tk.Frame(root)

mytext='x/y=p*100'
text=tk.Label(root,text=mytext,borderwidth=1)

text.pack()

t=ttk.Separator(root, orient='horizontal')
t.pack(fill='x')

variable=StringVar(root)
variable.set(optiuni[0])
dropdown=OptionMenu(root,variable,*optiuni)
dropdown.pack()

root.mainloop()

d=howmuchisXpercentofY(10,25)
print('Answer: ',d)
e=int(XiswhatpercentofY(12,40))
print(f"Answer: {e}%")
f=(YisPpercentofANS(9,60))
print(f'Answer: {f:0.0f}')
g=whatpercentofXisY(27,6)
print(f'Answer:{g:0.2f}%')
h=PpercentofwhatisY(20,35)
print(f'Answer:{h}')

