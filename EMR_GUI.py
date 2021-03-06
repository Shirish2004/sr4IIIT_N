import PySimpleGUI as sg
import pandas as pd
import openpyxl
import speech_recognition as sr
r=sr.Recognizer()
sg.theme("Dark")
File='EMR_File.xlsx'
df=pd.read_excel(File)
layout = [
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('Patient Name', size=(100,2)), sg.InputText(key='Name')],
    [sg.Text('Date', size=(100,2)), sg.InputText(key='Date')],
    [sg.Text('Patient Id', size=(100,2)), sg.InputText(key='Patient Id')],
    [sg.Text('Medical Record Id', size=(100,2)), sg.InputText(key='Medical Record Id')],
    [sg.Text('Doctors Name', size=(100,2)), sg.InputText(key='Doctors Name')],
    [sg.Text('Symptoms', size=(100,2)), sg.InputText(key='Symptoms')],
    [sg.Text('Diagnosis', size=(100,2)), sg.InputText(key='Diagnosis')],
    [sg.Text('Test Suggested', size=(100,2)), sg.InputText(key='Test Suggested')],
    [sg.Text('Next Appointment Date', size=(100,2)), sg.InputText(key='Next Appointment Date')],
    [sg.Submit(), sg.ReadButton('Clear'), sg.ReadButton('Name'),sg.ReadButton('Date'),sg.ReadButton('PID'),sg.ReadButton('MRID'),sg.ReadButton('Doctor'),sg.ReadButton('Symptoms'),sg.ReadButton('Diagnosis'),sg.ReadButton('Next'),sg.ReadButton('Test'),sg.Exit()]
]

window = sg.Window('Speech Recognition EMR', layout)

def clear_input():
    for key in values:
        window[key]('')
    return None

with sr.Microphone() as source:
    while True:
        r.adjust_for_ambient_noise(source)
        event, values = window.read()
        # print (f"Will listen for {event} with {r.energy_threshold}")
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Clear':
            clear_input()
        if event == 'Name0':
            # print(f"Sample rate: {source.SAMPLE_RATE}, format : {source.format}")
            audio_text = r.listen(source,5)
            try:
                value0=r.recognize_google(audio_text,language='en-US')
            except:
                value0="Sorry, Couldn't write"
            window['Name'].update(value0)
        if event=='Date1':
            audio_text = r.listen(source,5)
            try:
                value1=r.recognize_google(audio_text,language='en-US')
            except:
                value1="Sorry, Couldn't write"
            window['Date'].update(value1)
        if event =='PID':
            audio_text = r.listen(source,5)
            try:
                value2=r.recognize_google(audio_text,language='en-US')
            except:
                value2="Sorry, Couldn't write"
            window['Patient Id'].update(value2)
        if event =='MRID':
            audio_text=r.listen(source,5)
            try:
                value3=r.recognize_google(audio_text,language='en-US')
            except:
                value3="Sorry, Couldn't write"
            window['Medical Record Id'].update(value3)
        if event=='Doctor':
            audio_text = r.listen(source,5)
            try:
                value4=r.recognize_google(audio_text,language='en-US')
            except:
                value4="Sorry, Couldn't write"
            window['Doctors Name'].update(value4)
        if event =='Symptoms2':
            audio_text = r.listen(source,5)
            try:
               value5=r.recognize_google(audio_text,language='en-US')
            except:
               value5="Sorry, Couldn't write"
            window['Symptoms'].update(value5)
        if event =='Diagnosis3':
                audio_text = r.listen(source,5)
                try:
                    value6=r.recognize_google(audio_text,language='en-US')
                except:
                    value6="Sorry, Couldn't write"
                window['Diagnosis'].update(value6)
        if event =='Test':
                audio_text = r.listen(source,5)
                try:
                    value7=r.recognize_google(audio_text,language='en-US')
                except:
                    value7="Sorry, Couldn't write"
                window['Test Suggested'].update(value7)
        if event =='Next':
                audio_text = r.listen(source,5)
                try:
                    value8=r.recognize_google(audio_text,language='en-US')
                except:
                    value8="Sorry, Couldn't write"
                window['Next Appointment Date'].update(value8)
        if event == 'Submit':
            df = df.append(values, ignore_index=True)
            df.to_excel('EMR_File.xlsx', index=False)
            sg.popup('Data saved!')
            clear_input()

window.close()
