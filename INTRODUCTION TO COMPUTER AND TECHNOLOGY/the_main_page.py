import tkinter as tk
import customtkinter
root = tk.Tk()
def tocalculator():
    root.destroy()
    import calculator
def toconverter():
    root.destroy()
    import currency_converter
def tobinery():
    root.destroy(ary)
def totemp():
    root.destroy()
    import Tem_calculator   
def togame():
    root.destroy()
    import the_game
root.configure(bg="black")
go_tocalculator = customtkinter.CTkButton(text_font=("Arial",20),width=160,height=100,text="calculator",fg_color="white",hover_color="#574F4D",command=tocalculator).pack()
go_tocorency = customtkinter.CTkButton(text_font=("Arial",20),width=160,height=100,text="Currency Converter",fg_color="white",hover_color="#574F4D",command=toconverter).pack()
go_tobine = customtkinter.CTkButton(text_font=("Arial",20),width=160,height=100,text="Number converter",fg_color="white",hover_color="#574F4D",command=tobinery).pack()
go_totemp = customtkinter.CTkButton(text_font=("Arial",20),width=160,height=100,text="temperature",fg_color="white",hover_color="#574F4D",command=totemp).pack()
go_togame = customtkinter.CTkButton(text_font=("Arial",20),width=160,height=100,text="Bing-Bong Game",fg_color="white",hover_color="#574F4D",command=togame).pack()

root.mainloop()

