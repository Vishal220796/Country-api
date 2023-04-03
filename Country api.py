from tkinter import *
import requests
import json

root=Tk()


root.geomatry("350x350")
root.configure(background="light slate blue")

city_name_label=Label(root, text="Capital City Name",font=("Helvettica", 18,'bold'),bg="lime green", fg="white")
city_name_label.place(relx=0.35,rely=0.15,anchor=CENTER)

city_entry=Entry(root)
city_entry.place(relx=0.24,rely=0.25,anchor=CENTER)

country_name= Label(root,text="Country:", bg="maroon",fg="white", font=("Helvettica",10,"bold"))
country_name.place(relx=0.06,rely=0.45,anchor=W)

reigon = Label(root,text="Reigon:", bg="navy", fg="white", font=("Helvettica",10,"bold"))
reigon.place(relx=0.06,rely=0.55,anchor=W)

language = Label(root,text="Language:", bg="teal", fg="white", font=("Helvettica",10,"bold"))
language.place(relx=0.06,rely=0.65,rely=0.65, anchor=W)

population= Label(root,text="Population:", bg="red", fg="white", font=("Helvettica",10,"bold"))
population.place(relx=0.06,rely=0.75,anchor=W)

area = Label(root,text="Area:",bg="orange", fg="white", font=("Helvettica",10,"bold"))
area.place(relx=0.6,rely=0.85,anchor=W)              
