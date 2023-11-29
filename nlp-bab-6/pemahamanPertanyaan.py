
from nltk import word_tokenize, pos_tag

# teks pertayaan
question = "Siapa penemu lampu?"

# tokenisasi dan pos stagging
tokens = word_tokenize(question)
pos_tags = pos_tag(tokens)

for word, pos in pos_tags:
 if pos == 'NNP':
  print(f"{word} adalah sebuah pertanyaan.")


# contoh 1
# teks pertanyaan
pertanyaan1 = "Kapan pertama kali pesawat terbang ditemukan?"

# tokenisasi dan pos tagging
tokens1 = word_tokenize(pertanyaan1)
pos_tags1 = pos_tag(tokens1)

for word, pos in pos_tags1:
 if pos == 'NNP':
  print(f"{word} adalah sebuah pertanyaan.")




# contoh 2

# teks pertanyaan
pertanyaan2 = "Berapa panjang sungai amazon?"

# tokenisasi dan pos tagging
tokens2 = word_tokenize(pertanyaan2)
pos_tags2 = pos_tag(tokens2)

for word, pos in pos_tags2:
 if pos == 'NNP':
  print(f"{word} adalah sebuah pertanyaan.")



# contoh 3

# teks pertanyaan
pertanyaan3 = "Bagaimana cara membuat kue brownies?"

# tokenisasi dan pos tagging
tokens3 = word_tokenize(pertanyaan3)
pos_tags3 = pos_tag(tokens3)

for word, pos in pos_tags3:
 if pos == 'NNP':
  print(f"{word} adalah sebuah pertanyaan.")

