from asyncio.windows_events import NULL
import customtkinter
from tkinter import *

class mainwindow:
    def __init__(self):
        self.windo = Tk()
        self.x = ""
        self.the_first_number = 0
        self.the_second_number= 0
        self.windo.geometry("500x600")
        self.windo.configure(bg="white")
        self.windo.resizable(0,0)
    def run(self):
        self.windo.mainloop()
    
    
    def display(self):
        self.texxt = StringVar()
        self.texxt.set("")
        self.the_result_text = customtkinter.CTkLabel(height=100,width=500,text="0",fg_color="white",corner_radius=8,text_color="white",text_font=("Arial",20))
        self.the_result_text.grid(columnspan=3)
        self.button = customtkinter.CTkButton(text_font=("Arial",30),width=160,height=100,text="1",command= lambda: self.trying("1"),fg_color="white",hover_color="#574F4D").grid(row=1,column=0)
        
        self.button = customtkinter.CTkButton(text_font=("Arial",30),width=160,height=100,text="2",command= lambda: self.trying("2"),fg_color="white",hover_color="#574F4D").grid(row=1,column=1)
        self.button = customtkinter.CTkButton(text_font=("Arial",30),width=160,height=100,text="3",command= lambda: self.trying("3"),fg_color="white",hover_color="#574F4D").grid(row=1,column=2)
        self.button = customtkinter.CTkButton(text_font=("Arial",30),width=160,height=100,text="4",command= lambda: self.trying("4"),fg_color="white",hover_color="#574F4D").grid(row=2,column=0)
        self.button = customtkinter.CTkButton(text_font=("Arial",30),width=160,height=100,text="5",command= lambda: self.trying("5"),fg_color="white",hover_color="#574F4D").grid(row=2,column=1)
        self.button = customtkinter.CTkButton(text_font=("Arial",30),width=160,height=100,text="6",command= lambda: self.trying("6"),fg_color="white",hover_color="#574F4D").grid(row=2,column=2)
        self.button = customtkinter.CTkButton(text_font=("Arial",30),width=160,height=100,text="7",command= lambda: self.trying("7"),fg_color="white",hover_color="#574F4D").grid(row=3,column=0)
        self.button = customtkinter.CTkButton(text_font=("Arial",30),width=160,height=100,text="8",command= lambda: self.trying("8"),fg_color="white",hover_color="#574F4D").grid(row=3,column=1)
        self.button = customtkinter.CTkButton(text_font=("Arial",30),width=160,height=100,text="9",command= lambda: self.trying("9"),fg_color="white",hover_color="#574F4D").grid(row=3,column=2)
        self.button = customtkinter.CTkButton(text_font=("Arial",30),width=160,height=100,text="0",command= lambda: self.trying("0"),fg_color="white",hover_color="#574F4D").grid(row=4,column=0)
        self.button = customtkinter.CTkButton(text_font=("Arial",30),width=160,height=100,text="+",command= lambda: self.trying("+"),fg_color="white",hover_color="#574F4D").grid(row=4,column=1)
        self.button = customtkinter.CTkButton(text_font=("Arial",30),width=160,height=100,text="-",command= lambda: self.trying("-"),fg_color="white",hover_color="#574F4D").grid(row=4,column=2)
        self.button = customtkinter.CTkButton(text_font=("Arial",30),width=160,height=100,text="*",command= lambda: self.trying("*"),fg_color="white",hover_color="#574F4D").grid(row=5,column=0)
        self.button = customtkinter.CTkButton(text_font=("Arial",30),width=160,height=100,text="/",command= lambda: self.trying("/"),fg_color="white",hover_color="#574F4D").grid(row=5,column=1)
        self.button = customtkinter.CTkButton(text_font=("Arial",30),width=160,height=100,text="=",command= lambda: self.trying("="),fg_color="white",hover_color="#574F4D").grid(row=5,column=2)
        self.button = customtkinter.CTkButton(master=self.windo,text_font=("Arial",30),width=160,height=100,text="C",command= lambda: self.trying("C"),fg_color="white",hover_color="#574F4D").grid(row=0,column=2)



    def trying(self, text):
        
        self.text = text
        if(self.text == "C"):
            self.x=""
            self.the_first_number = 0 
            self.the_second_number = 0 
            self.the_result = 0

        elif(self.text == "+"):
            self.sine = "+"
            if(self.x == "" and self.the_first_number == 0):
                print("it is empty")
            else:
                self.the_first_number = float(self.x)
                self.x = ""
                

        
        elif(self.text == "-"):
            self.sine = "-"
            if(self.x == "" and self.the_first_number == 0):
                print("it is empty")
            else:
                self.the_first_number = float(self.x)
                self.x = ""


        
        elif(self.text == "*"):
            self.sine = "*"
            if(self.x == "" and self.the_first_number == 0):
                print("it is empty")
            else:
                self.the_first_number = float(self.x)
                self.x = ""

        
        elif(self.text == "/"):
            self.sine = "/"
            if(self.x == "" and self.the_first_number == 0):
                print("it is empty")
            else:
                self.the_first_number = float(self.x)
                self.x = ""


        elif(self.text=="="):
            if(self.sine==""):
                NULL
            elif(self.sine == "+"):
                if(self.x == ""):
                    self.the_second_number = 0
                else:
                    self.the_second_number = int(self.x)
                    self.the_result = self.the_first_number + self.the_second_number
                    self.the_first_number = self.the_result
                    self.x=str(round(self.the_result,3))
                    self.sine = ""


            elif(self.sine == "-"):
                if(self.x == ""):
                    self.the_second_number = 0
                else:
                    self.the_second_number = int(self.x)
                    self.the_result = self.the_first_number - self.the_second_number
                    self.the_first_number = self.the_result
                    self.x=str(round(self.the_result,3))
                    self.sine = ""

            elif(self.sine == "*"):
                if(self.x == ""):
                    self.the_second_number = 0
                else:
                    self.the_second_number = int(self.x)
                    self.the_result = self.the_first_number * self.the_second_number
                    self.the_first_number = self.the_result
                    self.x=str(round(self.the_result,3))
                    self.sine = ""

            elif(self.sine == "/"):
                if(self.x == ""):
                    print("it is empty")
                    self.the_second_number = 0
                elif(self.x == "0"):
                    self.x="N/A press C"

                else:
                    self.the_second_number = int(self.x)
                    print(self.the_second_number)
                    if(self.the_second_number!=0):
                        self.the_result = self.the_first_number / self.the_second_number
                        self.the_first_number = self.the_result
                        self.x=str(round(self.the_result,3))
                        self.sine = ""



            

        else:
            self.x = self.x + self.text
        self.the_result_text.config(text=self.x)    


root = mainwindow()
root.display()
root.run()