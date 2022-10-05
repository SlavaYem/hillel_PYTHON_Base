#############################################################################
def domains_internet(filename):
    with open(filename, "r") as name:
        text = name.read()
        domen_name = text.replace(".", "")
    return domen_name
my_1_txt = domains_internet("domains.txt")
print(my_1_txt)
#############################################################################
def names (filename):
    with open(filename, "r") as name:
        text = '\t'.join([line.split()[1] for line in name.readlines()])
    return text

my_2_txt = names("names.txt")
print(my_2_txt)
#############################################################################
def authors (filename):
    with open("authors.txt", "r") as name:
        data = [line.split("-") for line in name.readlines()]
        new_list = []
        new_list_2 = []
        for index in range(len(data)):
           new_str = data[index].pop(0)
           new_list.append(new_str)
        for count_1 in new_list:
            dict = {}
            dict["data"] = count_1
            if count_1[0].isdigit():
                new_list_2.append(dict)
    return new_list_2


my_3_txt = authors("authors.txt")
print(my_3_txt)