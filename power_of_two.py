def power_of_two(pow):
    for i in range(0, pow+1):
        print(5 ** i)


if __name__ == "__main__":
    try:
            print(("Enter The Number: "))
            number = int(input())
            print(("Power of Two Numbers Are: "))
            power_of_two(number)
    except Exception as ex:
        print(ex)

# def is_power_of_two(number : int) -> bool:
#     while number != 1:
#         if number % 2:
#             return  False
#         number /= 2
#     return True
