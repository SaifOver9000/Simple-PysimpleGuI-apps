import pySimpleGui  as sg

layout = [ #here the layout represents rows
    [sg.Text('Text')],
    [sg.Button('Button')],
    [sg.Input()]
]
sg.Window('Converter',layout) #this .Window is used to to just create a window.
         #we establish the title|a string| and the layout 


