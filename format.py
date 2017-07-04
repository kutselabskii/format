import os, re

def clangFormat(path):
    fileList = os.listdir(path)
    for i in fileList:
        if os.path.isdir(path + "\\" + i):
            clangFormat(path + "\\" + i)
        else:
            if (re.search('.*\.cpp|.*\.h', i)):
                os.system("clang-format -style=file -i " + path + "\\" + i)


clangFormat(os.getcwd())
