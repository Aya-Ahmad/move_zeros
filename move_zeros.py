"""
This function takes a list of numbers 
and moves all zeros to the end of the list while maintaining the order of the other elements.
"""
def move_zeros( numbers ):
#to store the zero elements
    zero_array = []
#to store non-zero elements
    num_array = []
#loop is needed to separate zeros from non-zeros
    for i in range (len(numbers)):
        if numbers[i] == 0:
            zero_array.append(numbers[i])
        else:
            num_array.append(numbers[i])
#moving the zeros to the end of the list
    numbers = num_array + zero_array
    return numbers

numbers = []
size = int (input("How many elements do you want in your array? "))
#if condition needed here to validate the input
if size<=0:
    print("Give me a positive number for your array -- no zeros or negatives!")
else:
    for i in range ( size ):
        values = int (input("Let's fill this array! Type in your numbers: "))
        numbers.append( values )
    move_zeros_array = move_zeros( numbers )
    print ("Zeros, you're being sent to the end of the list! ",move_zeros_array)
    