import re

subj = {}


with open('FFt 5.6.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        subject, lecture, practice, lab = line.split()
        su = re.sub("[:]", "", subject)
        lec = re.sub("[^0123456789]", "", lecture)
        if lec == "": lec = 0
        p = re.sub("[^0123456789]", "", practice)
        if p == "": p = 0
        la = ''.join(i for i in lab if i.isdigit())
        if la == "": la = 0
        subj[su] = int(lec) + int(p) + int(la)
    print(f'Общее количество часов по предмету - \n {subj}')