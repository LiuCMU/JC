'''
This is the file to extrat total energy from mdout files. 
'''

import os
import argparse
import glob


def ExtracInfo(result, data):
    '''
    result is the path where the output is stored;
    data is a list containing all lines of the orginal input file.
    '''
    with open(result, 'w+') as f_write:
        for line in data:
            split_line = line.split()
            if 'Etot' in line:
                f_write.write(f'{split_line[2]} \n')

def DeleteLst2(path):
    '''
    Result is the path of file, of which we want to delete the last two lines
    '''
    with open(path, 'r') as f_d:
        data = f_d.readlines()
    Tol = len(data)
    with open(path, 'w+') as f:
        for val in data:
            if data.index(val) < Tol-2:
                f.write(f'{val}')

def ReadData(path):
    f = open(path, 'r')
    data = f.readlines()
    f.close()
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This script extract the total energy from give mdout file')
    parser.add_argument('mdout_file_path', help='The path of mdout file')

    args = parser.parse_args()
    data = ReadData(args.mdout_file_path)
    ExtracInfo('Etot.txt', data)
    DeleteLst2('Etot.txt')