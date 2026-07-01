#Excersice: Write a function named is_valid_percentage, accepting one numerical argument x. 
# It should return True if x is between 0 and 100 (inclusive), and return False otherwise.


def is_valid_percentage(x):
    if x < 0 or x > 100:
        return False
    else:
        return True
 
assert_equal(is_valid_percentage(-1), False)
assert_equal(is_valid_percentage(0), True)
assert_equal(is_valid_percentage(50), True)
assert_equal(is_valid_percentage(100), True)
assert_equal(is_valid_percentage(101), False)