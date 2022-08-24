#This script is completely autoral made by myself while learning how to use the tkinter libraby. @EduardoNabha, 24/08/2022.
#requisits: tkinter
import tkinter as tk

#Constants



class Calculadora:
    def __init__(self):
        self.mainScreen = tk.Tk()
        self.mainScreen.title(f'Made by @EduardoNabha')
        self.mainScreen.geometry("800x800")
        self.mainScreen.resizable(0,0)
        self.equation = ''
        self.numbers =['0','1','2','3','4','5','6','7','8','9']
        self.operators=['*','/','+','-']
        #Calling Visual Elements
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
    
    def createDisplay(self):
        self.display = tk.Text(self.mainScreen, height=6, width=2)
        self.display.grid(row=0,column=0, sticky=tk.NSEW, columnspan=4)
    
    def createNumberButtons(self):
        for x in range(len(self.numbers)):
            button = tk.Button(self.mainScreen, text=x, command=lambda value=x: self.    addToEquation(value), height=4, width=8)
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
            button = tk.Button(self.mainScreen, text=self.operators[x],command=lambda value=self.operators[x]: self.addToEquation(value), height=4, width=8 )
            button.grid(row=x+1,column=3, sticky=tk.NSEW)

    def createOpenAndCloseButtons(self):
        opButton = tk.Button(self.mainScreen,text='(', command=lambda:self.addToEquation('('), height=4, width=8)
        opButton.grid(row=4, column=0,sticky=tk.NSEW)
        clButton = tk.Button(self.mainScreen,text=')', command=lambda:self.addToEquation(')'), height=4, width=8)
        clButton.grid(row=4, column=2,sticky=tk.NSEW)
    
    def createClearButton(self):
        clear = tk.Button(self.mainScreen, text='C', command= lambda: self.clearEquation(), height=4, width=8)
        clear.grid(row=5,column=0,sticky=tk.NSEW)

    def createDotButton(self):
        dot = tk.Button(self.mainScreen, text='.', command= lambda: self.addToEquation('.'), height=4, width=8)
        dot.grid(row=5,column=1,sticky=tk.NSEW)
    
    def createResultButton(self):
        result = tk.Button(self.mainScreen, text='=', command= lambda: self.resolveEquation(), height=4, width=8)
        result.grid(row=5,column=2, columnspan=2, sticky=tk.NSEW)
    def run(self):
        self.mainScreen.mainloop()



#Aplication

if __name__=='__main__':
    calculator = Calculadora()
    calculator.run()
