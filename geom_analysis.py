'''
This module functions associated with analyzing the geometry of a molecule.

It can be run as as script with an xyz file

I add a mark here May 8th
'''


import numpy
import os
import argparse #enable command line data path

def open_xyz(file):
    xyz_file = numpy.genfromtxt(file, skip_header=2, dtype='unicode')
    symbols = xyz_file[:, 0]
    coordinates = xyz_file[:, 1:]
    coordinates = coordinates.astype(numpy.float)
    return symbols, coordinates
    

def calculate_distance(atom1_coord, atom2_coord):
    """
    Calculate the distance between two points in 3D space
    Inputs: coordinates of the two atoms
    Return: distance between the atoms
    """
    
    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    atom_distance = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return atom_distance
    
def bond_check(distance, minimum=0, maximum=1.5):
    if distance < 0:
        raise ValueError(f'Invalid atom distance {distance}. Distance cannot be less than 0!')
    if distance >minimum and distance<=maximum:
        return True
    else:
        return False



if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='The script analyzes a user given xyz file and out puts the length of the bonds.')
    parser.add_argument('xyz_file', help='The file path for the xyz file to analyze.')
    args = parser.parse_args() # collect all the args in the parser

    #file_location = os.path.join('data', 'water.xyz')
    xyzfilename = args.xyz_file # specif with args that I am going to use
    symbols, coordinates = open_xyz(xyzfilename)
    num_atoms = len(symbols)
    for num1 in range(0, num_atoms):
        for num2 in range(0, num_atoms):
            if num1<num2:
                atom_distance = calculate_distance(coordinates[num1], coordinates[num2])
                if bond_check(atom_distance, 0, 1.5) is True:
                    print(f'{symbols[num1]} to {symbols[num2]} : {atom_distance:.3f}')
                
# be sure to click save! Or no change will be saved.