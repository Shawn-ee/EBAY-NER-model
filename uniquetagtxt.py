def get_unique_tags(input_file):
    unique_tags = set()

    with open(input_file, 'r',encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        words = line.split()
        if len(words) > 1:
            tag = "".join(words[1:])
            unique_tags.add(tag)

    return list(unique_tags)

# usage
unique_tags = get_unique_tags("data/fulltraindataset.txt")
print(unique_tags)