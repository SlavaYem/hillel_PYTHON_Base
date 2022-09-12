#########################################################
value = 123
new_value = value / 2 if value < 100 else - value
########################################################
value = 14
if value < 100:
    new_value = 1
else:
    new_value = 0
#########################################################
value = 245
if value < 100:
    new_value = True
else:
    new_value = False
#########################################################
my_str = "zxc"
if len(my_str) < 5:
    new_str = my_str * 2
else:
    new_str = my_str
#########################################################
my_str = "zxc"
if len(my_str) < 5:
    new_str = my_str + my_str[::-1]
else:
    new_str = my_str
