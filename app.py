#!/usr/bin/env python

def repeat(x,callback):
    """bzzz bzzz !!"""
    for _ in range(x):
        callback()
        
def greetings():
    """gnag ganan gna gnagna"""

    print ("bonjour le fork!")


def gnouu():
    pass
    
if __name__ == "__main__":
    repeat(3,greetings)
