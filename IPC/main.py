import re, os

path = "IPC_Chinese_txt/"

for f in os.listdir(path):
    with open(path + f, 'r', encoding='utf8') as datafile:
        linelist_orig = datafile.readlines()
        linelist = linelist_orig

    for line in linelist_orig:
        # if re.match(r'^A\d{1,2}', line):
        if re.match(r'小类索引', line):
            print(line)
            print(linelist.index(line))
            linelist.remove(line)
        if re.match(r'附注', line):
            print(linelist)

    break