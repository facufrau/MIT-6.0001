###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    if target_weight in memo:
        return memo[target_weight]
    elif target_weight == 0:
        return 0
    elif target_weight < 0:
        return None
    
    smallest = None
    for egg in egg_weights:
        new_weight = target_weight - egg
        new_result = dp_make_weight(egg_weights, new_weight, memo)
        if new_result != None:
            result = new_result + 1
            if smallest == None or result < smallest:
                smallest = result
    memo[target_weight] = smallest
    return smallest

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    # egg_weights = (2,3,5)
    # n = 8
    # print("Egg weights = (2,3,5)")
    # print("n = 8")
    # print("Expected ouput: 2 (3 * 1 + 5 * 1 = 8)")
    # print("Actual output:", dp_make_weight(egg_weights, n))
    # print()

    # egg_weights = (1, 5, 10, 25)
    # n = 99
    # print("Egg weights = (1, 5, 10, 25)")
    # print("n = 99")
    # print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    # print("Actual output:", dp_make_weight(egg_weights, n))
    # print()

    egg_weights = (1, 5, 10, 25)
    n = 100
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 100")
    print("Expected ouput: 4 (4 * 25 = 100)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()