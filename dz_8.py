############################################################################################################
# my_list = ["qwe", "zxc", "ert", "tyu"]
# new_list = []
# for i, num in enumerate(my_list):
#     if i % 2:
#         new_list.append(num[::-1])
#     else:
#         new_list.append(num)
# print(new_list)
############################################################################################################
# my_list = ["abc","dbc","zxc"]
# new_list = []
# for index in my_list:
#      if "a" == index[0]:
#          new_list.append(index)
# print(new_list)
############################################################################################################
# my_list = ["abc","dbc","zxc" ," dfsf aa"]
# new_list = []
# for index in my_list:
#      if "a" in index:
#          new_list.append(index)
# print(new_list)
############################################################################################################
# persons = [{"name": "John", "age": 15},
#            {"name": "Anna", "age": 27},
#            {"name": "Johna", "age": 30}]
# youngest_person = []
# ages = []
# longest_person_name = []
# name_lens = []
#
# for person_dict in persons:
#     ages.append(person_dict["age"])
#     name_lens.append(len(person_dict["name"]))
# # print(name_lens, ages)
# min_age = min(ages)
# max_len_name = max(name_lens)
#
# for person_dict in persons:
#     if person_dict["age"] == min_age:
#         youngest_person.append(person_dict["name"])
#     if len(person_dict["name"]) == max_len_name:
#         longest_person_name.append(person_dict["name"])
#
# mean_age = sum(ages) / len(ages)
#
# print(youngest_person, longest_person_name, mean_age)
############################################################################################################
# my_dict_1 = {1: 1, 2: 2, 3: 3, 11: 100}
# my_dict_2 = {11: 11, 2: 22}
#
# result_1 = list(set(my_dict_1.keys()).intersection(set(my_dict_2.keys())))
# print(result_1)
#
# result_2 = list(set(my_dict_1.keys()).difference(set(my_dict_2.keys())))
# print(result_2)
#
# result_3 = {key: my_dict_1[key] for key in result_2}
# print(result_3)
#
# result_4 = my_dict_1.copy()
# for key in my_dict_2:
#     if key in result_4:
#         result_4[key] = [result_4[key], my_dict_2[key]]
#     else:
#         result_4[key] = my_dict_2[key]
# print(result_4)
############################################################################################################