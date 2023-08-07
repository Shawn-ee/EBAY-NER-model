import csv
import sys
maxInt = sys.maxsize
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
def count_words(input_string):
    words = input_string.split()
    return len(words)

def find_unique_labels(file_path):
    unique_labels = set()

    with open('data/Train_Tagged_Titles.tsv', encoding='utf-8') as f:
        tsvreader = csv.reader(f, delimiter='\t')

        for line in tsvreader:
            if len(line) < 4:
                continue
            record_num = line[0]
            title = line[1]
            token = line[2]
            tag = line[3]
            word_count = count_words(token)
            if record_num is not None and word_count == 1:
                unique_labels.add(tag)

    return list(unique_labels)






unique_labels = find_unique_labels('data/Train_Tagged_Titles.tsv')
print(unique_labels)
