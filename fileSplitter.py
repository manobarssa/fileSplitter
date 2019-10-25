# -*- coding: utf-8 -*-
"""
version 0.3

@author: @manobarssa
"""
#!python3

import argparse, os

def splitter(path, chunk):    
    with open(path,'rb') as f:
        fb = f.read(chunk)
        count = 0
        basename = os.path.basename(path)
        os.mkdir(basename+'_SPLITED')
        os.chdir(basename+'_SPLITED')
        while len(fb) > 0:
            if count < 10:
                cname = '0' + str(count)
            else:
                cname = str(count)            
            with open(basename+'_part_' + cname, 'wb') as rsz:
                rsz.write(fb)
            fb = f.read(chunk)
            count+=1
        os.chdir('..')
        return print('File parts written to {} folder.'.format(basename+'_SPLITED'))

def joiner(files):
    fn = files[0]
    filename = fn.replace(fn[fn.index('_part'):],'')
    with open(filename,'wb') as jf:
        for f in files:
            with open(f,'rb') as pf:
                bobj = pf.read()        
            jf.write(bobj)
    return print('Files joined to {} file.'.format(filename))
    
def main():
    parser = argparse.ArgumentParser(description= ''' 
    Split a file into n parts or join n parts into a file.''')
    
    #General arguments    
    parser.add_argument('-f', dest='file', metavar='File Path', type=str, 
                        help='Path to file that will be splited.')
    parser.add_argument('mode', metavar='MODE', type=str,
                        help='split or join')
        
    #Chunk or n group arguments
    chorn = parser.add_mutually_exclusive_group()
    chorn.add_argument('-c', dest='chunk', metavar='Chunk Size', type=int,
                       help='Chunk size in bytes.')
    chorn.add_argument('-n', dest='nparts', metavar='n_parts', type=int,
                       help='Number of parts in which the file will be splited.')
    
    
    
            
    args = parser.parse_args()
    #Defines the chunk size
    if args.chunk is not None:
        chunk = args.chunk
    elif args.nparts is not None:
        n = args.nparts
        file_size = os.path.getsize(args.file)
        chunkInt = file_size//n
        chunkDec = (file_size/n) - (chunkInt)
        if chunkDec == 0:
            chunk = chunkInt
        else:
            chunk = chunkInt + 1        
    
    #Splits the file    
    if args.mode.lower() == 'split':
        path = args.file        
        splitter(path,chunk)
    else:
        files = [x for x in os.listdir() if os.path.isfile(x)]
        joiner(files)

        
if __name__ == '__main__':
    main()    



    
    
        
        
    
    