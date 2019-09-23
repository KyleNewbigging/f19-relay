#!/usr/bin/env python3

import sys

def main(args):
    print("Hello world!")

    pos=(0,0)

    x=0

    up=(0,1)
    down=(0,-1)
    left=(1,0)
    right=(-1,0)
    dir=[up,left,down,right]

    for i in argv[1]:
        if (i=='L'):
            x+=1
        elif (i=='R'):
            x-=1
        if (x==4):
            x=0
        if (x==-1):
            x=3

        if (i!='O' and i!='L' and i!='R'):
            pos+=dir


    return 0

if __name__ == "__main__":
    main(sys.argv)
