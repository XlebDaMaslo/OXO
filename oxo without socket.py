from tkinter import *
import socket
import random
import threading

class OXO():
    def __init__(self):
        #self.sock = socket.socket()
        #self.sock.connect(('localhost', 9090))
        
        self.root = Tk() #основное окно
        self.root.geometry('250x100')
        self.root.title('xoxo')
        self.label = Label(text='Здарова', font='Arial 24')
        self.button = Button(text="Поiхали", width=10, height=2)
        self.button.config(command=self.play)

        self.win = 0
        self.nich = 0
        self.por = 0

        self.place_1 = ''
        self.place_2 = ''
        self.place_3 = ''
        self.place_4 = ''
        self.place_5 = ''
        self.place_6 = ''
        self.place_7 = ''
        self.place_8 = ''
        self.place_9 = ''

        self.label.pack()
        self.button.pack()

        self.root.mainloop()
    def stavka(self,event):
        print(event)
        
        
        #self.c.delete(self.fef[self.v-1])
        #1r ничо дельного не придумал
        if event.x < 150 and event.y < 200:
            self.c.delete(self.fef[0])
            if self.agag == 0:
                self.c.create_oval(50, 100, 150, 200)
                self.place_1 = 'o'
                self.agag = 1
            else:
                self.c.create_line(50, 100, 150, 200)
                self.c.create_line(150, 100, 50, 200)
                self.place_1 = 'x'
                self.agag = 0
        elif event.x > 150 and event.y < 200 and event.x < 250:
            self.c.delete(self.fef[1])
            #self.c.create_oval(150, 100, 250, 200)
            if self.agag == 0:
                self.c.create_oval(150, 100, 250, 200)
                self.place_2 = 'o'
                self.agag = 1
            else:
                self.c.create_line(150, 100, 250, 200)
                self.c.create_line(250, 100, 150, 200)
                self.place_2 = 'x'
                self.agag = 0
        elif event.x > 250 and event.y < 200:
            self.c.delete(self.fef[2])
            #self.c.create_oval(250, 100, 350, 200)
            if self.agag == 0:
                self.c.create_oval(250, 100, 350, 200)
                self.place_3 = 'o'
                self.agag = 1
            else:
                self.c.create_line(250, 100, 350, 200)
                self.c.create_line(350, 100, 250, 200)
                self.place_3 = 'x'
                self.agag = 0
        #2r
        elif event.x < 150 and event.y > 200 and event.y < 300:
            self.c.delete(self.fef[3])
            #self.c.create_oval(50, 200, 150, 300)
            if self.agag == 0:
                self.c.create_oval(50, 200, 150, 300)
                self.place_4 = 'o'
                self.agag = 1
            else:
                self.c.create_line(50, 200, 150, 300)
                self.c.create_line(150, 200, 50, 300)
                self.place_4 = 'x'
                self.agag = 0
        elif event.x > 150 and event.y > 200 and event.x < 250 and event.y < 300:
            self.c.delete(self.fef[4])
            #self.c.create_oval(150, 200, 250, 300)
            if self.agag == 0:
                self.c.create_oval(150, 200, 250, 300)
                self.place_5 = 'o'
                self.agag = 1
            else:
                self.c.create_line(150, 200, 250, 300)
                self.c.create_line(250, 200, 150, 300)
                self.place_5 = 'x'
                self.agag = 0
        elif event.x > 250 and event.y > 200 and event.y < 300:
            self.c.delete(self.fef[5])
            #self.c.create_oval(250, 200, 350, 300)
            if self.agag == 0:
                self.c.create_oval(250, 200, 350, 300)
                self.place_6 = 'o'
                self.agag = 1
            else:
                self.c.create_line(250, 200, 350, 300)
                self.c.create_line(350, 200, 250, 300)
                self.place_6 = 'x'
                self.agag = 0
        #3r
        elif event.x < 150 and event.y > 300:
            self.c.delete(self.fef[6])
            #self.c.create_oval(50, 300, 150, 400)
            if self.agag == 0:
                self.c.create_oval(50, 300, 150, 400)
                self.place_7 = 'o'
                self.agag = 1
            else:
                self.c.create_line(50, 300, 150, 400)
                self.c.create_line(150, 300, 50, 400)
                self.place_7 = 'x'
                self.agag = 0
        elif event.x > 150 and event.y > 300 and event.x < 250:
            self.c.delete(self.fef[7])
            #self.c.create_oval(150, 300, 250, 400)
            if self.agag == 0:
                self.c.create_oval(150, 300, 250, 400)
                self.place_8 = 'o'
                self.agag = 1
            else:
                self.c.create_line(150, 300, 250, 400)
                self.c.create_line(250, 300, 150, 400)
                self.place_8 = 'x'
                self.agag = 0
        elif event.x > 250 and event.y > 200:
            self.c.delete(self.fef[8])
            #self.c.create_oval(250, 300, 350, 400)
            if self.agag == 0:
                self.c.create_oval(250, 300, 350, 400)
                self.place_9 = 'o'
                self.agag = 1
            else:
                self.c.create_line(250, 300, 350, 400)
                self.c.create_line(350, 300, 250, 400)
                self.place_9 = 'x'
                self.agag = 0
        if (self.place_1 == 'o' and self.place_2 == 'o' and self.place_3 == 'o') or (self.place_1 == 'o' and self.place_4 == 'o' and self.place_7 == 'o') or (self.place_4 == 'o' and self.place_5 == 'o' and self.place_6 == 'o') or (self.place_2 == 'o' and self.place_5 == 'o' and self.place_8 == 'o') or (self.place_7 == 'o' and self.place_8 == 'o' and self.place_9 == 'o') or (self.place_3 == 'o' and self.place_6 == 'o' and self.place_9 == 'o') or (self.place_1 == 'o' and self.place_5 == 'o' and self.place_9 == 'o') or (self.place_3 == 'o' and self.place_5 == 'o' and self.place_7 == 'o'):
            self.frame.destroy()
            self.l_won = Label(text='Выиграл O', font='Arial 24')
            self.l_won.pack()
            self.b_restart = Button(text="Ещё хочу", width=10, height=2)
            self.b_restart.config(command=self.restart)
            self.b_restart.pack()
            if int(self.o_or_x) == 0:
                self.win+=1
                ww = 'Won: ' + str(self.win)
                self.l_win.configure(text=ww, font='Arial 24')
            else:
                self.por+=1
                pp = 'Gamover: ' + str(self.por)
                self.l_por.configure(text=pp, font='Arial 24')
                
        elif (self.place_1 == 'x' and self.place_2 == 'x' and self.place_3 == 'x') or (self.place_1 == 'x' and self.place_4 == 'x' and self.place_7 == 'x') or (self.place_4 == 'x' and self.place_5 == 'x' and self.place_6 == 'x') or (self.place_2 == 'x' and self.place_5 == 'x' and self.place_8 == 'x') or (self.place_7 == 'x' and self.place_8 == 'x' and self.place_9 == 'x') or (self.place_3 == 'x' and self.place_6 == 'x' and self.place_9 == 'x') or (self.place_1 == 'x' and self.place_5 == 'x' and self.place_9 == 'x') or (self.place_3 == 'x' and self.place_5 == 'x' and self.place_7 == 'x'):
            self.frame.destroy()
            self.l_won = Label(text='Выиграл X', font='Arial 24')
            self.l_won.pack()
            self.b_restart = Button(text="Ещё хочу", width=10, height=2)
            self.b_restart.config(command=self.restart)
            self.b_restart.pack()
            if int(self.o_or_x) == 1:
                self.win+=1
                ww = 'Won: ' + str(self.win)
                self.l_win.configure(text=ww, font='Arial 24')
            else:
                self.por+=1
                pp = 'Gamover: ' + str(self.por)
                self.l_por.configure(text=pp, font='Arial 24')
        elif (self.place_1 == 'o' or self.place_1 == 'x') and (self.place_2 == 'o' or self.place_2 == 'x') and (self.place_3 == 'o' or self.place_3 == 'x') and (self.place_4 == 'o' or self.place_4 == 'x') and (self.place_5 == 'o' or self.place_5 == 'x') and (self.place_6 == 'o' or self.place_6 == 'x') and (self.place_7 == 'o' or self.place_7 == 'x') and (self.place_8 == 'o' or self.place_8 == 'x') and (self.place_9 == 'o' or self.place_9 == 'x'):
            self.frame.destroy()
            self.l_won = Label(text='Ничья', font='Arial 24')
            self.l_won.pack()
            self.b_restart = Button(text="Ещё хочу", width=10, height=2)
            self.b_restart.config(command=self.restart)
            self.b_restart.pack()

            self.nich+=1
            nn = 'Nichya: ' + str(self.nich)
            self.l_nich.configure(text=nn, font='Arial 24')
            
            
            #pass
    def request(self):
        self.sock.send('Чо там с деньгами?'.encode())
        self.label.destroy()
        self.button.destroy()
        self.label = Label(text='Падажди Второго такого', font='Arial 24')
        self.button = Button(text="Антистресс", width=10, height=2)
        self.label.pack()
        self.button.pack()
        thread = threading.Thread(target=self.wait)
        thread.start()
    def wait(self):
        
        while True:
            try:
                data = self.sock.recv(1024).decode()
                if data == 'wait':
                    pass
                else:
                    self.play()
            except (ConnectionResetError, ConnectionAbortedError):
                return
        #pass
        
    def play(self):
        self.o_or_x = random.randint(0,1)
        self.agag = self.o_or_x
        print(self.o_or_x)
        self.label.destroy()
        self.button.destroy()
        self.root.geometry('400x600')
        self.l_win = Label(text='Won: ', font='Arial 24')
        self.l_win.pack()
        self.l_nich = Label(text='Nichya: ', font='Arial 24')
        self.l_nich.pack()
        self.l_por = Label(text='Gamover: ', font='Arial 24')
        self.l_por.pack()
        self.exit = Button(text="Я всё.", width=10, height=2, command=self.exit)
        self.exit.pack()
        self.play_2()
    def restart(self):
        self.place_1 = ''
        self.place_2 = ''
        self.place_3 = ''
        self.place_4 = ''
        self.place_5 = ''
        self.place_6 = ''
        self.place_7 = ''
        self.place_8 = ''
        self.place_9 = ''
        self.l_won.destroy()
        self.b_restart.destroy()
        self.play_2()
    def play_2(self):
        self.frame = Frame()
        self.c = Canvas(self.frame, width=400, height=600, bg='grey80')
        self.frame.pack()
        self.c.pack()
        
        a = 3
        b=3
        self.v=0
        self.fef=[1,2,3,4,5,6,7,8,9]
        y=100
        for i in range(3):
            print(1)
            a=3
            x=50
            for k in range(3):
                print(0)
                self.fef[self.v] = self.c.create_rectangle(x, y, x+100, y+100,
                           tag="rect",
                           fill="lightgreen")
                self.c.tag_bind(self.fef[self.v],'<Button-1>', self.stavka)
                a-=1
                x+=100
                self.v+=1
            y+=100
            b-=1
    def exit(self):
        print(1)
        #self.sock.close()
        self.root.destroy()
        sys.exit()

        
oleg = OXO()
