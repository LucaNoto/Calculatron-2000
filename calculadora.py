# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 08:19:21 2016

@author: Lucanoto
"""

import tkinter as tk
#import tkinter.ttk as ttk

class Telas():
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.rowconfigure(0, minsize=600)
        self.root.columnconfigure(0, minsize=400)
        self.root.resizable(width=False, height=False)
        self.root.grid()
        self.algorism = 0
        
        self.simples_frame()
        
    def simples_frame(self):
        
        #Configurações do Frame
        self.simples = tk.Frame(self.root)
        
        self.simples.columnconfigure(0, minsize=100, weight=1)
        self.simples.columnconfigure(1, minsize=100, weight=1)
        self.simples.columnconfigure(2, minsize=100, weight=1)
        self.simples.columnconfigure(3, minsize=100, weight=1)

        self.simples.rowconfigure(0, minsize=100, weight=1)
        self.simples.rowconfigure(1, minsize=100, weight=1)
        self.simples.rowconfigure(2, minsize=100, weight=1)
        self.simples.rowconfigure(3, minsize=100, weight=1)
        self.simples.rowconfigure(4, minsize=100, weight=1)
        self.simples.rowconfigure(5, minsize=100, weight=1)
        


        self.simples.grid(row=0, column=0, sticky="nsew")
        
        self.visor = tk.Label(self.simples)
        self.visor.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.visor.configure (text= "0",font='Bodoni 70', fg='White', bg= 'Black')
        
        self.ac = tk.Label(self.simples)
        self.ac.grid(row=1, column=0, sticky="nsew")
        self.ac.configure(text= "AC",font='Bodoni 70', fg='Black')
        self.ac.bind('<1>',self.clicked_clear)
        
        mais_menos = tk.Label(self.simples)
        mais_menos.grid(row=1, column=1, sticky="nsew")
        mais_menos.configure(text= "+/-",font='Bodoni 70', fg='Black')
        mais_menos.bind('<1>',self.clicked_negate)

        percent = tk.Label(self.simples)
        percent.grid(row=1, column=2, sticky="nsew")
        percent.configure(text= "%",font='Bodoni 70', fg='Black')
        percent.bind('<1>',self.clicked_percent)

        divide = tk.Label(self.simples)
        divide.grid(row=1, column=3, sticky="nsew")
        divide.configure(text= "/",font='Bodoni 70', fg='Black', bg='Orange')
        divide.bind('<1>',self.clicked_divide)
        
#------------------------------

        seven = tk.Label(self.simples)
        seven.grid(row=2, column=0, sticky="nsew")
        seven.configure(text= "7",font='Bodoni 70', fg='Black')
        seven.bind('<1>',self.clicked_7)

        eight = tk.Label(self.simples)
        eight.grid(row=2, column=1, sticky="nsew")
        eight.configure(text= "8",font='Bodoni 70', fg='Black')
        eight.bind('<1>',self.clicked_8)

        nine = tk.Label(self.simples)
        nine.grid(row=2, column=2, sticky="nsew")
        nine.configure(text= "9",font='Bodoni 70', fg='Black')
        nine.bind('<1>',self.clicked_9)

        multiply = tk.Label(self.simples)
        multiply.grid(row=2, column=3, sticky="nsew")
        multiply.configure(text= "X",font='Bodoni 70', fg='Black', bg='Orange')
        multiply.bind('<1>',self.clicked_multiply)
        
#------------------------------

        four = tk.Label(self.simples)
        four.grid(row=3, column=0, sticky="nsew")
        four.configure(text= "4",font='Bodoni 70', fg='Black')
        four.bind('<1>',self.clicked_4)

        five = tk.Label(self.simples)
        five.grid(row=3, column=1, sticky="nsew")
        five.configure(text= "5",font='Bodoni 70', fg='Black')
        five.bind('<1>',self.clicked_5)

        six = tk.Label(self.simples)
        six.grid(row=3, column=2, sticky="nsew")
        six.configure(text= "6",font='Bodoni 70', fg='Black')
        six.bind('<1>',self.clicked_6)

        subtract = tk.Label(self.simples)
        subtract.grid(row=3, column=3, sticky="nsew")
        subtract.configure(text= "-",font='Bodoni 70', fg='Black', bg='Orange')
        subtract.bind('<1>',self.clicked_subtract)

#------------------------------

        one = tk.Label(self.simples)
        one.grid(row=4, column=0, sticky="nsew")
        one.configure(text= "1",font='Bodoni 70', fg='Black')
        one.bind('<1>',self.clicked_1)

        two = tk.Label(self.simples)
        two.grid(row=4, column=1, sticky="nsew")
        two.configure(text= "2",font='Bodoni 70', fg='Black')
        two.bind('<1>',self.clicked_2)

        three = tk.Label(self.simples)
        three.grid(row=4, column=2, sticky="nsew")
        three.configure(text= "3",font='Bodoni 70', fg='Black')
        three.bind('<1>',self.clicked_3)

        add = tk.Label(self.simples)
        add.grid(row=4, column=3, sticky="nsew")
        add.configure(text= "+",font='Bodoni 70', fg='Black', bg='Orange')
        add.bind('<1>',self.clicked_add)
#------------------------------

        zero = tk.Label(self.simples)
        zero.grid(row=5, column=0, columnspan=2, sticky="nsew")
        zero.configure(text= "0",font='Bodoni 70', fg='Black')
        zero.bind('<1>',self.clicked_0)

        dot = tk.Label(self.simples)
        dot.grid(row=5, column=2, sticky="nsew")
        dot.configure(text= ".",font='Bodoni 70', fg='Black')
        dot.bind('<1>',self.clicked_dot)

        self.equal = tk.Label(self.simples)
        self.equal.grid(row=5, column=3, sticky="nsew")
        self.equal.configure(text= "=",font='Bodoni 70', fg='Black', bg='Orange')
        self.equal.bind('<1>',self.clicked_equal)
        
    def clicked_0(self,event):
        self.algorism = (self.algorism * 10)
        self.visor.configure(text= self.algorism)
        
    def clicked_1(self,event):
        self.algorism = (self.algorism * 10) + 1
        self.visor.configure(text= self.algorism)
        
    def clicked_2(self,event):
        self.algorism = (self.algorism * 10) + 2
        self.visor.configure(text= self.algorism)

    def clicked_3(self,event):
        self.algorism = (self.algorism * 10) + 3 
        self.visor.configure(text= self.algorism)

    def clicked_4(self,event):
        self.algorism = (self.algorism * 10) + 4
        self.visor.configure(text= self.algorism)

    def clicked_5(self,event):
        self.algorism = (self.algorism * 10) + 5
        self.visor.configure(text= self.algorism)

    def clicked_6(self,event):
        self.algorism = (self.algorism * 10) + 6
        self.visor.configure(text= self.algorism)

    def clicked_7(self,event):
        self.algorism = (self.algorism * 10) + 7
        self.visor.configure(text= self.algorism)

    def clicked_8(self,event):
        self.algorism = (self.algorism * 10) + 8
        self.visor.configure(text= self.algorism)

    def clicked_9(self,event):
        self.algorism = (self.algorism * 10) + 9
        self.visor.configure(text= self.algorism)

    def clicked_dot(self,event):
        pass

#-------------------------------------

    def clicked_clear(self,event):
        self.algorism = 0
        self.visor.configure(text= self.algorism)
    
    def clicked_negate(self,event):
        self.algorism = self.algorism * (-1)
        self.visor.configure(text= self.algorism, font='Bodoni 70',fg='White')
        self.algorism = 0
        

    def clicked_percent(self,event):
        self.algorism = self.algorism/100
        self.visor.configure(text= self.algorism)
        self.algorism = 0

        
    def clicked_divide(self,event):
        pass
    def clicked_multiply(self,event):
        pass
    def clicked_subtract(self,event):
        pass
    def clicked_add(self,event):
        pass
    def clicked_equal(self,event):
        pass




        
    def start(self):
        self.root.mainloop()

Calculatron = Telas()
Calculatron.start()

