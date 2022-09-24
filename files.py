import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def filesop():
    myfile = open("textfile.txt", "w+");
    for i in range(10):
        myfile.write("This is some text\n");
    
    myfile.close();

    myfile = open("textfile.txt", "a+");
    for i in range(10):
        myfile.write("This is some new text\n");   
    myfile.close();

    myfile = open("textfile.txt","r");
    if myfile.mode == 'r':
        contents = myfile.read()
        print(contents); 
    myfile.close();

    myfile = open("textfile.txt","r");
    if myfile.mode == 'r':
        fl = myfile.readlines();
    for x in fl:
        print(x);

def oss():
    print(os.name);
    print("Item exists:", str(path.exists("textfile.txt")));
    print("Item is a file:", path.isfile("textfile.txt"));
    print("Item is a directory:", path.isdir("textfile.txt"));
    print("Item's path", path.realpath("textfile.txt"));
    print("Item's path and name: ", path.split(path.realpath("textfile.txt")));
    t = time.ctime(path.getmtime("textfile.txt"));
    print(t);
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")));
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"));
    print(td);
def main():
    oss();

if __name__ == "__main__":
    main()