# https://www.youtube.com/watch?v=XAUzKhkBTFk
# How Does Python Process A Regular Expression? Part 2
# Bring in the library
#  that we need. 
import re
# Create a RegEx object
#  we can use later.
# Our pattern is a zip code
#  like nnnnn-nnnn,
#  The +4 is optional.
regEx = "[0-9]{5}(?:-[0-9]{4})?$"
p = re.compile(regEx)
my_zip = "12345-9876"
# Check against our string.
# It will match.
print(f"Checking {my_zip}")
result = p.search(my_zip)
print(f"result is of type {result}")
print(f"group(): {result.group()}")
print(f"start(): {result.start()}")
print(f"end(): {result.end()}")
print("----------------")
# Now let's try it with a
#  string that won't match.
# The result will be None.
my_str = "123" # too short
print(f"Checking {my_str}")
result = p.search(my_str)
print(f"result is of type {result}")
print("----------------")
# So, the easy way to check 
#  for a pattern match is 
#  to check for the result None.
# This will not match...
my_str = "ABCDE"
print(f"Checking {my_str}")
result = p.search(my_str) 
if result is not None:
    print("Pattern found")
    print(f"Starting at index {result.start()}")
else:
    print("Pattern NOT found")
print("----------------")
# Now try it with 5 digits
#  and the dash, but nothing
#  after that.
# Our pattern won't match.
my_zip = "12345-"
print(f"Checking {my_zip}")
result = p.search(my_zip) 
if result is not None:
    print("Pattern found")
    print(f"Starting at index {result.start()}")
else:
    print("Pattern NOT found")
