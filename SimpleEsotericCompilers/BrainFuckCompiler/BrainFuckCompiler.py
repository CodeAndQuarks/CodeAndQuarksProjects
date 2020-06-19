# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:20:35 2020

@author: CodeAndQuarks

Desc: This is a Brainfuck compiler/interpreter in Python3 because why not.
      It is a esoteric programming language created in 1993 by Urban Müller.
      It is Turing complete.
      Its memory system is tape-based.
      Esoteric programming languages as a rule ,
      are meant to be less for practical use and more for 'fun'.
      So enjoy compiling your .bf and .b files!
"""
#------------------------------------------------------------------------------
"""First. Lets determine out our 8 simple cmds for Brainfuck"""
#increment and decrement a cell on the tape
add, sub='+','-'
#move up or down the tape
increase, decrease='>','<'
#start and end a loop as long as we are not at 0
start, end='[',']'
#recieve input and return output
output,read='.',','
#-----------------------------------------------------------------------------
def commands(bf):
    """This will read the entire bf language"""
    global add, sub, increase, decrease, start, end, output, read
    print('\n This is your code in Brainfuck: \n', bf, '\n')
    a=list(bf)
    #memory
    mem = [0]
    #pointer for our tape of memory
    p= 0
    #read command @ r of a[]
    r = 0
    """For sake of argument,lets return ASCII+Output,and then a finalised printout"""
    ASCII_values=[]
    line=""
    print('\nOutput from tape...')
    while r < len(a):
        if a[r] == decrease:
            if p > 0:
                p -= 1
        elif a[r] == increase:
            p += 1
            if len(mem) <= p:
                mem.append(0)
        elif a[r] == add:
            mem[p] += 1
        elif a[r] == sub:
            if mem[p] > 0:
                mem[p] -= 1
        elif a[r] == output:
            #grab all of that output
            value=chr(mem[p])
            print(mem[p],' : ',value)
            ASCII_values.append(mem[p])
            line+=value
        elif a[r] == read:
            e = input("Enter:")
            try:
                o = int(e)
            except ValueError:
                o = ord(e)
            mem[p] = o
        # check for loops
        elif a[r] == start:
            if mem[p] == 0:
                loop_state = 1
                while loop_state > 0:
                    r += 1
                    if a[r] == start:
                        loop_state += 1
                    elif a[r] == end:
                        loop_state-= 1
        elif a[r] == end:
            loop_state = 1
            while loop_state > 0:
                r -= 1
                if a[r] == start:
                   loop_state -= 1
                elif a[r] == end:
                   loop_state += 1
            r-=1               
        r += 1
    print('Sucessfully compiled!')
    return  print('\nThis is your output in ASCII:\n',ASCII_values,
                  '\nThis is your output as a readable string:\n' ,line)
#------------------------------------------------------------------------------
def compilebrainf():
    """Actually open and compile your .b or .bf file"""
    string=input('Please select the .b, .bf you wish to compile: ' )
    folder='brainfuck/'
    filename=folder+string
    """Check if .b or bf file even exists"""
    import os.path
    if os.path.exists(filename):
        # file exists  
        bf_file=open(filename,'r')
        data=""
        for lines in bf_file:
            data+=str(lines)
    
        return commands(data)
    else:
        print('This file type does not exist')      
#------------------------------------------------------------------------------       
"""Try calling HelloWorld.bf"""
compilebrainf()