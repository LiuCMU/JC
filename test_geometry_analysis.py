'''
Tests for geometry analyis functions
'''

import geom_analysis as ga
import pytest

def test_calculate_distance(): #make sure the test function start with test_
    coord1 = [0,  0, 0]
    coord2 = [1, 0, 0]
    
    expected = 1.0 
    oberved = ga.calculate_distance(coord1, coord2)
    
    assert oberved == expected #if this statement is not true, then it will not pass the test
    
def test_bond_check():
    distance = 1
    minimum = 0
    maximum = 1.5
    
    expected = True
    oberved = ga.bond_check(distance, minimum, maximum)
    assert oberved == expected

#checking the edge cases for a variable
def test_bond_check_0():
    distance = 0
    
    expected = False
    oberved = ga.bond_check(distance)
    assert oberved == expected
    
def test_bond_check_1_5():
    distance = 1.5
    
    expected = True
    oberved = ga.bond_check(distance)
    assert oberved == expected
    
# check negative bond distances when the code will raise an error
def test_bond_check_negative():
    distance = -1
    expected = False
    with pytest.raises(ValueError):
        oberved = ga.bond_check(distance)