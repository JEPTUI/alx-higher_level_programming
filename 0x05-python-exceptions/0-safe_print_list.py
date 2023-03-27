#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_printed = 0
    while num_printed < x:
        try:
            print("{}".format(my_list[num_printed]), end="")
        except IndexError:
            break
        num_printed += 1
    print("")

    return num_printed
