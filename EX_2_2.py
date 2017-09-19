import json
import re

with open('pizza-train.json') as data_file:
    data = json.load(data_file)

#this line below is to get the output shown in the hand-in
#data = data[1:3]

list_lines = []
words = set()
bag_of_words_matrix = []

for index in data:
    line = re.findall('[a-z0-9]+', index['request_text'].lower())

    word_dict = {}
    for word in line:
        words.add(word)
        if word not in word_dict:
            word_dict[word]=1
        else:
            word_dict[word] += 1
    list_lines.append(word_dict)

for row in list_lines:
    matrix_row = []
    for column in words:
        if column in row:
            matrix_row.append(row[column])
        else:
            matrix_row.append(0)
    bag_of_words_matrix.append(matrix_row)

print words
print bag_of_words_matrix

print len(bag_of_words_matrix)
print len(words)






