def split_file_with_encoding(file_path, num_parts):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lines_per_part = (len(lines) + num_parts - 1) // num_parts

    for i in range(num_parts):
        start_idx = i * lines_per_part
        end_idx = min((i + 1) * lines_per_part, len(lines))
        part_lines = lines[start_idx:end_idx]

        with open(f'part_{i}.txt', 'w', encoding='utf-8') as out:
            out.writelines(part_lines)

# Usage: Replace 'fulltraindataset.txt' with your input file path and 3 with the desired number of parts.
split_file_with_encoding('data/fulltraindataset.txt', 3)