with open('FFt 5.2.txt', encoding='UTF-8') as read_file:
    text = read_file.readlines()
line_in_file = int(len(text))
word_in_file = 0

for line in text:
    string = (line.split())
    word_in_file += int(len(string))
# Подсчитал общее количество слов. Принцип понял, если вложить в цикл фор еще один цикл то можно посчитать количество слов каждой строке.
print(f'В файле {line_in_file} строки и {word_in_file} слов')
