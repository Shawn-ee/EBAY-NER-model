# BERT NER

Use google BERT to do CoNLL-2003 NER !

![new](https://i.imgur.com/OB4Ugp4.png) Train model using Python and Inference using C++

[ALBERT-TF2.0](https://github.com/kamalkraj/ALBERT-TF2.0)

[BERT-NER-TENSORFLOW-2.0](https://github.com/kamalkraj/BERT-NER-TF)

[BERT-SQuAD](https://github.com/kamalkraj/BERT-SQuAD)


# Requirements

-  `python3`
- `pip3 install -r requirements.txt`

# Run

`python test.py --data_dir=data/ --bert_model=bert-base-cased --task_name=ner --output_dir=out_base --max_seq_length=128 --do_train --num_train_epochs 5 --do_eval --warmup_proportion=0.1`

# dataset
https://drive.google.com/drive/u/0/folders/1XyopBw1-f1JshJJmzNf1DuPFjLGe7NyL

### C++ unicode support 
- http://github.com/ufal/unilib

### Tensorflow version

- https://github.com/kyzhouhzau/BERT-NER
