#!/usr/bin/python3
# Write a function that divides element by element 2 lists.


def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(list_length):
        try:
           a =  my_list_1[i] / my_list_2[i]
        except(ValueError, TypeError):
            a = 0
            print("wrong type")
        except(ZeroDivisionError):
            a = 0
            print("division by 0")
        except(IndexError):
            a = 0
            print("out of range")
        finally:
            new.append(a)
    return(new)
