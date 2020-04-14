
from translate import Translator
with open('FFt 5.4.txt', encoding='UTF-8') as salary_file:
    new_list = salary_file.readlines()

word_list = [k.strip() for w in new_list for k in w.split('—')]
translator = Translator(from_lang="english",to_lang="russian")

b = 0
push_list = []
for i, el in enumerate(word_list[::2]):
    translate = translator.translate(el)
    word_list.pop(b)
    word_list.insert(b,translate)
    b +=2

for i in range(0, len(word_list), 2):
    result_list = []
    result_list.append(word_list[i])
    result_list.append(' - ')
    result_list.append(word_list[i+1])
    push_list.append(result_list)

with open('FFt 5.4.1.txt', 'w', encoding='UTF-8') as new_file:
    for i in push_list:
        i.append('\n')
        new_file.writelines(i)