
import os
import pandas as pd

# current_dir = os.getcwd()
# print(current_dir)
# isEx = os.path.exists('data.txt')
# print(isEx)
# txt_file = open('data.txt', 'a')
# str = '你好'
# str_encode = str.encode()
# txt_file.write('\n' + str)
# txt_file.close()

# test_str = 'http://www.baidu.com/tets/hello.png'
# str_split = test_str.split('/')
# print(str_split)
# last_one = str_split[-1]
# print(last_one)
#
# str_index = test_str.rfind('/')
# print(str_index)
# print(len(test_str))
# str_find = test_str[str_index+1:len(test_str)]
# print(str_find)

# result = []
# def get_all(cwd):
#     get_dir = os.listdir(cwd)
#     for i in get_dir:
#         sub_dir = os.path.join(cwd, i)
#         if os.path.isdir(sub_dir):
#             get_all(sub_dir)
#         else:
#             result.append(i)


# if __name__ == "__main__":
#     get_all(os.getcwd())
#     print(result)

# def isXLSX(str):
#     str_split = str.split('.')
#     last_one = str_split[-1]
#     return last_one == 'xlsx'


# if __name__ == "__main__":
excel_dir = os.getcwd() + '/excel/'
file1 = excel_dir + 'excel1.xlsx'
file2 = excel_dir + 'excel3.xlsx'
merge_file = '安海燕宝贝专属.xlsx'

data1 = pd.read_excel(file1)
print(data1)

data2 = pd.read_excel(file2)
print(data2)

data_merge = pd.merge(data1, data2, how='left')
print(data_merge)





# xlsx_list = os.listdir(os.path.join(os.getcwd(), 'excel'))
# print(xlsx_list)

