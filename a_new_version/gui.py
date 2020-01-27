import tkinter

''''
#create a loop 
top = tkinter.Tk(className='cyber')

#create the label
label = tkinter.Label(top)
label['text'] = "僕のプログラムへようこそ"
label.pack()

#create the buttons
button = tkinter.Button(top)
button['text'] = 'submit'
button.pack()

#let the button can do something
def on_it():
    label['text'] = '???'
    pass
button['command'] =  on_it
button.pack()
#create new string 
text = tkinter.StringVar()
text.set('what do you want to do')
entry = tkinter.Entry(top)
entry['textvariable'] = text
entry.pack()

top.mainloop()

'''
top = tkinter.Tk()
Spinbox = tkinter.Spinbox(top)