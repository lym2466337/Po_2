"""
    text,设置    --》//*[contain(@text,'设置')]
    text,设置，1  --->//*[contain(@text,'设置')]
    text,设置，0   -->//*[@text,'设置']
"""
loc = "text,设置,0"


def get_xpath(loc):
    str_m = ''
    arg_list = loc.split(",")
    key_index = 0
    value_index = 1
    option_index = 2
    if len(arg_list) == 2:
        str_m = "contain(@" + arg_list[key_index] + ",'" + arg_list[value_index] + "')" +"and"
    elif len(arg_list) == 3:
        if arg_list[option_index] == "1":
            str_m = "contain(@" + arg_list[key_index] + ",'" + arg_list[value_index] + "')" +"and"
        elif arg_list[option_index] == "0":
            str_m = "@" + arg_list[key_index] + ",'" + arg_list[value_index] + "'" +"and"
    return str_m


def get_xpaths(loc):
    str_start = "//*["
    str_end = "]"
    str_m = ''
    if isinstance(loc, str):
        if loc.startswith("//"):
            return loc
        str_m = get_xpath(loc)
    else:
        for i in loc:
            str_m += get_xpath(i)
    str_m = str_m.rstrip("and")
    loc = str_start + str_m + str_end
    return loc


print(get_xpaths(["text,设置,0","text,设置,1","text,设置,1"]))
print("xxxx")
print("yyyyyyy")
