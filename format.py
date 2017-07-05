import os, re

def clangFormat(path):
    fileList = os.listdir(path)
    for i in fileList:
        if os.path.isdir(path + "\\" + i):
            clangFormat(path + "\\" + i)
        else:
            if (re.search('.*\.cpp|.*\.h', i)):
                nameCheck(path, i)
                os.system("clang-format -style=file -i " + path + "\\" + i)

def nameCheck(path, filename):
    os.system("clang -Xclang -ast-dump " + path + "\\" + filename + " > " + path + "\\dump.d")
    file = open(path + "\\dump.d", "r")
    data = file.readlines()
    file.close()
    for i in data:
        i = i.rstrip('\n')

        #Namespaces check
        if (re.search('NamespaceDecl', i)):
            if (re.search('invalid', i) == None):
                string = re.sub('^.*> ', '', i)
                place = re.findall(placementReg, string)[0]
                string = re.sub(place, '', string)
                if (string not in namespaceList):
                    if (re.match(namespaceReg, string) == None):
                        print ('@->Namespace ' + string + ' on ' + place + 'in ' + path + "\\" + filename)
                    namespaceList.append(string)

        #Functions check
        if (re.search('FunctionDecl', i)):
            if (re.search('invalid', i) == None):
                string = re.sub('^.*> ', '', i)
                place = re.findall(placementReg, string)[0]
                string = re.sub(place, '', string)
                string = re.sub(' .*$', '', string)
                if (string not in funcList):
                    if (re.match(functionReg, string) == None):
                        print ('@->Function ' + string + ' on ' + place + 'in ' + path + "\\" + filename)
                    funcList.append(string)
        #Variables check
        if (re.search('VarDecl', i)):
            if (re.search('invalid', i) == None):
                string = re.sub('^.*> ', '', i)
                place = re.findall(placementReg, string)[0]
                string = re.sub(place, '', string)
                string = re.sub(' .*$', '', string)
                if (string not in varList):
                    if (re.match(variableReg, string) == None):
                        print ('@->Variable ' + string + ' on ' + place + 'in ' + path + "\\" + filename)
                    varList.append(string)    

                
#Ignored names
global varList, funcList, namespaceList
namespaceList = []
funcList = ['main']
varList = []

#Default regexes
global namespaceReg, variableReg, functionReg
namespaceReg = '^[a-z][a-z0-9_]*$' #under_score
variableReg  = '^[a-z][a-z0-9_]*$' #under_score
functionReg  = '^[a-z][a-z0-9_]*$' #under_score

#AST regexes
global placementReg
placementReg = '\w{3,4}(?::\d+){1,2} ' #aaaa:11:11 || aaaa:11

currentDir = re.sub('format\.py', '', os.path.abspath(__file__))

config = open(currentDir + '\\format.config', 'r')
config_data = config.readlines()
config.close()
for i in config_data:
    if (re.search('Namespace:', i)):
        namespaceReg = re.findall('\^.*\$', i)[0]
    if (re.search('Variable:', i)):
        variableReg = re.findall('\^.*\$', i)[0]
    if (re.search('Function:', i)):
        functionReg = re.findall('\^.*\$', i)[0]

clangFormat(currentDir)
wait = input('Watch')

##nameCheck('D:\\Test\\test', 'Source.cpp')

##dump = open('D:\\Test\\test\\dump.d', 'r')
##data = dump.readlines()
##dump.close()
##
##for i in data:
##    print(i)
##    a = input()
##    if (a == 'q'):
##        break

