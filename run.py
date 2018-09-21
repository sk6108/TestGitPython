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
	p = os.system("cd /home/beehive/gitScripts/ | /opt/anaconda/bin/git pull")
	try:
   		p
   		print("done")
	except NameError:
   		print("This was not working... ")    
   		os.system('act -U db_superuser -w db_superuser -c "\\remove' + file_name + '"')
   		os.system('act -U db_superuser -w db_superuser -c "\install' + file_name + '"')


def main():
#### add input parameter
    file_name = get_input_data()
<<<<<<< Local Changes

    sys.
    try:
        print(get_files(file_name))
    except Exception as e:
        print (str(e))
=======

    get_files(file_name)
>>>>>>> External Changes

if __name__ == '__main__':
    main()


