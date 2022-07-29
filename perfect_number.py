# Python program to check Perfect Number

# Function to check perfect number
def is_perfect(num):
    """

    :param num:
    :return:
    """
    perfect_sum = 0

    for i in range(1, num):
        if num % i == 0:
            perfect_sum += i

    # Function call & Decision
    if perfect_sum == num:
        print('%d is PERFECT' % (num))
    else:
        print('%d is NOT PERFECT' % (num))


if __name__ == "__main__":
    try:
        integer = int(input(" Number: "))
        is_perfect(integer)
    except Exception as ex:
        print(ex)