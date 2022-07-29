# fibonacci_number
def fibonacci_series(num):
    """
    :param num:
    :return:
    """

    # check if input is 0 then it'll print incorrect input
    if num < 0:
        print("Incorrect input")

    # check if num is 0 then it'll return 0
    elif num == 0:
        return 0

    # check if num is 1,2 it'll return 1
    elif num == 1 or num == 2:
        return  1
    else:
        return fibonacci_series(num-1) + fibonacci_series(num-2)
    print(fibonacci_series(9))

if __name__ == "__main__":
    try:

        term = int(input("Enter how many fibonacci terms do you want :"))
        fibonacci_series(term)
    except Exception as ex:
        print(ex)


# # fibonacci series logic
# def fibonacci_series(nth_term):
#     """fibonacci series logic"""
#
#     first = 0
#     second = 1
#     next_number = first + second
#     if nth_term > 2:
#         print(first, second, end=" ")
#         for i in range(3, term + 1):
#             if i == term:
#                 print(next_number)
#             else:
#                 print(next_number, end=" ")
#                 first = second
#                 second = next_number
#                 next_number = first + second
#     else:
#         print("Entered integer is either negative or too small")
#
#
# if _name_ == "_main_":
#     print("Enter how many fibonacci terms do you want : ")
#     term = int(input())
#     fibonacci_series(term)