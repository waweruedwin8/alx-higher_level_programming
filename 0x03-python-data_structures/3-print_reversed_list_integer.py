def print_reversed_list_integer(my_list=[]):
    for num in reversed(my_list):
        print("{}".format(num))


my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
