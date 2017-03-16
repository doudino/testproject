#!/usr/bin/env python

def repeat(x,callback):
    for _ in range(x):
        callback()
        
def greetings():
    print ("bonjour python2 et python3")

def gnouu():
    pass
    
if __name__ == "__main__":
    repeat(3,greetings)
