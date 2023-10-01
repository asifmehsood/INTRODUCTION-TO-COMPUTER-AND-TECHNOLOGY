import tkinter as tk
import requests



class mainwindow:
    def __init__(self):
        self.windo = tk.Tk()
        self.Clicked = tk.StringVar()
        self.Clicked2 = tk.StringVar()
        self.the_result = "0"
        self.windo.geometry("200x250")
        self.windo.resizable(0,0)
    def run(self):
        self.windo.mainloop()
    def display(self):

        self.to_Text = tk.Label(text="From",pady=10)
        self.to_Text.pack()
        self.Clicked.set("USD")
        self.drow_down = tk.OptionMenu(self.windo,self.Clicked,"PKR","YER","USD","SAR")
        self.drow_down.pack()

        self.to_Text = tk.Label(text="TO",pady=10)
        self.to_Text.pack()
        self.Clicked2.set("USD")
        self.drow_down2 = tk.OptionMenu(self.windo,self.Clicked2,"PKR","YER","USD","SAR")
        self.drow_down2.pack()

        self.enter_field = tk.Entry()
        self.enter_field.pack()
        self.enter_field.insert(tk.END , "0")

        #C
        button1 = tk.Button(text="CONVERT",command=self.conversion)
        button1.pack()

        # The result txt
        self.txe1 = tk.Label(text=self.the_result,pady=10)
        self.txe1.pack()
    def conversion(self):
        #those two lines take input from the menu about what currencey it will be converted to
        self.to1 = str(self.Clicked.get())
        self.to = self.to1

        #those two lines take input from the menu about what currencey it will be converted from
        self.from1 = str(self.Clicked2.get())
        self.from2 = self.from1

        #those lines requsts the API to bring the information as a JSON
        self.url = 'https://v6.exchangerate-api.com/v6/3930c785ed9538053f156b62/latest/' + self.to
        self.response = requests.get(self.url)
        self.data = self.response.json()
        self.exchange_rate = self.data['conversion_rates']

        #this line change the text on the screen that shows the result 
        self.txe1.config(text=str(round(int(self.enter_field.get())*self.exchange_rate[self.from2],4) ))    


root = mainwindow()
root.display()
root.run()
