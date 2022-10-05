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
#######################################