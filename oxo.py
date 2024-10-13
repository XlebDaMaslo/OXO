# client.py
from tkinter import *
import socket
import threading

class OXO:
    def __init__(self):
        self.root = Tk()
        self.root.title("Tic-Tac-Toe")
        self.buttons = [[None] * 3 for _ in range(3)]  # 2D list to store button widgets
        self.board = [[''] * 3 for _ in range(3)]  # Represents the game board

        self.my_turn = False  # Initially not player's turn
        self.my_mark = ''     # X or O

        self.create_widgets()

        self.sock = socket.socket()
        try:  # Better error handling with try...except
            self.sock.connect(('localhost', 9090))
            self.receive_thread = threading.Thread(target=self.receive_data)
            self.receive_thread.daemon = True  # Allow the program to exit even if thread is active
            self.receive_thread.start()
        except OSError as e:
            print(f"Error connecting to server: {e}")
            self.root.destroy()
            return  # Important: Exit the client if the connection fails


    def create_widgets(self):
        # Grid of buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = Button(self.root, text="", width=10, height=5,
                                         command=lambda row=i, col=j: self.button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        # Message label to indicate wait status. Add widgets to the main window's grid 
        self.message_label = Label(self.root, text="")
        self.message_label.grid(row=3, column=0, columnspan=3)



    def button_click(self, row, col):
        if self.my_turn and self.board[row][col] == '':  # Only process valid moves 
            self.board[row][col] = self.my_mark  # Update own view before send
            self.buttons[row][col].config(text=self.my_mark, state=DISABLED)  # Reflect board change 
            self.send_move(row, col)
            self.my_turn = False



    def send_move(self, row, col):
         # Sending row, column and mark to easily rebuild server board 
        data = f"{row},{col},{self.my_mark}"
        self.sock.sendall(data.encode())

    def receive_data(self):

        while True:
            try:

                data = self.sock.recv(1024).decode()
                
                if data.startswith("start_"):
                    self.my_mark = data[6]
                    self.message_label.config(text=f"You are: {self.my_mark}")
                    if self.my_mark == 'X':
                         self.my_turn = True
                    

                elif data == 'wait':  # Make this check more robust
                    self.message_label.config(text="Waiting for another player...")

                elif "," in data: # Data comes as a string "row,col,mark". Example data would be a message like "0,2,x"
                    row, col, mark = data.split(",")  # Unpack info
                    self.board[int(row)][int(col)] = mark
                    self.buttons[int(row)][int(col)].config(text=mark, state=DISABLED) #Update GUI (Tkinter window buttons text and button) 
                    self.my_turn = True


                elif data in ['won', 'gamover', 'nichya']:
                     self.game_over(data) # Check if client.py already does this  

            except (ConnectionResetError, ConnectionAbortedError, OSError):

                print("Connection to the server was lost.")

                # Close the Tkinter window cleanly. Not sure where this code will live? Inside class outside class, main bit?
                # Try both of these, and in different places in client.py to ensure client does indeed shut down gracefully
                self.root.quit() # Option1
                self.root.destroy() # Option 2 (Safer in rare corner cases)
                return


    def game_over(self, result):
        if (result == 'won' and self.my_mark == 'O') or (result == 'gamover' and self.my_mark == 'X'): #Check if this is how your game client knows victory
            message = "You Won!"
        elif (result == 'won' and self.my_mark == 'X') or (result == 'gamover' and self.my_mark == 'O'):  # Correct this part, too
             message = "You Lost!"
        else:  # Correct conditions. This should also tell you about draw. Is that a draw according to how your server handles gamover or game finish situations??
            message = "Draw!"
        self.message_label.config(text=message)
        #Disable buttons for replay to occur through some mechanism you introduce later: 
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=DISABLED)


if __name__ == "__main__":
    oxo = OXO()
    oxo.root.mainloop()
