#!/usr/bin/env python
# coding: utf-8

# ###Python Turtle
# * Turtle Graphics

# In[2]:


#Step 1:Make all the turtle package to be imported
import turtle
#Turtle method creates and returns a new object
a1 = turtle.Turtle()
#forward() method moves 100 pixels
turtle.forward(100)
#We are done
turtle.done()


# In[ ]:


#Line drawing in reverse direction
import turtle as tt
a1 = tt.Turtle()
a1.backward(100)
tt.done


# In[ ]:


#Draw a square using Turtle
import turtle as tt
a1 = tt.Turtle()
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
tt.done()


# In[ ]:


#Draw square
import turtle as t
aa=turtle.Turtle()
aa.backward(150)
aa.left(90)
aa.backward(150)
aa.left(90)
aa.backward(150)
aa.left(90)
aa.backward(150)
aa.left(90)
t.done()


# In[2]:


#Loop statements
import turtle as t
aa=t.Turtle()
for i in range (4):
    aa.backward(150)
    aa.left(90)
t.done()


# In[3]:


#Loop statements
import turtle as t
aa=t.Turtle()
for i in range (4):
    aa.forward(150)
    aa.right(90)
t.done()


# In[ ]:


#Simple star
import turtle as t 
a1=t.Turtle()
for i in range (40):
    a1.forward(50)
    a1.right(144)
t.done()


# In[ ]:


#spiraling Star
import turtle as t 
a1=t.Turtle()
a1.pencolor('blue')
for i in range (40):
    a1.forward(i*10)
    a1.right(144)
t.done
    


# In[8]:


#Suare spiral
import turtle as t
a1=t.Turtle()
a1.pencolor('Green')
for i in range (250):
    a1.forward(i)
    a1.left(91)
t.done()


# In[14]:


#Hexagon Spiral with multi colour
from turtle import *
colors=['green','blue','yellow','orange','violet','black']
for x in range(250):
    pencolor(colors[x%6])
    width(x/100+1)
    forward(x)
    left(59)
t.done    


# In[1]:


#go to function
from turtle import *
goto(50,50)
goto(-50,50)
goto(100,-50)
goto(-50,-50)


# In[16]:


# set heading (heading)
# will change the current direction to the heading angle
from turtle import *
colors=['green','blue','yellow','violet','orange','black']
for angle in range(0,360,15):
    pencolor(colors[angle%6])
    setheading(angle)
    forward(100)
    write (str(angle)+'o')
    backward(100)
t.done()


# In[14]:


import turtle as t
from turtle import *
pencolor('red')
for i in range (15):
    forward(100)
    left(90)
    forward(10)
    left(90)
    forward(100)
    right(90)
    forward(10)
    right(90)
pencolor('blue')
for i in range(90):
    undo()
t.done()


# In[1]:


#
from turtle import *
pensize(10)
pencolor('red')
forward(250)
pencolor(0,1.0,0)
forward(250)
pensize(10)
goto(-400,50)

for red in range(4):
    for green in range(4):
        for blue in range(4):
            pencolor(red/4.0,green/4.0,blue/4.0)
            forward(10)
#t.done()


# In[6]:


#Generate a Rectangle
import turtle as t
a1=t.Turtle()
a1.fillcolor('yellow')
a1.begin_fill()
for i in range(4):
    a1.forward(100)
    a1.right(90)
    a1.forward(50)
    a1.right(90)
t.done()


# In[11]:


import turtle
 
t = turtle.Turtle()
t.fillcolor('green')
t.begin_fill()
t.circle(100)
t.end_fill()


# In[12]:


#Python program to draw color filled square in turtle programming
import turtle
 
t = turtle.Turtle()
t.fillcolor('blue')
t.begin_fill()
for i in range(4):
  t.forward(150)
  t.right(90)
t.end_fill()


# In[ ]:


#generate the symbols
fron turtle import *
fillcolor('orange')
pensize(10)
pencolor('black')

