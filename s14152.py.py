################### window


from tkinter import*
window=Tk()
window.title('CS 1011 CAL')
window.geometry('450x170')


 


#   Entry widget

e=Entry(window, width='40',font=('bold','14'))
e.place(anchor= NW)
e.insert(INSERT,'Enter your expression here')
e.grid(row=0,columnspan=4,sticky=W+E)




    # buttons for numbers
def p1(num):
    s=e.get()
    if (s.find('+')+1== s.rfind('0') and s.find('0')!= 0 )or (s.find('-')+1== s.rfind('0') and s.find('0')!= 0 ) or (s.find('/')+1== s.rfind('0') and s.find('0')!= 0 ) or (s.find('*')+1== s.rfind('0') and s.find('0')!= 0 ):
        e.delete(s.find('+')+1 or s.find('-')+1 or s.find('/')+1 or s.find('*')+1 )
        e.insert(INSERT,num)
    elif s==str(0) or s == ('Enter your expression here'):
        e.delete(0,END)
        e.insert(INSERT,num)

        
    else: 
        e.insert(INSERT,num)
        
        
            
#buttons for operators
def p2(op):
    s=e.get()
    if s == ('Enter your expression here'):
        e.delete(0,END)
        e.insert(INSERT,op)
    else:
     
        e.insert(INSERT,op)
    


    #clear button(14)
def disappear():
    e.delete(0,END)
    

    
    
#b15 equal sign doing calculations and returning the expected results.
def p3():
    try:
        
            result=float(eval((e.get()).replace(',','')))
                
            
            
    except ZeroDivisionError:
            e.delete(0,END)
            e.insert(INSERT,'Can\'t divide by zero')
    
        
    except SyntaxError :
            e.delete(0,END)
            e.insert(INSERT,'Invalid input')

            
    except  NameError:
            e.delete(0,END)
            e.insert(INSERT,'undefined')
    
    
            
            
    except TypeError:
            e.delete(0,END)
            e.insert(INSERT,'Unsupported')

    
            
    else:
            e.delete(0,END)
            if result!=int(result):
                e.insert(INSERT,format(result,','))
    
            else:
                e.insert(INSERT,format(int(result),','))
                        
def p4():
    s=e.get()
    if s==str(0) or s == ('Enter your expression here') :
        e.delete(0,END)
        e.insert(INSERT,'0')
        
    
    else:
        e.insert(INSERT,'0')
    
            
                

### ################  buttons
b1=Button(window,text='1',width='9',command=lambda :p1('1'),font=12)
b1.grid(row=2,column=0)
b2=Button(window,text='2',width='9',command=lambda :p1('2'),font=12)
b2.grid(row=2,column=1)
b3=Button(window,text='3',width='9',command=lambda :p1('3'),font=12)
b3.grid(row=2,column=2)
b4=Button(window,text='+',width='9',command=lambda :p2('+'),font=12)
b4.grid(row=2,column=3)
b5=Button(window,text='4',width='9',command=lambda :p1('4'),font=12)
b5.grid(row=3,column=0)
b6=Button(window,text='5',width='9',command=lambda :p1('5'),font=12)
b6.grid(row=3,column=1)
b7=Button(window,text='6',width='9',command=lambda :p1('6'),font=12)
b7.grid(row=3,column=2)
b8=Button(window,text='-',width='9',command=lambda :p2('-'),font=12)
b8.grid(row=3,column=3)
b9=Button(window,text='7',width='9',command=lambda :p1('7'),font=12)
b9.grid(row=4,column=0)
b10=Button(window,text='8',width='9',command=lambda :p1('8'),font=12)
b10.grid(row=4,column=1)
b11=Button(window,text='9',width='9',command=lambda :p1('9'),font=12)
b11.grid(row=4,column=2)
b12=Button(window,text='*',width='9',command=lambda :p2('*'),font=12)
b12.grid(row=4,column=3)
b13=Button(window,text='0',width='9',command=p4,font=12)
b13.grid(row=5,column=0)
b14=Button(window,text='Clear',width='9',command=disappear,font=12)
b14.grid(row=5,column=1)
b15=Button(window,text='=',width='9',command=p3,font=12)
b15.grid(row=5,column=2)
b16=Button(window,text='/',width='9',command=lambda :p2('/'),font=12)
b16.grid(row=5,column=3)
window.mainloop()

