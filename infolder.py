# codeing utf-8
# This file for creat a folder named 'regulations' under current dir
# mave .pdf files in the folder first
#

from os import *                 # for dir and file oprate
from shutil import *             # for move files
foldername="Regulation"
if path.exists( foldername)==False:
    mkdir(foldername)

curenntpath=getcwd()
filelist=listdir(curenntpath)
for filename in filelist:
    if path.splitext(filename)[1] == '.pdf':
        if path.exists(foldername+'/'+filename): # if already in new folder
            remove(foldername+'/'+filename)
            move(curenntpath + "/" + filename, foldername)
        else:
            move(curenntpath + "/" + filename,foldername)

chdir(curenntpath+'/'+foldername)
subdirpath = getcwd()
regulationlist=listdir(subdirpath)
#print regulationlist[-1]
for regulation in regulationlist:
    subfoldername=regulation[:4].lower()
    if path.exists(subfoldername) == False:
        mkdir(subfoldername)
    move(subdirpath + "/" + regulation, subfoldername)






