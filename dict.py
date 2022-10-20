def dict():
    dict = open("/Users/cunyang/Desktop/tools/zidian/user.txt", "r",encoding= u'utf-8',errors='ignore')
    # dict_list=list(dict.readlines())
    dict_list = dict.read().splitlines()
    # print(dict_list)
    # for i in range(len(dict_list)):
    #     password =dict_list[i]
    return dict_list
    dict.close()
pw=dict()
