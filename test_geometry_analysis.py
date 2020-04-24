'''
Tests for geometry analyis functions
'''

import geom_analysis as ga

def test_calculate_distance():
    coord1 = [0,  0, 0]
    coord2 = [1, 0, 0]
    
    expected = 1.0 
    oberved = ga.calculate_distance(coord1, coord2)
    
    assert oberved == expected
    
def test_bond_check():
    distance = 1
    minimum = 0
    maximum = 1.5
    
    expected = True
    oberved = ga.bond_check(distance, minimum, maximum)
    assert oberved == expected
    
def test_bond_check_0():
    bond_distance = 0
    expected = False
    observed = ga.bond_check(bond_distance)
    
    assert expected == observed
    
    
def test_bond_check_1p6():
    bond_distance = 1.6
    expected = False
    observed = ga.bond_check(bond_distance)
    
    assert expected == observed