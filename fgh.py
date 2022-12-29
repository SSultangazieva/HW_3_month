# def chek_chetnoe(num):
#     if type(num) != int:
#         return print(None)
#     elif num % 2 == 0:
#         return print(True)
#     elif num % 2 != 0:
#         return print(False)

def chek_chetnoe(num):
    return print(num % 2 == 0 if type(num) == int else None)

chek_chetnoe(4)
chek_chetnoe(5)
chek_chetnoe(3.2)


