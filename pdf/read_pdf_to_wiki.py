import numpy as np
import os
import subprocess
from os.path import isfile, join

ef = r'pdftotext'


def convert(file_name_pdf):
    file_name_pdf = join(r'./resourses', file_name_pdf)
    bo = subprocess.check_output([ef, '-raw', file_name_pdf])
    return bo.decode('utf-8')


def write_file(bo, file_name, method="wb"):
    file_name = join(r'./results/', file_name)
    with open(file_name, method) as f:
        f.write(bo)


# 去除换行
def adjust(inpath, outpath):
    inpath = join(r'./results/', inpath)
    f = open(inpath, encoding='utf-8')
    lines = f.readlines()
    arr = [len(line) for line in lines]
    length = np.median(arr)  # 行字符数中值
    string = ""
    for line in lines:
        if len(line) >= length and line[-1] == '\n':
            string += line[:-1]  # 去掉句尾的回车
        elif line == '-----------\n':
            pass
        else:
            string += line
    string = string.encode('utf-8')
    write_file(string, outpath)


def rm(inpath):
    inpath = join(r'./results/', inpath)
    os.remove(inpath)


if __name__ == '__main__':
    # 批处理
    su_count = 0
    er_count = 0
    count = 0
    target_path = r'./resourses'
    for base_path, folder_list, file_list in os.walk(target_path):
        for file_name in file_list:
            if file_name[-3:] != 'pdf':
                # 不是pdf文件
                continue
            try:
                pdffile = file_name
                tmpfile = pdffile.replace('pdf', 'tmp')
                txtfile = pdffile.replace('pdf', 'txt')
                bo = convert(pdffile).encode('utf-8')
                write_file(bo, tmpfile)
                adjust(tmpfile, txtfile)
                rm(tmpfile)
                su_count += 1
                count += 1
                print(count, "-->", file_name, " success!\n ")
            except Exception as e:
                er_count += 1
                count += 1
                print(count, "-->", file_name, " error!\n ")

    print("\ncount: ", count, "\n", "success: ", su_count, "\n", "error: ", er_count)
