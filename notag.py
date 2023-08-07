
def concatenate_words(input_file, output_file):
    with open(input_file, 'r',encoding='utf-8') as f:
        lines = f.readlines()

    with open(output_file, 'w',encoding='utf-8') as f:
        for line in lines:
            words = line.split()
            if len(words) > 1:
                first_word = words[0]
                remaining_words = "".join(words[1:])
                new_line = first_word + "\t" + remaining_words + "\n"
            else:
                new_line = line
            f.write(new_line)

# usage
concatenate_words("data/fulltraindataset.txt", "data/fulltraindataset.txt")









