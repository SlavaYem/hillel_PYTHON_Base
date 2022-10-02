# def reverse_str_in_list(my_list_in_def):
#     for i, num in enumerate(my_list_in_def):
#         if i % 2:
#             new_list.append(num[::-1])
#         else:
#             new_list.append(num)
#     return new_list
#
#
# new_list = []
# my_list = ["qwe", "zxc", "ert", "tyu"]
# new_list = reverse_str_in_list(my_list)
# print(new_list)
###############################################################################
# def a_first_in_str_in_list(my_list_in_def):
#     for index in my_list_in_def:
#         if "a" == index[0]:
#             new_list.append(index)
#     return new_list
#
#
# my_list = ["abc", "dbc", "zxc"]
# new_list = []
# new_list = a_in_str_in_list(my_list)
# print(new_list)
###############################################################################
# def a_in_str_in_list(my_list_in_def):
#     for index in my_list_in_def:
#         if "a" in index:
#             new_list.append(index)
#     return new_list
#
#
# my_list = ["abc","dbc","zxc" ," d aa"]
# new_list = []
# new_list = a_in_str_in_list(my_list)
# print(new_list)
###############################################################################
# def str_not_int_in_list(my_list_in_def):
#     for index in range(len(my_list_in_def)):
#         if type(my_list_in_def[index]) == str:
#             my_new_list.append(my_list_in_def[index])
#     return my_new_list
#
# my_new_list = []
# my_list = [1, 2, 3, "11", "22", 33]
# my_new_list = str_not_int_in_list(my_list)
# print(my_new_list)
###############################################################################
# def symbols_alone_in_str(my_str_in_def):
#     my_list_in_def = [i for i in my_str if my_str.count(i) == 1]
#     return my_list_in_def
#
# my_str = " qweeeeee"
# my_list = symbols_alone_in_str(my_str)
# print(my_list)
###############################################################################
# def symbols_in_lists(my_str_1_in_def,my_str_2_in_def):
#     for i in my_str_1_in_def:
#         if i in my_str_2_in_def:
#             result.append(i)
#     return result
#
#
#
# my_str_1 = "qwe dfsfdsf e q "
# my_str_2 = "qwe  e  q"
# result = []
# my_result = symbols_in_lists(my_str_1,my_str_2)
# print(my_result)
###############################################################################
# def symbols_in_lists(my_str_1_in_def, my_str_2_in_def):
#     for i in my_str_1_in_def:
#         k = my_str_1_in_def.find(i) - my_str_1_in_def.rfind(i)
#         if k == 0:
#             if i in my_str_2_in_def and my_str_2_in_def.find(i) - my_str_2_in_def.rfind(i) == 0:
#                 result.append(i)
#     return result
#
#
# my_str_1 = "qwe dfsfdsf e q "
# my_str_2 = "qwe  e  q"
# result = []
# my_result = symbols_in_lists(my_str_1, my_str_2)
# print(my_result)
###############################################################################
# import random
# import string
#
#
# def create_email(names_in_def, domains_in_def):
#     number_random = random.randint(100, 1000)
#     number_random_str = str(number_random)
#     rand_string = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 7)))
#     my_str_1 = random.choice(names_in_def) + "." + number_random_str + "@" + rand_string + "." + random.choice(domains_in_def)
#     return my_str_1
#
#
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
#
# e_mail = create_email(names, domains)
# print(e_mail)


