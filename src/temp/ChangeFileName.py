# -*- coding: utf-8 -*-

import os
import re


def change_file_name(path):
    if path == '': 
        path = os.getcwd()          #获取当前路径
    print(path)

    files_list = os.listdir(path)   # 获取目标路径文件名列表
    for name in files_list:
        print(name, end = '')
        if "_1" in name:
            new_name = name.replace('_1', '')
            os.rename(path+ '\\' + name, path + '\\' + new_name)
            print(' CHANGE_TO: ', new_name, end = '')
        print()


def change_file_name_1(path):
    if path == '': 
        path = os.getcwd()          #获取当前路径
    print(path)

    files_list = os.listdir(path)   # 获取目标路径文件名列表
    for name in files_list:
        print(name, end = '')
        if re.match(r'[4-9][1-4][0-4]\.mp3', name):
            new_name = 'IELTS0' + name[0] + 'T' + name[1] + 'S' + name[2] + '.mp3'
            os.rename(path+ '\\' + name, path + '\\' + new_name)
            print(' CHANGE_TO: ', new_name, end = '')
        print()



if __name__ == '__main__':
    change_file_name('')
