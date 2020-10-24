#!/usr/bin/env python
# coding: utf-8

# In[12]:


def Inches_Centimeters_converter(i):
    c = i * 2.54
    print (i, "inches converts to", c, "centimeters.")
def Kilograms_Pounds_converter(k):
    p = k * 2.205
    print (k, "kilograms converts to", p, "pounds.")
def Fahrenheit_Celcius_converter(f):
    c = (32 * f - 32) * 5/9
    print (f, "degrees Fahrenheit converts to", c, "degrees Celcius.")

type = input("Which converter do you want to use?")
t = type.lower()
if (t == "inches to centimeters"):
    i = input("How many inches do you want to convert to centimeters?")
    i = int(i)
    Inches_Centimeters_converter(i)
elif (t == "kilograms to pounds"):
    k = input("How many kilograms do you want to convert to pounds?")
    k = int(k)
    Kilograms_Pounds_converter(k)
elif (t == "fahrneheit to celcius"):
    f = input("How many degrees Fahrenheit do you want to convert to degrees Celcius")
    f = int(f)
    Fahrenheit_Celcius_converter(f)
    


# In[ ]:




