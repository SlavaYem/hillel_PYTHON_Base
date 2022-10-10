# #############################################################################
def domains_internet(filename):
    my_1_txt = []
    with open(filename, "r") as name:
        text = name.read()
        domen_name = text.replace(".", "")
        my_1_txt.append(domen_name)
    return my_1_txt
my_1_txt = domains_internet("domains.txt")
print(my_1_txt)
# #############################################################################
def names (filename):
    with open(filename, "r") as name:
        text = '\t'.join([line.split()[1] for line in name.readlines()])
    return text

my_2_txt = names("names.txt")
print(my_2_txt)
# #############################################################################
def authors (filename):
    with open("authors.txt", "r") as name:
        data = [line.split("-")[0] for line in name.readlines()]
        new_list = []
        for count_1 in data:
            dict = {}
            dict["data"] = count_1
            if count_1[0].isdigit():
                new_list.append(dict)
    return new_list


my_3_txt = authors("authors.txt")
print(my_3_txt)