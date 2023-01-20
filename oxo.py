from tkinter import *
import socket #импорт файла для работы с сокетами
import random
import threading
import sys

class OXO():
    def __init__(self):
        self.setka_o = [(50, 100, 150, 200),(150, 100, 250, 200),(250, 100, 350, 200),
                        (50, 200, 150, 300),(150, 200, 250, 300),(250, 200, 350, 300),
                        (50, 300, 150, 400),(150, 300, 250, 400),(250, 300, 350, 400)]
        
        self.setka_x = [((50, 100, 150, 200), (150, 100, 50, 200)), ((150, 100, 250, 200), (250, 100, 150, 200)), ((250, 100, 350, 200),(350, 100, 250, 200)),
                        ((50, 200, 150, 300), (150, 200, 50, 300)), ((150, 200, 250, 300), (250, 200, 150, 300)), ((250, 200, 350, 300), (350, 200, 250, 300)),
                        ((50, 300, 150, 400), (150, 300, 50, 400)), ((150, 300, 250, 400), (250, 300, 150, 400)), ((250, 300, 350, 400), (350, 300, 250, 400))]
        
        
        self.root = Tk() #основное окно
        self.root.geometry('250x100')
        self.root.title('xoxo')
        self.label = Label(text='Здарова', font='Arial 24')
        self.button = Button(text="Поiхали", width=10, height=2)
        self.button.config(command=self.connect)

        self.win = 0
        self.nich = 0
        self.por = 0
        self.rez = 0

        self.place = ['','','','','','','','','']
        self.hod_place = []

        self.label.pack()
        self.button.pack()

        self.root.mainloop()
    def stavka(self,event):
        print(event)
        #self.proverochka()
        
        #self.c.delete(self.fef[self.v-1])
        #1r ничо дельного не придумал
        if event.x < 150 and event.y < 200:
            for i in self.hod_place:
                if i == 0:
                    return
            if self.hod:
                self.c.delete(self.fef[0])
                if self.agag == 0:
                    self.c.create_oval(50, 100, 150, 200)
                    self.place[0] = 'o'
                    #self.agag = 1
                else:
                    self.c.create_line(50, 100, 150, 200)
                    self.c.create_line(150, 100, 50, 200)
                    self.place[0] = 'x'
                    #self.agag = 0
                self.hod = False
                self.hod_place.append(0)

                self.proverochka()
                mm = str(0) + str(self.place[0]) + str(self.hod) + str(self.rez)
                print(mm)
                
                self.sock.send(mm.encode())
            else:
                pass
        elif event.x > 150 and event.y < 200 and event.x < 250:
            for i in self.hod_place:
                if i == 1:
                    return
            if self.hod:
                self.c.delete(self.fef[1])
                #self.c.create_oval(150, 100, 250, 200)
                if self.agag == 0:
                    self.c.create_oval(150, 100, 250, 200)
                    self.place[1] = 'o'
                    #self.agag = 1
                else:
                    self.c.create_line(150, 100, 250, 200)
                    self.c.create_line(250, 100, 150, 200)
                    self.place[1] = 'x'
                    #self.agag = 0
                self.hod = False
                self.hod_place.append(1)

                self.proverochka()
                mm = str(1) + str(self.place[1]) + str(self.hod) + str(self.rez)
                print(mm)
                self.sock.send(mm.encode())
            else:
                pass
        elif event.x > 250 and event.y < 200:
            for i in self.hod_place:
                if i == 2:
                    return
            if self.hod:
                self.c.delete(self.fef[2])
                #self.c.create_oval(250, 100, 350, 200)
                if self.agag == 0:
                    self.c.create_oval(250, 100, 350, 200)
                    self.place[2] = 'o'
                    #self.agag = 1
                else:
                    self.c.create_line(250, 100, 350, 200)
                    self.c.create_line(350, 100, 250, 200)
                    self.place[2] = 'x'
                    #self.agag = 0
                self.hod = False
                self.hod_place.append(2)

                self.proverochka()
                mm = str(2) + str(self.place[2]) + str(self.hod) + str(self.rez)
                print(mm)
                self.sock.send(mm.encode())
            else:
                pass
        #2r
        elif event.x < 150 and event.y > 200 and event.y < 300:
            for i in self.hod_place:
                if i == 3:
                    return
            if self.hod:
                self.c.delete(self.fef[3])
                #self.c.create_oval(50, 200, 150, 300)
                if self.agag == 0:
                    self.c.create_oval(50, 200, 150, 300)
                    self.place[3] = 'o'
                    #self.agag = 1
                else:
                    self.c.create_line(50, 200, 150, 300)
                    self.c.create_line(150, 200, 50, 300)
                    self.place[3] = 'x'
                    #self.agag = 0
                self.hod = False
                self.hod_place.append(3)

                self.proverochka()
                mm = str(3) + str(self.place[3]) + str(self.hod) + str(self.rez)
                print(mm)
                self.sock.send(mm.encode())
            else:
                pass
        elif event.x > 150 and event.y > 200 and event.x < 250 and event.y < 300:
            for i in self.hod_place:
                if i == 4:
                    return
            if self.hod:
                self.c.delete(self.fef[4])
                #self.c.create_oval(150, 200, 250, 300)
                if self.agag == 0:
                    self.c.create_oval(150, 200, 250, 300)
                    self.place[4] = 'o'
                    #self.agag = 1
                else:
                    self.c.create_line(150, 200, 250, 300)
                    self.c.create_line(250, 200, 150, 300)
                    self.place[4] = 'x'
                    #self.agag = 0
                self.hod = False
                self.hod_place.append(4)
                
                self.proverochka()
                mm = str(4) + str(self.place[4]) + str(self.hod) + str(self.rez)
                print(mm)
                self.sock.send(mm.encode())
            else:
                pass
        elif event.x > 250 and event.y > 200 and event.y < 300:
            for i in self.hod_place:
                if i == 5:
                    return
            if self.hod:
                self.c.delete(self.fef[5])
                #self.c.create_oval(250, 200, 350, 300)
                if self.agag == 0:
                    self.c.create_oval(250, 200, 350, 300)
                    self.place[5] = 'o'
                    #self.agag = 1
                else:
                    self.c.create_line(250, 200, 350, 300)
                    self.c.create_line(350, 200, 250, 300)
                    self.place[5] = 'x'
                    #self.agag = 0
                self.hod = False
                self.hod_place.append(5)

                self.proverochka()
                mm = str(5) + str(self.place[5]) + str(self.hod) + str(self.rez)
                print(mm)
                self.sock.send(mm.encode())
            else:
                pass
        #3r
        elif event.x < 150 and event.y > 300:
            for i in self.hod_place:
                if i == 6:
                    return
            if self.hod:
                self.c.delete(self.fef[6])
                #self.c.create_oval(50, 300, 150, 400)
                if self.agag == 0:
                    self.c.create_oval(50, 300, 150, 400)
                    self.place[6] = 'o'
                    #self.agag = 1
                else:
                    self.c.create_line(50, 300, 150, 400)
                    self.c.create_line(150, 300, 50, 400)
                    self.place[6] = 'x'
                    #self.agag = 0
                self.hod = False
                self.hod_place.append(6)

                self.proverochka()
                mm = str(6) + str(self.place[6]) + str(self.hod) + str(self.rez)
                print(mm)
                self.sock.send(mm.encode())
            else:
                pass
        elif event.x > 150 and event.y > 300 and event.x < 250:
            for i in self.hod_place:
                if i == 7:
                    return
            if self.hod:
                self.c.delete(self.fef[7])
                #self.c.create_oval(150, 300, 250, 400)
                if self.agag == 0:
                    self.c.create_oval(150, 300, 250, 400)
                    self.place[7] = 'o'
                    #self.agag = 1
                else:
                    self.c.create_line(150, 300, 250, 400)
                    self.c.create_line(250, 300, 150, 400)
                    self.place[7] = 'x'
                    #self.agag = 0
                self.hod = False
                self.hod_place.append(7)

                self.proverochka()
                mm = str(7) + str(self.place[7]) + str(self.hod) + str(self.rez)
                print(mm)
                self.sock.send(mm.encode())
            else:
                pass
        elif event.x > 250 and event.y > 200:
            for i in self.hod_place:
                if i == 8:
                    return
            if self.hod:
                self.c.delete(self.fef[8])
                #self.c.create_oval(250, 300, 350, 400)
                if self.agag == 0:
                    self.c.create_oval(250, 300, 350, 400)
                    self.place[8] = 'o'
                    #self.agag = 1
                else:
                    self.c.create_line(250, 300, 350, 400)
                    self.c.create_line(350, 300, 250, 400)
                    self.place[8] = 'x'
                    #self.agag = 0
                self.hod = False
                self.hod_place.append(8)
                
                self.proverochka()
                mm = str(8) + str(self.place[8]) + str(self.hod) + str(self.rez)
                print(mm)
                self.sock.send(mm.encode())
                
            else:
                pass

        #if not self.hod:
        #    n=0
        #    for i in self.place:
        #        if  i != '':
        #            mm = str(n) + str(i) + str(self.hod)
        #            print(mm)
        #            self.sock.send(mm.encode())
        #            #print(n,'qwii')
        #        n+=1

    def proverochka(self):
        if (self.place[0] == 'o' and self.place[1] == 'o' and self.place[2] == 'o') or (self.place[0] == 'o' and self.place[3] == 'o' and self.place[6] == 'o') or (self.place[3] == 'o' and self.place[4] == 'o' and self.place[5] == 'o') or (self.place[1] == 'o' and self.place[4] == 'o' and self.place[7] == 'o') or (self.place[6] == 'o' and self.place[7] == 'o' and self.place[8] == 'o') or (self.place[2] == 'o' and self.place[5] == 'o' and self.place[8] == 'o') or (self.place[0] == 'o' and self.place[4] == 'o' and self.place[8] == 'o') or (self.place[2] == 'o' and self.place[4] == 'o' and self.place[6] == 'o'):
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

                #self.sock.send('Gamover'.encode())
                self.rez = 'gamover'
            else:
                self.por+=1
                pp = 'Gameover: ' + str(self.por)
                self.l_por.configure(text=pp, font='Arial 24')
                #self.sock.send('Won'.encode())
                self.rez = 'won'   
                    
        elif (self.place[0] == 'x' and self.place[1] == 'x' and self.place[2] == 'x') or (self.place[0] == 'x' and self.place[3] == 'x' and self.place[6] == 'x') or (self.place[3] == 'x' and self.place[4] == 'x' and self.place[5] == 'x') or (self.place[1] == 'x' and self.place[4] == 'x' and self.place[7] == 'x') or (self.place[6] == 'x' and self.place[7] == 'x' and self.place[8] == 'x') or (self.place[2] == 'x' and self.place[5] == 'x' and self.place[8] == 'x') or (self.place[0] == 'x' and self.place[4] == 'x' and self.place[8] == 'x') or (self.place[2] == 'x' and self.place[4] == 'x' and self.place[6] == 'x'):
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

                #self.sock.send('Gameover'.encode())
                self.rez = 'gamover'
            else:
                self.por+=1
                pp = 'Gamover: ' + str(self.por)
                self.l_por.configure(text=pp, font='Arial 24')

                #self.sock.send('Won'.encode())
                self.rez = 'won'
                    
        elif (self.place[0] == 'o' or self.place[0] == 'x') and (self.place[1] == 'o' or self.place[1] == 'x') and (self.place[2] == 'o' or self.place[2] == 'x') and (self.place[3] == 'o' or self.place[3] == 'x') and (self.place[4] == 'o' or self.place[4] == 'x') and (self.place[5] == 'o' or self.place[5] == 'x') and (self.place[6] == 'o' or self.place[6] == 'x') and (self.place[7] == 'o' or self.place[7] == 'x') and (self.place[8] == 'o' or self.place[8] == 'x'):
            self.frame.destroy()
            self.l_won = Label(text='Ничья', font='Arial 24')
            self.l_won.pack()
            self.b_restart = Button(text="Ещё хочу", width=10, height=2)
            self.b_restart.config(command=self.restart)
            self.b_restart.pack()

            self.nich+=1
            nn = 'Nichya: ' + str(self.nich)
            self.l_nich.configure(text=nn, font='Arial 24')

            #self.sock.send('Nichya'.encode())
            self.rez = 'nichya'
        
    def connect(self):
        self.sock = socket.socket() #создание сокета
        self.sock.connect(('localhost', 9090))
        self.request()
    def request(self):
        #self.sock.send('Чо там с деньгами?'.encode())
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
                self.data = self.sock.recv(1024).decode()
                print(self.data)
                
                if 'won' in self.data:
                    self.frame.destroy()
                    self.l_won = Label(text='Выиграл O', font='Arial 24')
                    self.l_won.pack()
                    self.b_restart = Button(text="Ещё хочу", width=10, height=2)
                    self.b_restart.config(command=self.restart)
                    self.b_restart.pack()
                    
                    self.win+=1
                    ww = 'Won: ' + str(self.win)
                    self.l_win.configure(text=ww, font='Arial 24')
                    print('wwwwww')
                    continue
                
                elif 'gamover' in self.data:
                    self.frame.destroy()
                    self.l_won = Label(text='Выиграл X', font='Arial 24')
                    self.l_won.pack()
                    self.b_restart = Button(text="Ещё хочу", width=10, height=2)
                    self.b_restart.config(command=self.restart)
                    self.b_restart.pack()
                    
                    self.por+=1
                    pp = 'Gamover: ' + str(self.por)
                    self.l_por.configure(text=pp, font='Arial 24')
                    print('ppppppp')
                    continue
                
                elif 'nichya' in self.data:
                    self.frame.destroy()
                    self.l_won = Label(text='Ничья', font='Arial 24')
                    self.l_won.pack()
                    self.b_restart = Button(text="Ещё хочу", width=10, height=2)
                    self.b_restart.config(command=self.restart)
                    self.b_restart.pack()

                    self.nich+=1
                    nn = 'Nichya: ' + str(self.nich)
                    self.l_nich.configure(text=nn, font='Arial 24')
                    print('nnnnnnnn')
                    continue


                
                if 'start' in self.data:
                    if 'X' in self.data:
                        self.o_or_x = 1
                        self.agag = 1
                        self.hod = True
                    else:
                        self.o_or_x = 0
                        self.agag = 0
                        self.hod = False
                    self.play()
                elif 'o' in self.data or 'x' in self.data:
                    print('opaa')
                    n = self.data[0]
                    print(n)
                    self.place[int(n)] = self.data[1]
                    self.hod = self.data[2]
                    self.c.delete(self.fef[int(self.data[0])])
                    if self.data[1] == 'o':
                        for i in self.setka_o[int(self.data[0])]:
                            if self.setka_o[int(self.data[0])].index(i) == 0:
                                x1 = i
                            elif self.setka_o[int(self.data[0])].index(i) == 1:
                                y1 = i
                            elif self.setka_o[int(self.data[0])].index(i) == 2:
                                x2 = i
                            elif self.setka_o[int(self.data[0])].index(i) == 3:
                                y2 = i
                        self.c.create_oval(x1,y1,x2,y2)
                                              
                        self.place[int(self.data[0])] = 'o'
                        #self.agag = 1
                        
                    else:
                        #self.c.delete(self.fef[int(self.data[0])])
                        for i in self.setka_x[int(self.data[0])][0]:
                            if self.setka_x[int(self.data[0])][0].index(i) == 0:
                                x1 = i
                            elif self.setka_x[int(self.data[0])][0].index(i) == 1:
                                y1 = i
                            elif self.setka_x[int(self.data[0])][0].index(i) == 2:
                                x2 = i
                            elif self.setka_x[int(self.data[0])][0].index(i) == 3:
                                y2 = i
                        for i in self.setka_x[int(self.data[0])][1]:
                            if self.setka_x[int(self.data[0])][1].index(i) == 0:
                                x1_1 = i
                            elif self.setka_x[int(self.data[0])][1].index(i) == 1:
                                y1_1 = i
                            elif self.setka_x[int(self.data[0])][1].index(i) == 2:
                                x2_1 = i
                            elif self.setka_x[int(self.data[0])][1].index(i) == 3:
                                y2_1 = i
                        self.c.create_line(x1,y1,x2,y2)
                        self.c.create_line(x1_1,y1_1,x2_1,y2_1)
                        self.place[int(self.data[0])] = 'x'
                        #self.agag = ArithmeticError
                        

                else:
                    self.request()
            except (ConnectionResetError, ConnectionAbortedError):
                return
            
        #pass
        
    def play(self):
        #self.o_or_x = random.randint(0,1)
        #self.agag = self.o_or_x
        #print(self.o_or_x)
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
        self.place = ['','','','','','','','','']
        self.hod_place = []
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
        self.sock.close()
        self.root.destroy()
        sys.exit()

        
oleg = OXO()
