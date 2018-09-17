#!/opt/anaconda/bin/python

import re
import sys
#import git 
import os



def get_input_data():   

#### using of input parameters
    while True:
        line = sys.stdin.readline()

#### break on EOF
        if line == "":
            break
        line = line.rstrip()
        input_par = line.split(';') 
        return input_par[0]

def get_files(file_name):    
p = os.system("cd /home/beehive/gitScripts/ | git pull")
try:
   p
   print("done"
except NameError:
   print("This was not working... ")    


def main():
#### add input parameter
    file_name = get_input_data()
    print(file_name)
    try:
        print(get_files(file_name))
    except Exception as e:
        print (str(e))

if __name__ == '__main__':
    main()


