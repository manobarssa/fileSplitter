# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 22:55:23 2019

@author: Anderson
"""
#!python3

import argparse, os

def splitter(path, chunk):    
    with open(path,'rb') as f:
        fb = f.read(chunk)
        count = 0    
        while len(fb) > 0:
            if str(count) < 10:
                cname = '0' + str(count)
            else:
                cname = str(count)
            basename = os.path.basename()
            with open(basename+'_part_' + cname, 'wb') as rsz:
                rsz.write(fb)
            fb = f.read(chunk)
            count+=1

def joiner():
    
    files = [x for x in os.listdir() if os.path.isfile(x)]
    filename = files[0].replace()
    with open(filename,'wb') as jf:
        for f in files:
            with open(f,'rb') as pf:
                bobj = pf.read()        
            jf.write(bobj)
    

        
    if '-n' in args_dict.keys():
        file_size = os.path.getsize(path)
        n = int(args_dict['-n'])
        blockInt = file_size//n
        blockDec = (file_size/n) - (blockInt)
        if blockDec == 0:
            block = blockInt
        else:
            block = blockInt + 1
        
        with open(path,'rb') as f:
            fb = f.read(block)
            count = 0    
            while len(fb) > 0:
                with open(basename+'_part_' + str(count), 'wb') as rsz:
                    rsz.write(fb)
                fb = f.read(block)
                count+=1
    
    print('Partitioned files has been written to {}'.format(os.getcwd()))