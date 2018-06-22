import random
import string
import sys


def replytext(inp):
    lt = len(inp)
    response=[]
    for x in range(lt):
        if(inp[x].isalpha()):
            y=random.randint(0,50)
            if (y%2 is 0):
                response.append(inp[x].upper())
            else:
                response.append(inp[x].lower())
        else:
            response.append(inp[x])
    
    return response
