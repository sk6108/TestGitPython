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
	os.system("cd /home/beehive/gitScripts/ | /opt/anaconda/bin/git pull")
	if os.path.exists(file_name):
		remove = 'act -U db_superuser -w db_superuser -c "\remove ' + file_name + '"'
  		os.system(remove)
		install = 'act -U db_superuser -w db_superuser -c "\install ' + file_name + '"' 
        	os.system(install)
   		print("done")
	else:
   		print("This was not working... ")    

def main():
#### add input parameter
    file_name = get_input_data()

    get_files(file_name)

if __name__ == '__main__':
    main()


