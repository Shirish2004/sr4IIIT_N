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
    [sg.Text('Patient Name', size=(20,2)), sg.InputText(key='Name')],
    [sg.Text('Date', size=(30,1)), sg.InputText(key='Date')],
    [sg.Text('Patient Id', size=(15,1)), sg.InputText(key='Patient Id')],
    [sg.Text('Medical Record Id', size=(20,1)), sg.InputText(key='Medical Record Id')],
    [sg.Text('Doctors Name', size=(30,2)), sg.InputText(key='Doctors Name')],
    [sg.Text('Symptoms', size=(100,2)), sg.InputText(key='Symptoms')],
    [sg.Text('Diagnosis', size=(100,2)), sg.InputText(key='Diagnosis')],
    [sg.Text('Test Suggested', size=(100,2)), sg.InputText(key='Test Suggested')],
    [sg.Text('Next Appointment Date', size=(15,1)), sg.InputText(key='Next Appointment Date')],
    [sg.Submit(), sg.ReadButton('Clear'), sg.ReadButton('Name'),sg.ReadButton('Date'),sg.ReadButton('PID'),sg.ReadButton('MRID'),sg.ReadButton('Doctor'),sg.ReadButton('Symptoms'),sg.ReadButton('Diagnosis'),sg.ReadButton('Next'),sg.ReadButton('Test'),sg.Exit()]
]

window = sg.Window('Speech Recognition EMR', layout)

def clear_input():
    for key in values:
        window[key]('')
    return None


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Name':
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print (f"Will listen for {event} at {source.SAMPLE_RATE} with {r.energy_threshold}")
            audio_text = r.listen(source,5)
        try:
            value0=r.recognize_google(audio_text,language='en-US')
        except:
            value0="Sorry, Couldn't write"
        window['Patient Name'].update(value0)
    if event=='Date':
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print (f"Will listen for {event} at {source.SAMPLE_RATE} with {r.energy_threshold}")
            audio_text = r.listen(source,5)
            try:
                value1=r.recognize_google(audio_text,language='en-US')
            except:
                value1="Sorry, Couldn't write"
            window['Date'].update(value1)
    if event =='PID':
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio_text = r.listen(source,5)
            print (f"Will listen for {event} at {source.SAMPLE_RATE} with {r.energy_threshold}")
            try:
                value2=r.recognize_google(audio_text,language='en-US')
            except:
                value2="Sorry, Couldn't write"
            window['Patient Id'].update(value2)
    if event =='MRID':    
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print (f"Will listen for {event} at {source.SAMPLE_RATE} with {r.energy_threshold}")
            audio_text=r.listen(source,5)
            try:
                value3=r.recognize_google(audio_text,language='en-US')
            except:
                value3="Sorry, Couldn't write"
            window['Medical Record Id'].update(value3)
    if event=='Doctor':      
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print (f"Will listen for {event} at {source.SAMPLE_RATE} with {r.energy_threshold}")
            audio_text = r.listen(source,5)
            try:
                value4=r.recognize_google(audio_text,language='en-US')
            except:
                value4="Sorry, Couldn't write"
            window['Doctors Name'].update(value4)
    if event =='Symptoms':
        with sr.Microphone() as source:
             r.adjust_for_ambient_noise(source)
             print (f"Will listen for {event} at {source.SAMPLE_RATE} with {r.energy_threshold}")
             audio_text = r.listen(source,5)
             try:
                value5=r.recognize_google(audio_text,language='en-US')
             except:
                value5="Sorry, Couldn't write"
             window['Symptoms'].update(value5)
    if event =='Diagnosis':
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print (f"Will listen for {event} at {source.SAMPLE_RATE} with {r.energy_threshold}")
            audio_text = r.listen(source,5)
            try:
                value6=r.recognize_google(audio_text,language='en-US')
            except:
                value6="Sorry, Couldn't write"
            window['Diagnosis'].update(value6)
    if event =='Test':
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio_text = r.listen(source,5)
            print (f"Will listen for {event} at {source.SAMPLE_RATE} with {r.energy_threshold}")
            try:
                value7=r.recognize_google(audio_text,language='en-US')
            except:
                value7="Sorry, Couldn't write"
            window['Test Suggested'].update(value7)
    if event =='Next':
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print (f"Will listen for {event} at {source.SAMPLE_RATE} with {r.energy_threshold}")
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