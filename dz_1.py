#########################################################
value = 123
new_value = value / 2 if value < 100 else - value
########################################################
value = 40
new_value = value / value if value < 100 else value * 0
print(new_value)
#########################################################
value = 140
new_value = True if value < 100 else False
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
