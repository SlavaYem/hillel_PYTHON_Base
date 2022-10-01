############################################################################################################################
# number = 123123400000434343000032
# new_number = str(nubmer)
# print(new_number.count('0'))
############################################################################################################################
# number = 10020000
# new_number = str(number)
# print(len(new_number) - len(new_number.rstrip('0')))
############################################################################################################################
# my_list_1 = [1, 2, 3, 4, 5]
# my_list_2 = [10, 9, 8, 7, 6]
# my_result = []
#
# for index in range(len(my_list_1)):
#     if index % 2 == 0:
#         my_result.append(my_list_1[index])
#
# for index in range(len(my_list_2)):
#     if index % 2 == 1:
#         my_result.append(my_list_2[index])
# print(my_result)
############################################################################################################################
# my_list = [1, 2, 3, 4]
# new_list = []
#
# new_list = my_list.copy()
# number = new_list.pop(0)
# new_list.append(number)
# print(new_list)
############################################################################################################################
# my_list = [1, 2, 3, 4]
# number = my_list.pop(0)
# my_list.append(number)
# print(my_list)
############################################################################################################################
# my_str = "43 больше чем 34 но меньше чем 56"
# my_str_list = my_str.split()
# counter = 0
#
# for item in my_str_list:
#     if item.isdigit():
#         counter += int(item)
#
# print(counter)
############################################################################################################################
# my_str = "My long string"
# l_limit = "o"
# r_limit = "g"
# sub_str = my_str[my_str.find(l_limit) + 1: my_str.rfind(r_limit)]
# print(sub_str)
############################################################################################################################
# my_str = "abcdffref"
# my_result = []
# for index in range(0, len(my_str), 2):
#     my_result.append(my_str[index: index + 2].ljust(2, '_'))
# print(my_result)
############################################################################################################################
# my_list = [2,4,1,5,3,9,0,7]
# counter = 0
# for index in range(1, len(my_list)-1):
#     if my_list[index] > sum([my_list[index-1], my_list[index + 1]]):
#         counter += 1
# print(counter)
############################################################################################################################
# my_list = [1, 2, 3, "11", "22", 33]
# my_new_list = []
#
# for index in range(len(my_list)):
#     if type(my_list[index]) == str:
#         my_new_list.append(my_list[index])
# print(my_new_list)
############################################################################################################################
# my_str = " qweeeeee"
# my_list = [i for i in my_str if my_str.count(i) == 1]
# print(my_list)
############################################################################################################################
# my_str_1 = "qwe dfsfdsf e q "
# my_str_2 = "qwe  e  q"
# result = []
# for i in my_str_1:
#     if i in my_str_2:
#         result.append(i)
# print(result)
############################################################################################################################
# my_str_1 = "qwe dfsfdsf q qqq"
# my_str_2 = "qwe zxc  qewqeqweqwe"
# result = []
# for i in my_str_1:
#     k = my_str_1.find(i) - my_str_1.rfind(i)
#     if k == 0:
#         if i in my_str_2 and my_str_2.find(i) - my_str_2.rfind(i) == 0 :
#             result.append(i)
# print(result)