#Excersice: Given a list of three elements, check if all three elements are equal.

def all_equal(row):
    if row[0] == row[1] and row[1] == row[2]:
        return True
    else:
        return False

assert_equal(all_equal(["X", "X", "X"]), True)
assert_equal(all_equal(["O", "O", "O"]), True)
assert_equal(all_equal(["X", "O", "X"]), False)

#ODER NOCH KÜRZER   return row[0] == row[1] == row[2]