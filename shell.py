from genericpath import exists, isfile
import os
from os import path
import shutil
from shutil import make_archive
from unittest import result
from zipfile import ZipFile

def archs():
    if path.exists("newfile.txt"):
        src = path.realpath("newfile.txt");
        dst = src + ".bak";
        shutil.copy(src, dst);
        #os.rename("textfile.txt", "newfile.txt")
        root_dir, tail = path.split(src);
        if not path.exists("archive.zip"):
            shutil.make_archive("archive", "zip", root_dir);
    
    with ZipFile("testzip.zip", "w") as newzip:
        newzip.write("newfile.txt");
        newzip.write("textfile.txt.bak");

def prstat():
    totalbytes = 0;
    dirlist = os.listdir();
    for entry in dirlist:
        if os.path.isfile(entry):
            filesize = os.path.getsize(entry);
            totalbytes += filesize;
    os.mkdir("results");

    resultsfile = open("results/results.txt", "w+");
    if resultsfile.mode == "w+":
        resultsfile.write("Total bytecount: " + str(totalbytes) + "\n");
        resultsfile.write("Files list:\n");
        resultsfile.write("---------------\n");
        for entry in dirlist:
            if os.path.isfile(entry):
                resultsfile.write(entry + "\n");
        resultsfile.close();

def main():
    prstat();

if __name__ == "__main__":
    main()