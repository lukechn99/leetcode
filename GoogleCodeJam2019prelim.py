# Someone just won the Code Jam lottery, and we owe them N jamcoins! 
# However, when we tried to print out an oversized check, we encountered a problem. 
# The value of N, which is an integer, includes at least one digit that is a 4... 
# and the 4 key on the keyboard of our oversized check printer is broken.

# Fortunately, we have a workaround: 
# we will send our winner two checks for positive integer amounts A and B, 
# such that neither A nor B contains any digit that is a 4, and A + B = N. 
# Please help us find any pair of values A and B that satisfy these conditions.

# replace_four will take an integer number and convert it into a list of
# digits in string representation. Strings are used so that there is no need to
# keep track of a digit's power, instead, string concatenationcan be used at the end
# A second list is constructed which stores 2's and 0's 
# leading 0's are later taken off
def replace_four (i: int):
    sum_a = list(str(i))
    sum_b = []
    for i in range(len(sum_a)):
        if sum_a[i] == "4":
            sum_a[i] = "2"
            sum_b.append("2")
        else:
            sum_b.append("0")
    str_a = ""
    str_b = ""
    for n in sum_a:
        str_a += n
    while sum_b[0] == "0":
        sum_b = sum_b[0:]
    for n in sum_b:
        str_b += n
    print(str(i) + ": " + str_a + " " + str_b)