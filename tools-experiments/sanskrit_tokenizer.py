# Sanskrit Tokenizer Script (Beginner Level)
# Created as part of learning exercises by Prithvi Diwanji
# This script performs simple tokenization of a Sanskrit sentence using whitespace.
# It was uploaded as part of my learning process in Sanskrit + NLP.
# I am currently exploring basic tools like tokenizers, glossers, and structured annotation.
# I am learning how to tokenize sentences and understand how such tools work under the hood.
# This script is intended for learning and demonstration, not for production use.
# Input sentence
sentence = "रामः वनं गच्छति।"

# Tokenize the sentence by splitting on whitespace
tokens = sentence.split()

# Print each token with its index
print("Tokenized Output:")
for idx, token in enumerate(tokens, start=1):
    print(f"{idx}: {token}")
