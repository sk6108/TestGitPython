#!/opt/anaconda/bin/python3.6

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
    path = "/home/beehive/gitScripts/"
    os.system("cd /home/beehive/gitScripts/ && /opt/anaconda/bin/git pull")
    os.system('act -U db_superuser -w db_superuser -c "\\remove' + file_name + '"')
    os.system('act -U db_superuser -w db_superuser -c "\install' + path + file_name + '"')


def main():
#### add input parameter
    file_name = get_input_data()
    get_files(file_name)
    print("done")


if __name__ == '__main__':
    main()


