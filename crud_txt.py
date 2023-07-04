
'''
Created on : July 04, 2023

@author: Hasan 

source:
    https://onecompiler.com/tutorials/python/working-with-files/crud-with-files
'''

import os



# create 
def create_file(filename):
    file = open(filename,"w")

# read 
def read_file(filename):
    file = open(filename,"r")
    print(file.read())

# update 
def update_file(filename):
    file = open(filename,"a")
    file.write("Happy learning!!")
    file.close()

# delete 
def delete_file(filename):
    os.remove(filename)

def startpy():
    # create_file("test.txt")
    # read_file("test.txt")
    # update_file("test.txt")
    delete_file("test.txt")
    # print("Tact101")
    
if __name__ == '__main__':
    startpy()