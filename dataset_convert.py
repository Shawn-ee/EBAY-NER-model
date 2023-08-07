import csv
import sys
maxInt = sys.maxsize

while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

def count_columns(filename):
    with open(filename, encoding='utf-8') as f:
        tsvreader = csv.reader(f, delimiter='\t')
        num_columns = max(len(row) for row in tsvreader)
    return num_columns

def count_words(input_string):
    words = input_string.split()
    return len(words)



# Replace 'your_file.tsv' with the path to your TSV file
# file_path = 'data/fulltraindataset.txt'
# num_columns = count_columns(file_path)
# print(f'The TSV file has {num_columns} columns.')




with open('data/Train_Tagged_Titles.tsv',encoding='utf-8') as f,open('data/fulltraindataset.txt', 'w', encoding='utf-8') as out:
    tsvreader = csv.reader(f,delimiter='\t')
    prev_record_num = None
    for line_num, line in enumerate(tsvreader, 1):
        try:
            if len(line) < 4:
                continue
            record_num = line[0]
            title = line[1]
            token = line[2]
            tag = line[3]
            word_count = count_words(token)
            if prev_record_num is not None and record_num != prev_record_num:
                out.write('\n')  # Write an extra newline (empty line) between titles.
            if record_num is not None and word_count==1:
                # print(title+'token::'+token+'tag::'+tag)
                out.write(f'{token}\t{tag}\n')  # Write the token and tag to the output file.
                prev_record_num = record_num

        except Exception as e:
            print(f"Error on line {line_num}: {e}")






