import csv
import sys
import os
class datasubmit:
    import csv
    def __init__(self, input_txt, output_tsv):
        self.input_txt = input_txt
        self.output_tsv = output_tsv

        # Increase the CSV field size limit
        maxInt = sys.maxsize
        while True:
            try:
                csv.field_size_limit(maxInt)
                break
            except OverflowError:
                maxInt = int(maxInt / 10)

    def _process_lines(self):
        sentences = []
        sentence = []
        with open(self.input_txt, 'r', encoding='utf-8') as f:
            for line in f:  # This reads the file line-by-line
                line = line.strip()
                if line:  # If the line is not empty
                    sentence.append(line)
                else:  # If the line is empty
                    if sentence:
                        sentences.append(sentence)
                        sentence = []
        # Handle the last sentence if the file doesn't end with an empty line
        if sentence:
            sentences.append(sentence)
        return sentences

    def convert(self):
        sentences = self._process_lines()

        # Write to the TSV file
        with open(self.output_tsv, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter='\t')
            for idx, sentence in enumerate(sentences, 1):
                for word in sentence:
                    writer.writerow([idx, '', word])  # Empty second column

    def append_array_to_column(self, data_array):
        temp_file = "temp.tsv"
        data_array = [item for sublist in data_array for item in sublist]
        with open(self.output_tsv, 'r', encoding='utf-8') as f_in, open(temp_file, 'w', encoding='utf-8') as f_out:
            for line, new_value in zip(f_in, data_array):
                columns = line.strip().split('\t')

                # Ensure there are enough columns
                while len(columns) < 2:
                    columns.append('')

                # Update the second column
                columns[1] = new_value

                # Write the updated line to the temp file
                f_out.write('\t'.join(columns) + '\n')

        # Replace the original file with the updated file
        os.remove(self.output_tsv)
        os.rename(temp_file, self.output_tsv)




