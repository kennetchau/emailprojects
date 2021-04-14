#!/usr/bin/env python
# coding: utf-8

# In[1]:


# python 3
# email project, replace code with inputs


# In[2]:


# import module
from datetime import datetime, time, timedelta
import calendar
import PySimpleGUI as sg
import os
import pyperclip
import codecs


# In[3]:


# creating list for time 
allmachine = ["B",'C','D','E','G','I','J','K']
timeslot = []
starttime = datetime(1,1,1,9,30,0)
timeslot.append(starttime)


# In[4]:


# Using script to generate all timeslot required
for i in range(18):
    timeslot.append(timeslot[i]+timedelta(minutes=30))


# In[5]:


for i in range(len(timeslot)):
    timeslot[i] = timeslot[i].strftime("%H:%M")


# In[6]:


width = max(map(len, timeslot))+1


# In[7]:


#original text
text = """"""


# In[8]:


def swapdate(inputs): #changing string to datetime object
    datetime_object = datetime.strptime(inputs,'%b %d %Y')
    return datetime_object


# In[9]:


sg.theme('LightBrown1') #setting theme


# In[10]:


# creating a layout for the giu
layout = [
    [sg.Text('Email editor:')],
    [sg.Text('Choose a template'),sg.FileBrowse()],
    [sg.Text('Name:'),sg.InputText(key='name')],
    [sg.Text('email:'),sg.InputText(key='email')],
    [sg.Text('title:'),sg.InputText(key='title')],
    [sg.In(key='date',visible = False),sg.CalendarButton('Select date',target='date',format=('%b %d %Y'))],
    [sg.Text('Start time:'),sg.Combo(timeslot, size=(width, 5), key='startime')],
    [sg.Text('End time:'),sg.Combo(timeslot, size=(width, 5), key='endtime')],
    [sg.Text('room code:'),sg.Combo(allmachine, size=(width, 5), enable_events=False, key='machine')],
    [sg.Button('Generate')], [sg.Button('Close')]
]


# In[11]:


# creating the window
window = sg.Window('Email generator',layout)


# In[ ]:


# loop for giu
while True:
    event, values = window.read()
    Whatday = ""
    Day = ""
    if event == sg.WIN_CLOSED or event == "Close":
        break
    try:
        Whatday = calendar.day_name[swapdate(values['date']).weekday()]
        Day = swapdate(values['date']).strftime("%b %d")
    except:
        print("wrong format: please inputs as month date year")
        
    try:
        file = codecs.open(values['Browse'],'r',encoding = 'utf-8' )
        text = file.read()
        file.close()
    except:
        print("file read fail.")
        
    text = text.format(values['name'], values['email'], Day, Whatday, values['startime'],values["endtime"],values['machine'].upper(),values['title'])
    print(event,values)
    pyperclip.copy(text)
    print("successful")


# In[ ]:


window.close()


# In[ ]:





# In[ ]:




