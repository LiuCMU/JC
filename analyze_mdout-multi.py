'''
This is the file to extrat total energy from mdout files. 
'''

import os
import argparse
import glob
import matplotlib.pyplot as plt


def ExtracInfo(result, data):
    '''
    result is the path where the output is stored;
    data is a list containing all lines of the orginal input file.
    '''
    with open(result, 'w+') as f_write:
        values = []
        for line in data:
            split_line = line.split()
            if 'Etot' in line:
                f_write.write(f'{split_line[2]} \n')
                values.append(split_line[2])
    return values

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
    parser.add_argument('--make_plots', help='flag to decide if a plot of the energies will be plotted')
    args = parser.parse_args()
    
    filenames = glob.glob(args.mdout_file_path)
    print(filenames)
    for file in filenames:
        fname = os.path.basename(file).split('.')[0]
        data = ReadData(file)
        values = ExtracInfo(f'{fname}.txt', data)
        print(f'File {fname}.txt has been generated from {file}')
        
        if args.make_plots:
            plt.figure()
            plt.plot(values)
            plt.savefig(f'{fname}.png')
            print(f'{fname}.png has been generated from {file}')