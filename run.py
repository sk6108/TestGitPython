#!/opt/anaconda/bin/python

import re
import sys
import git 


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
    g = git.cmd.Git('.')
    g.pull()


def main():
#### add input parameter
    file_name = get_input_data()
    print(file_name)
    try:
        get_files(file_name)
    except Exception as e:
        print (str(e))

if __name__ == '__main__':
    main()


