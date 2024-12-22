import tkinter as tk
import math

w, l = 650, 650
checkbox, check, check1, check2, check3, check4 = 0, 0, 0, 0, 0, 0

def checked():
    if check.get() == True:
        draw_line()
    else:
        cvs.delete('bgraph')

def checked1():
    global check1
    if check1.get() == True:
        draw_quadra()
    else:
        cvs.delete('rgraph')

def checked2():
    global check2
    if check2.get() == True:
        draw_rat()
    else:
        cvs.delete('ggraph')

def checked3():
    global check3
    if check3.get() == True:
        draw_irat()
    else:
        cvs.delete('pgraph')

def checked4():
    global check4
    if check4.get() == True:
        draw_cir()
    else:
        cvs.delete('brgraph')
        
checkbox = tk.Tk()
checkbox.title('Which graph?')
checkbox.geometry('300x130')
checkbox.resizable(False, False)
            
check = tk.BooleanVar()
check.set(False)

cbtn = tk.Checkbutton(checkbox, text='일차함수', variable=check, command=checked)
cbtn.pack()

check1 = tk.BooleanVar()
check1.set(False)

cbtn1 = tk.Checkbutton(checkbox, text='이차함수', variable=check1, command=checked1)
cbtn1.pack()

check2 = tk.BooleanVar()
check2.set(False)

cbtn2 = tk.Checkbutton(checkbox, text='유리함수', variable=check2, command=checked2)
cbtn2.pack()

check3 = tk.BooleanVar()
check3.set(False)

cbtn3 = tk.Checkbutton(checkbox, text='무리함수', variable=check3, command=checked3)
cbtn3.pack()

check4 = tk.BooleanVar()
check4.set(False)

cbtn4 = tk.Checkbutton(checkbox, text='원의 방정식', variable=check4, command=checked4)
cbtn4.pack()

# Slider for Linear Function #############################################################################################################

luser_input1, luser_input2 = 0, 0
al, bl, q = 0, 0, 0
    
def show_lvalue1(val):
    global al, bl, llabel1
    al = float(val)
    llabel1.config(text=f"a: {val}")
    if check.get() == True:
        draw_line()
    
def show_lvalue2(val):
    global al, bl
    bl = float(val)
    llabel2.config(text=f"b: {val}")
    if check.get() == True:
        draw_line()

lslider = tk.Tk()
lslider.geometry('324x150')
lslider.title("일차함수의 계수")
lslider.resizable(False, False)

lslider1 = tk.Scale(lslider, from_=-10, to=10, length=300, resolution = 0.5, orient="horizontal", command=show_lvalue1)
lslider1.pack()

llabel1 = tk.Label(lslider, text="a: 0")
llabel1.pack()

lslider2 = tk.Scale(lslider, from_=-200, to=200, length=300, resolution = 1, orient="horizontal", command=show_lvalue2)
lslider2.pack()

llabel2 = tk.Label(lslider, text="b: 0")
llabel2.pack()

# Slider for Quadratic Function #############################################################################################################

user_input1, user_input2, user_input3 = 0, 0, 0
a, b, c, q = 0, 0, 0, 0

def show_value1(val):
    global a, b, c
    a = float(val)
    label1.config(text=f"a: {val}")
    if check1.get() == True:
        draw_quadra()
    
def show_value2(val):
    global a, b, c
    b = float(val)
    label2.config(text=f"b: {val}")
    if check1.get() == True:
        draw_quadra()
    
def show_value3(val):
    global a, b, c
    c = float(val)
    label3.config(text=f"c: {val}")
    if check1.get() == True:
        draw_quadra()
    
slider = tk.Tk()
slider.geometry('324x200')
slider.title("이차함수의 계수")
slider.resizable(False, False)

slider1 = tk.Scale(slider, from_=-2, to=2, length=300, resolution = 0.05, orient="horizontal", command=show_value1)
slider1.pack()

label1 = tk.Label(slider, text="a: 0")
label1.pack()

slider2 = tk.Scale(slider, from_=-100, to=100, length=300, resolution = 0.5, orient="horizontal", command=show_value2)
slider2.pack()

label2 = tk.Label(slider, text="b: 0")
label2.pack()

slider3 = tk.Scale(slider, from_=-200, to=200, length=300, resolution = 0.5, orient="horizontal", command=show_value3)
slider3.pack()

label3 = tk.Label(slider, text="c: 0")
label3.pack()

# Slider for Rational Function ##############################################################################################

ruser_input1, ruser_input2, ruser_input3, ruser_input4 = 0, 0, 0, 0
ar, br, cr, dr, q = 1, 1, 0, 0, 0

def rshow_value1(val):
    global ar, br, cr, dr
    ar = float(val)
    rlabel1.config(text=f"a: {val}")
    if check2.get() == True:
        draw_rat()
    
def rshow_value2(val):
    global ar, br, cr, dr
    br = float(val)
    rlabel2.config(text=f"b: {val}")
    if check2.get() == True:
        draw_rat()
    
def rshow_value3(val):
    global ar, br, cr, dr
    cr = float(val)
    rlabel3.config(text=f"c: {val}")
    if check2.get() == True:
        draw_rat()

def rshow_value4(val):
    global ar, br, cr, dr
    dr = float(val)
    rlabel4.config(text=f"d: {val}")
    if check2.get() == True:
        draw_rat()
        
rslider = tk.Tk()
rslider.geometry('405x250')
rslider.title("유리함수의 계수")
rslider.resizable(False, False)

rslider1 = tk.Scale(rslider, from_=-5, to=5, length=300, resolution = 0.1, orient="horizontal", command=rshow_value1)
rslider1.pack()

rlabel1 = tk.Label(rslider, text="a: 0")
rlabel1.pack()

rslider2 = tk.Scale(rslider, from_=-100, to=100, length=300, resolution = 0.5, orient="horizontal", command=rshow_value2)
rslider2.pack()

rlabel2 = tk.Label(rslider, text="b: 0")
rlabel2.pack()

rslider3 = tk.Scale(rslider, from_=-200, to=200, length=300, resolution = 1, orient="horizontal", command=rshow_value3)
rslider3.pack()

rlabel3 = tk.Label(rslider, text="c: 0")
rlabel3.pack()

rslider4 = tk.Scale(rslider, from_=-100, to=100, length=300, resolution = 0.5, orient="horizontal", command=rshow_value4)
rslider4.pack()

rlabel4 = tk.Label(rslider, text="d: 0")
rlabel4.pack()

# Slider for Irrational Function ##############################################################################################

iruser_input1, iruser_input2, iruser_input3, iruser_input4 = 0, 0, 0, 0
iar, ibr, icr, idr, q = 0, 0, 0, 0, 0

def irshow_value1(val):
    global iar, ibr, icr, idr
    iar = float(val)
    irlabel1.config(text=f"a: {val}")
    if check3.get() == True:
        draw_irat()
    
def irshow_value2(val):
    global iar, ibr, icr, idr
    ibr = float(val)
    irlabel2.config(text=f"b: {val}")
    if check3.get() == True:
        draw_irat()
    
def irshow_value3(val):
    global iar, ibr, icr, idr
    icr = float(val)
    irlabel3.config(text=f"c: {val}")
    if check3.get() == True:
        draw_irat()

def irshow_value4(val):
    global iar, ibr, icr, idr
    idr = float(val)
    irlabel4.config(text=f"d: {val}")
    if check3.get() == True:
        draw_irat()

irslider = tk.Tk()
irslider.geometry('405x250')
irslider.title("무리함수의 계수")
irslider.resizable(False, False)

irslider1 = tk.Scale(irslider, from_=-5, to=5, length=300, resolution = 0.1, orient="horizontal", command=irshow_value1)
irslider1.pack()

irlabel1 = tk.Label(irslider, text="a: 0")
irlabel1.pack()

irslider2 = tk.Scale(irslider, from_=-200, to=200, length=300, resolution = 1, orient="horizontal", command=irshow_value2)
irslider2.pack()

irlabel2 = tk.Label(irslider, text="b: 0")
irlabel2.pack()

irslider3 = tk.Scale(irslider, from_=-200, to=200, length=300, resolution = 1, orient="horizontal", command=irshow_value3)
irslider3.pack()

irlabel3 = tk.Label(irslider, text="c: 0")
irlabel3.pack()

irslider4 = tk.Scale(irslider, from_=-200, to=200, length=300, resolution = 1, orient="horizontal", command=irshow_value4)
irslider4.pack()

irlabel4 = tk.Label(irslider, text="d: 0")
irlabel4.pack()

# Slider for Quadratic Function #############################################################################################################

cuser_input1, cuser_input2, cuser_input3 = 0, 0, 0
ca, cb, cc, q = 0, 0, 20, 0

def cshow_value1(val):
    global ca, cb, cc
    ca = float(val)
    clabel1.config(text=f"a: {val}")
    if check4.get() == True:
        draw_cir()
    
def cshow_value2(val):
    global ca, cb, cc
    cb = float(val)
    clabel2.config(text=f"b: {val}")
    if check4.get() == True:
        draw_cir()
    
def cshow_value3(val):
    global ca, cb, cc
    cc = float(val)
    clabel3.config(text=f"r: {val}")
    if check4.get() == True:
        draw_cir()
    
cslider = tk.Tk()
cslider.geometry('324x200')
cslider.title("원의 방정식")
cslider.resizable(False, False)

cslider1 = tk.Scale(cslider, from_=-200, to=200, length=300, resolution = 1, orient="horizontal", command=cshow_value1)
cslider1.pack()

clabel1 = tk.Label(cslider, text="a: 0")
clabel1.pack()

cslider2 = tk.Scale(cslider, from_=-200, to=200, length=300, resolution = 1, orient="horizontal", command=cshow_value2)
cslider2.pack()

clabel2 = tk.Label(cslider, text="b: 0")
clabel2.pack()

cslider3 = tk.Scale(cslider, from_=1, to=250, length=300, resolution = 1, orient="horizontal", command=cshow_value3)
cslider3.pack()

clabel3 = tk.Label(cslider, text="r: 0")
clabel3.pack()

# Graph #######################################################################################################################

def draw_quadra():
    global a, b, c, cvs, label5
    x=[]
    cvs.delete('rgraph')
    for i in range(-w, w):
        x.append([i + w/2, -1*(a*(i**2) + b*i + c) + l/2])
    cvs.create_line(x, fill='red', width = 2, smooth=True, tag='rgraph')
    label5.configure(text=f"{a}x^2 + {b}x + {c}")

def draw_line():
    global al, bl, cvs, llabel5
    x=[]
    cvs.delete('bgraph')
    for i in range(-w, w):
        x.append([i + w/2, -1*(al*i + bl) + l/2])
    cvs.create_line(x, fill='skyblue', width = 2, tag='bgraph')
    llabel5.configure(text=f"{al}x + {bl}")

def draw_rat():
    global ar, br, cr, dr, cvs, rlabel5
    x=[]
    y=[]
    cvs.delete('ggraph')

    if ar == 0:
        ar = 0.01
        
    for i in range(-w, int(-br/ar)):
        x.append([i + w/2, -cr/(ar*i + br) - dr + l/2])

    if cr/(ar*(-br/ar-0.5) + br) + dr > dr:
        x.append([-br/ar-0.5+w/2, 0])
    else:
        x.append([-br/ar-0.5+w/2, l])

    try:
        cvs.create_line(x, fill='green', width = 2, smooth=True, tag='ggraph')
    except:
        pass

    if cr/(ar*(-br/ar+0.5) + br) + dr > dr:
        y.append([-br/ar+0.5+w/2, 0])
    else:
        y.append([-br/ar+0.5+w/2, l])
        
    for i in range(int(-br/ar)+1, w):
        y.append([i + w/2, -cr/(ar*i + br) - dr + l/2])
        
    try:
        cvs.create_line(y, fill='green', width = 2, smooth=True, tag='ggraph')
    except:
        pass

    cvs.create_line(0, -dr+l/2, w, -dr+l/2, fill='greenyellow', width = 1.2, smooth=True, tag='ggraph')
    cvs.create_line(-br/ar+w/2, 0, -br/ar+w/2, 600, fill='greenyellow', width = 1.2, smooth=True, tag='ggraph')
    
    rlabel5.configure(text=f"({cr} / {ar}x + {br}) + {dr}")

def draw_irat():
    global iar, ibr, icr, idr, cvs, irlabel5
    x=[]
    
    cvs.delete('pgraph')

    if ibr == 0:
        ibr = 0.01
    if iar*ibr > 0:
        x.append([-icr/ibr+w/2, -idr+l/2])
    for i in range(-w, w):
        if ibr*i+icr >= 0:
            x.append([i + w/2, -iar*math.sqrt(ibr*i+icr)-idr + l/2])
    if iar*ibr < 0:
        x.append([-icr/ibr+w/2, -idr+l/2])
    cvs.create_line(x, fill='purple', width = 2, smooth=True, tag='pgraph')
    
    irlabel5.configure(text=f"{iar}sqrt({ibr}x + {icr}) + {idr}")

def draw_cir():
    global ca, cb, cc, cvs, clabel5
    
    x=[]
    y=[]
    
    cvs.delete('brgraph')

    for i in range(-w, w):
        if cc**2-(i-ca)**2 >= 0:
            x.append([i + w/2, -math.sqrt(cc**2-(i-ca)**2)-cb + l/2])
            
    cvs.create_line(x, fill='brown', width = 2, smooth=True, tag='brgraph')

    for i in range(-w, w):
        if cc**2-(i-ca)**2 >= 0:
            y.append([i + w/2, math.sqrt(cc**2-(i-ca)**2)-cb + l/2])

    cvs.create_line(y, fill='brown', width = 2, smooth=True, tag='brgraph')
    
    clabel5.configure(text=f"(x - {ca})^2 + (y - {cb})^2 = {cc}^2")

# User Settings #######################################################################################
def userinput(e):
    global user_input1, user_input2, user_input3, luser_input1, luser_input2, ruser_input1, ruser_input2, ruser_input3, ruser_input4
    global iruser_input1, iruser_input2, iruser_input3, iruser_input4, q
    
    if e.keysym == '1':
        q = tk.Tk()
        q.geometry('300x100')
        q.title('User Settings')
        q.resizable(False, False)

        lab = tk.Label(q, text='일차함수 a, b')
        lab.pack()
        luser_input1 = tk.Entry(q)
        luser_input1.pack()
        luser_input2 = tk.Entry(q)
        luser_input2.pack()

        btn = tk.Button(q)
        btn.config(text='a, b | Submit', width = 12, command=pressl)
        btn.pack()

        q.mainloop()
        
    if e.keysym == '2':
        q = tk.Tk()
        q.geometry('300x120')
        q.title('User Settings')
        q.resizable(False, False)

        lab = tk.Label(q, text='이차함수 a, b, c')
        lab.pack()
        user_input1 = tk.Entry(q)
        user_input1.pack()
        user_input2 = tk.Entry(q)
        user_input2.pack()
        user_input3 = tk.Entry(q)
        user_input3.pack()

        btn = tk.Button(q)
        btn.config(text='a, b, c | Submit', width = 15, command=press)
        btn.pack()

        q.mainloop()

    if e.keysym == '3':
        q = tk.Tk()
        q.geometry('300x150')
        q.title('User Settings')
        q.resizable(False, False)

        lab = tk.Label(q, text='유리함수 a, b, c, d')
        lab.pack()
        ruser_input1 = tk.Entry(q)
        ruser_input1.pack()
        ruser_input2 = tk.Entry(q)
        ruser_input2.pack()
        ruser_input3 = tk.Entry(q)
        ruser_input3.pack()
        ruser_input4 = tk.Entry(q)
        ruser_input4.pack()

        btn = tk.Button(q)
        btn.config(text='a, b, c, d | Submit', width = 18, command=pressr)
        btn.pack()

        q.mainloop()

    if e.keysym == '4':
        q = tk.Tk()
        q.geometry('300x150')
        q.title('User Settings')
        q.resizable(False, False)

        lab = tk.Label(q, text='무리함수 a, b, c, d')
        lab.pack()
        iruser_input1 = tk.Entry(q)
        iruser_input1.pack()
        iruser_input2 = tk.Entry(q)
        iruser_input2.pack()
        iruser_input3 = tk.Entry(q)
        iruser_input3.pack()
        iruser_input4 = tk.Entry(q)
        iruser_input4.pack()

        btn = tk.Button(q)
        btn.config(text='a, b, c, d | Submit', width = 18, command=pressir)
        btn.pack()

        q.mainloop()

    if e.keysym == '5':
        q = tk.Tk()
        q.geometry('300x120')
        q.title('User Settings')
        q.resizable(False, False)

        lab = tk.Label(q, text='원의 방정식 a, b, r')
        lab.pack()
        cuser_input1 = tk.Entry(q)
        cuser_input1.pack()
        cuser_input2 = tk.Entry(q)
        cuser_input2.pack()
        cuser_input3 = tk.Entry(q)
        cuser_input3.pack()

        btn = tk.Button(q)
        btn.config(text='a, b, r | Submit', width = 15, command=pressc)
        btn.pack()

        q.mainloop()
        
def press():
    global a, b, c, user_input1, user_input2, user_input3, q, check1
    a = float(user_input1.get())
    b = float(user_input2.get())
    c = float(user_input3.get())
    q.destroy()
    check1.set(True)
    draw_quadra()

def pressl():
    global al, bl, luser_input1, luser_input2, q, check
    al = float(luser_input1.get())
    bl = float(luser_input2.get())
    q.destroy()
    check.set(True)
    draw_line()

def pressr():
    global ar, br, cr, dr, ruser_input1, ruser_input2, ruser_input3, ruser_input4, q, check2
    ar = float(ruser_input1.get())
    br = float(ruser_input2.get())
    cr = float(ruser_input3.get())
    dr = float(ruser_input4.get())
    q.destroy()
    check2.set(True)
    draw_rat()

def pressir():
    global iar, ibr, icr, idr, iruser_input1, iruser_input2, iruser_input3, iruser_input4, q, check3
    iar = float(iruser_input1.get())
    ibr = float(iruser_input2.get())
    icr = float(iruser_input3.get())
    idr = float(iruser_input4.get())
    q.destroy()
    check3.set(True)
    draw_irat()

def press():
    global ca, cb, cc, cuser_input1, cuser_input2, cuser_input3, q, check4
    ca = float(cuser_input1.get())
    cb = float(cuser_input2.get())
    cc = float(cuser_input3.get())
    q.destroy()
    check4.set(True)
    draw_cir()

graph = tk.Tk()
graph.geometry(f'{w}x{l}')
graph.title('Graph')
graph.resizable(False, False)

cvs = tk.Canvas(graph, width = 1000, height = 1000, bg = 'white')
cvs.pack()

cvs.create_line(w/2,0,w/2,l)
cvs.create_line(0,l/2,w,l/2)

xa = tk.Label(graph, text="x")
xa.pack()
xa.place(x=5, y=l/2+5)

ya = tk.Label(graph, text="y")
ya.pack()
ya.place(x=w/2+5, y=5)

o = tk.Label(graph, text="O")
o.pack()
o.place(x=w/2-20, y=l/2+5)

label5 = tk.Label(graph, text=f"{a}x^2 + {b}x + {c}", bg='red')
label5.pack()
label5.place(x=20, y=l-125)

llabel5 = tk.Label(graph, text=f"{al}x + {bl}", bg='skyblue')
llabel5.pack()
llabel5.place(x=20, y=l-150)

rlabel5 = tk.Label(graph, text=f"({cr} / {ar}x + {br}) + {dr}", bg='green')
rlabel5.pack()
rlabel5.place(x=20, y=l-100)

irlabel5 = tk.Label(graph, text=f"{iar}sqrt({ibr}x + {icr}) + {idr}", bg='purple')
irlabel5.pack()
irlabel5.place(x=20, y=l-75)

clabel5 = tk.Label(graph, text=f"(x - {ca})^2 + (y - {cb})^2 = {cc}^2", bg='brown')
clabel5.pack()
clabel5.place(x=20, y=l-50)

checkbox.bind('<KeyRelease>', userinput)
graph.bind('<KeyRelease>', userinput)
slider.bind('<KeyRelease>', userinput)
lslider.bind('<KeyRelease>', userinput)
rslider.bind('<KeyRelease>', userinput)
irslider.bind('<KeyRelease>', userinput)
cslider.bind('<KeyRelease>', userinput)

input()

checkbox.mainloop()
graph.mainloop()
slider.mainloop()
lslider.mainloop()
rslider.mainloop()
irslider.mainloop()
cslider.mainloop()
