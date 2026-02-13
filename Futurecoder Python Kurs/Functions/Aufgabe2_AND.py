#Excersice: Rewrite this function using and instead.


def is_valid_percentage(x):
    if x >= 0 and x <= 100:
        return True
    else:
        return False

assert_equal(is_valid_percentage(-1), False)
assert_equal(is_valid_percentage(0), True)
assert_equal(is_valid_percentage(50), True)
assert_equal(is_valid_percentage(100), True)
assert_equal(is_valid_percentage(101), False)