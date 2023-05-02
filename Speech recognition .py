#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import speech_recognition as sr
import pyjokes
import pyttsx3
import webbrowser
import tkinter as tk
import wikipedia
engine = pyttsx3.init()
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
#female voice id
# Use female voice 
engine.setProperty('voice', voice_id) 

#some pre defined chats

greetings=["hello","hi","hey"]
wish={"morning":"Good morning","night":"Good night","care":"You too.","bye":"Please don't go"}
silly={"marry":"No, i have a boyfriend and i only date robots","love":"I love myself","hate":"lmao, look at your face ","children":"Oh please."}



# In[4]:



import tkinter as tk
root=tk.Tk()
root.geometry("1000x300")
root.title("Summer")
root.configure(bg="black")
e1=tk.Text(root)
l1=tk.Label(root,text="Output:")
l1.place(x=10,y=5)
e1.place(x=10,y=35,height=50,width=180)
e2=tk.Text(root)
l=tk.Label(root,text="-----------------------------------")
l.place(x=10,y=90)
l=tk.Label(root,text="You said:")
l.place(x=10,y=120)
e2.place(x=10,y=150,height=30,width=180)
b1=tk.Button(root,text="Speak",bg="red",fg="white",)
b1.place(x=50,y=200,height=50,width=100)

root.mainloop()


# In[2]:


import speech_recognition as sr
import pyjokes
import pyttsx3
import webbrowser
import tkinter as tk
import wikipedia
engine = pyttsx3.init()
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
#female voice id
# Use female voice 
engine.setProperty('voice', voice_id) 

#some pre defined chats

greetings=["hello","hi","hey"]
wish={"morning":"Good morning","night":"Good night","care":"You too.","bye":"Please don't go"}
silly={"marry":"No, i have a boyfriend and i only date robots","love":"I love myself","hate":"lmao, look at your face ","children":"Oh please."}

def check(): #defining function
        
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)  #listening audio
        order=r.recognize_google(audio,language="en-in") #recognizing the audio
    e2.insert(tk.END,order)  #insert in textarea
    global x
    x=order.split(' ')  #tokenizing the sentence
    
    #[do ,you ,have ,children] 
    
    for word in x:
        if word in greetings:   #creating random logic
            answer="Hey, My name is Edu. Nice to meet you."
            
        elif word in wish:
            answer=wish[word]
            engine.say(answer)
            engine.runAndWait()
            e1.insert(tk.END, answer)
            
            
        elif "joke" in x:
            nj=pyjokes.get_joke()
            engine.say(nj)
            engine.runAndWait()
            e1.insert(tk.END, nj)
  
            try:
                order=order.replace("who","")
        
            except:
                order=order.replace("what","")
            answer=wikipedia.summary(order,sentences=1)
            engine.say(answer)
            engine.runAndWait()
            e1.insert(tk.END, answer)
            break

            
elif word in silly:
            answer=silly[word]
            engine.say(answer)
            engine.runAndWait()
            e1.insert(tk.END, answer)
            
elif "quit" in x:
            root.destroy()
import tkinter as tk
root=tk.Tk()
root.geometry("200x300")
root.title("Neha")
root.configure(bg="black")
e1=tk.Text(root)
l1=tk.Label(root,text="Output:")
l1.place(x=10,y=5)
e1.place(x=10,y=35,height=50,width=180)
e2=tk.Text(root)
l=tk.Label(root,text="-----------------------------------")
l.place(x=10,y=90)
l=tk.Label(root,text="You said:")
l.place(x=10,y=120)
e2.place(x=10,y=150,height=30,width=180)
b1=tk.Button(root,text="Speak",bg="red",fg="white",)
b1.place(x=50,y=200,height=50,width=100)

root.mainloop()
            


# In[9]:


pip install SpeechRecognition


# In[ ]:




