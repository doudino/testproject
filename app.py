#!/usr/bin/env python2

def repeat(x,callback):
    for _ in range(x):
        callback()
        
def greetings():
    print "bonjour"

if __name__ == "__main__":
    repeat(3,greetings)
