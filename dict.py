def dict():
    dict = open("xxx/xxx/xxx/user.txt", "r",encoding= u'utf-8',errors='ignore')
    # 读取本地爆破字典
    dict_list = dict.read().splitlines()
   
    return dict_list
    dict.close()
pw=dict()
