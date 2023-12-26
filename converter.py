#This a tutorial app used to understang Python GUIs
import PySimpleGUI  as sg

layout = [[sg.Input(key = '-INPUT-'), 
           sg.Spin(['km to mile', 'kg to pound', 'sec to min'], key = '-UNITS-'), 
           sg.Button('Convert', key = '-CONVERT-')],
          [sg.Text('Output', key = "-OUTPUT-")]]#here the layout represents rows

window = sg.Window('Converter',layout) #this .Window is used to to just create a window.
         #we establish the title|a string| and the layout 


while True:
    event, values = window.read() # events are basically interactions with the systems, things that happpen to the system
    
    if event == sg.WIN_CLOSED: 
        break
    
    if event == '-CONVERT-':
        input_values = values['-INPUT-']
       # print(input_values)
        if input_values.isnumeric():
            match values['-UNITS-']:
                case 'km to mile':
                    output = round(float(input_values) * 0.6214, 2)
                    output_string = f'{input_values} km are {output} miles.'
                case 'kg to pound':
                    output = round(float(input_values) * 2.205, 2)
                    output_string = f'{input_values} kg are {output} pounds.'
                case 'sec to min':
                    output = round(float(input_values) / 60, 2)
                    output_string = f'{input_values} secs are {output} mins.'
            
            window['-OUTPUT-'].update(output_string)
        
        else:
            window['-OUTPUT-'].update('Please enter a number')
window.close()