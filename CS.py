import random
from tkinter import *

def password(tmn):
    MAI = 'ABCDEFGHIJKLMNOPQSRTUVWXYZ'
    MIN = 'abcdefghijklmnopqrstuvwxyz'
    NUM = '1234567890'
    SYM = '<=>?@[\]^_`{|}~.'

    pswd = ''
    usd = []
    try:
        tamanho = int(tmn)
    except ValueError:
        tamanho = len(tmn)
    finally:
        while tamanho > 0:
            esc = random.choice(list(MAI+MIN+NUM+SYM))
            if esc not in usd:
                pswd+=esc
                tamanho-=1
                usd.append(esc)
    txtx = Label()
    txtx.configure(text=pswd)
    txtx.place(x=60, y=30)

wnd = Tk()
wnd.geometry('190x65')
wnd.title('Criador de Senhas')
info1 = Label(text="tamanho")
info1.place(x=0, y=0)
res1 = Entry()
res1.place(x=60, y=0)
op1 = Button(text='criar', command=lambda: password(res1.get()))
op1.place(x=5, y=30)

wnd.mainloop()
