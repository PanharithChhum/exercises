#checks that a string only contains unique characters by 
#creating an array with extended ASCII length and hashing
#characters to their ASCII index and incrementing their frequency


ASCII = 256

def unique_string_checker(string):
    arr = [0] * ASCII
    for char in string:
        arr[ord(char)] += 1
        if arr[ord(char)] > 1:
            return False
    return True

string = "abcdefg"

print unique_string_checker(string)

