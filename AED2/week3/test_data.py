import pytest

def twoNumberSum(array, targetSum):
  """
  Description:
  A function that take in a non-empty array of distinct integers
  and an integer representing a target sum. If any two numbers 
  in the input array sum up to the target sum, the function should
  return then in an array, in any order. 
  If no two numbers sum up to the target sum, 
  the function should return an empty array.

  Parameters:
  array <list>: list of integers
  targetSum <integer>: integer representing a target sum

  Return:
  Interger pair which sum is equal to targetSum
  empty otherwise
  """
  # Old Solution
  """
  for i in range(len(array) - 1):
    firstNum = array[i]
    for j in range (i+1, len(array)):
      secondNum = array[j]
      if firstNum + secondNum == targetSum:
        return [firstNum, secondNum]
  return []
  """
  solution = {}
  for value in array:
    second_value = targetSum - value
    if (second_value not in solution):
        solution[value] = True
    else:
        return [second_value ,value]
  return []  

@pytest.fixture(scope="session")
def data():
    
    array = []
    
    # test 1 data
    array.append([3, 5, -4, 8, 11, 1, -1, 6])

    # test 2 data
    array.append([4, 6, 1, -3])

    # test 3 data
    array.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 15])

    # test 4 data
    array.append([15])

    # test 5 data
    array.append([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47])

    # test 6 data
    array.append([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47])

    # test 7 data
    array.append([-7, -5, -3, -1, 0, 1, 3, 5, 7])
    
    return array

def test_1(data):
    """
    Test evaluation for [3, 5, -4, 8, 11, 1, -1, 6] and target 10
    """
    assert twoNumberSum(data[0],10) == [11,-1]


def test_2(data):
    """
    Test evaluation for [4, 6, 1, -3] and target 3
    """
    assert twoNumberSum(data[1],3) == [6,-3]

def test_3(data):
    """
    Test evaluation for [1, 2, 3, 4, 5, 6, 7, 8, 9, 15] and target 26
    """
    assert twoNumberSum(data[2],26) == []

def test_4(data):
    """
    Test evaluation for [15] and target 15
    """
    assert twoNumberSum(data[3],15) == []

def test_5(data):
    """
    Test evaluation for [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47] and target 164
    """
    assert twoNumberSum(data[4],164) == [] 

def test_6(data):
    """
    Test evaluation for [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47] and target 163
    """
    assert twoNumberSum(data[5],163) == [210, -47] 

def test_7(data):
    """
    Test evaluation for [-7, -5, -3, -1, 0, 1, 3, 5, 7] and target -5
    """
    assert twoNumberSum(data[6],-5) == [-5, 0]
