#Excersice: Rewrite invalid_image so that the body is a single line return <expression>, i.e. no if statement. 
# It should pass the same tests.

def invalid_image(filename):
    return not filename.endswith(".png") and not filename.endswith(".jpg")
    
    # if filename.endswith(".png") or filename.endswith(".jpg"):
    #     return False
    # else:
    #     return True

assert_equal(invalid_image("dog.png"), False)
assert_equal(invalid_image("cat.jpg"), False)
assert_equal(invalid_image("invoice.pdf"), True)


#Alternative Lösungen
# def invalid_image(filename):
#     return not (filename.endswith(".png") or filename.endswith(".jpg"))

# def invalid_image(filename):
#     return not filename.endswith(".png") and not filename.endswith(".jpg")