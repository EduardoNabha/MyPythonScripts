#This script is completely autoral made by myself while learning how to use the tkinter libraby. @EduardoNabha, 24/08/2022.

import tkinter as tk

#Constants

COLOR_PRUSSIAN_BLUE = '#003249'
COLOR_ALICE_BLUE = '#E1EFF6'
COLOR_LIGHT_SKY_BLUE = '#97D2FB'
COLOR_FRENCH_SKY_BLUE = '#83BCFF' 

FONT_CONSOLAS_BIG = ('Consolas',18,'bold')
FONT_CONSOLAS_MEDIUM = ('Consolas', 16)

class Calculadora:
    def __init__(self):
        self.mainScreen = tk.Tk()
        self.mainScreen.title(f'Made by @EduardoNabha')
        self.mainScreen.geometry("445x448")
        self.mainScreen.resizable(0,0)
        self.equation = ''
        self.numbers =['0','1','2','3','4','5','6','7','8','9']
        self.operators=['*','/','+','-']
        #Calling Visual Elements
        self.createFrameDisplay()
        self.createDisplay()
        self.createNumberButtons()
        self.createOperatorButtons()
        self.createOpenAndCloseButtons()
        self.createClearButton()
        self.createDotButton()
        self.createResultButton()
    def addToEquation(self,char):
        self.equation += str(char)
        self.display.delete(1.0, 'end')
        self.display.insert(1.0,self.equation)

    def resolveEquation(self):
        try:
            self.equation = str(eval(self.equation))
            self.display.delete(1.0,'end')
            self.display.insert(1.0,self.equation)
        except:
            self.clearEquation()
            self.display.insert(1.0, 'Unknow Error')

    def clearEquation(self):
        self.equation = ''
        self.display.delete(1.0,'end')
    #Visual Elements

    def createFrameDisplay(self):
        self.frame = tk.Label(self.mainScreen, bg=COLOR_PRUSSIAN_BLUE, bd=4)
        self.frame.grid(row=0,column=0,columnspan=4,sticky=tk.NSEW)

    def createDisplay(self):
        self.display = tk.Text(self.frame, height=3, width=33, font=FONT_CONSOLAS_BIG)
        self.display.grid(sticky=tk.NSEW)
    
    def createNumberButtons(self):
        for x in range(len(self.numbers)):
            button = tk.Button(self.mainScreen, text=x, command=lambda value=x: self.addToEquation(value), height=2, width=2, background=COLOR_ALICE_BLUE, fg= COLOR_PRUSSIAN_BLUE, activebackground=COLOR_LIGHT_SKY_BLUE, highlightcolor=COLOR_LIGHT_SKY_BLUE, relief='solid',borderwidth=1, font=FONT_CONSOLAS_MEDIUM)
            if (x > 0 and x <4):
                button.grid(row=3, column=int(self.numbers[x-1]), sticky=tk.NSEW)            
            if (x > 3 and x < 7):
                button.grid(row=2, column=int(self.numbers[x-4]), sticky=tk.NSEW)                
            if (x > 6 and x < 10):
                button.grid(row=1, column=int(self.numbers[x-7]), sticky=tk.NSEW) 
            if (x == 0):
                button.grid(row=4, column=1, sticky=tk.NSEW)
        
    def createOperatorButtons(self):
        for x in range(len(self.operators)):
            button = tk.Button(self.mainScreen, text=self.operators[x],command=lambda value=self.operators[x]: self.addToEquation(value), height=2, width=2, background=COLOR_ALICE_BLUE, fg= COLOR_PRUSSIAN_BLUE, activebackground=COLOR_LIGHT_SKY_BLUE, highlightcolor=COLOR_LIGHT_SKY_BLUE, relief='solid',borderwidth=1, font=FONT_CONSOLAS_MEDIUM )
            button.grid(row=x+1,column=3, sticky=tk.NSEW)

    def createOpenAndCloseButtons(self):
        opButton = tk.Button(self.mainScreen,text='(', command=lambda:self.addToEquation('('), height=2, width=2, background=COLOR_ALICE_BLUE, fg= COLOR_PRUSSIAN_BLUE, activebackground=COLOR_LIGHT_SKY_BLUE, highlightcolor=COLOR_LIGHT_SKY_BLUE, relief='solid',borderwidth=1, font=FONT_CONSOLAS_MEDIUM)
        opButton.grid(row=4, column=0,sticky=tk.NSEW)
        clButton = tk.Button(self.mainScreen,text=')', command=lambda:self.addToEquation(')'), height=2, width=2, background=COLOR_ALICE_BLUE, fg= COLOR_PRUSSIAN_BLUE, activebackground=COLOR_LIGHT_SKY_BLUE, highlightcolor=COLOR_LIGHT_SKY_BLUE, relief='solid',borderwidth=1, font=FONT_CONSOLAS_MEDIUM)
        clButton.grid(row=4, column=2,sticky=tk.NSEW)
    
    def createClearButton(self):
        clear = tk.Button(self.mainScreen, text='C', command= lambda: self.clearEquation(), height=2, width=2, background=COLOR_ALICE_BLUE, fg= COLOR_PRUSSIAN_BLUE, activebackground=COLOR_LIGHT_SKY_BLUE, highlightcolor=COLOR_LIGHT_SKY_BLUE, relief='solid',borderwidth=1, font=FONT_CONSOLAS_MEDIUM)
        clear.grid(row=5,column=0,sticky=tk.NSEW)

    def createDotButton(self):
        dot = tk.Button(self.mainScreen, text='.', command= lambda: self.addToEquation('.'), height=2, width=2, background=COLOR_ALICE_BLUE, fg= COLOR_PRUSSIAN_BLUE, activebackground=COLOR_LIGHT_SKY_BLUE, highlightcolor=COLOR_LIGHT_SKY_BLUE, relief='solid',borderwidth=1, font=FONT_CONSOLAS_MEDIUM)
        dot.grid(row=5,column=1,sticky=tk.NSEW)
    
    def createResultButton(self):
        result = tk.Button(self.mainScreen, text='=', command= lambda: self.resolveEquation(), height=2, width=2, background=COLOR_FRENCH_SKY_BLUE, fg= COLOR_PRUSSIAN_BLUE, activebackground=COLOR_LIGHT_SKY_BLUE, highlightcolor=COLOR_LIGHT_SKY_BLUE, relief='solid',borderwidth=1, font=FONT_CONSOLAS_BIG)
        result.grid(row=5,column=2, columnspan=2, sticky=tk.NSEW)
    def run(self):
        self.mainScreen.mainloop()



#Aplication

if __name__=='__main__':
    calculator = Calculadora()
    calculator.run()
