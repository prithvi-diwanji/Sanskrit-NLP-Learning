# Sanskrit Tokenizer Script (Beginner Level)
# Created as part of learning exercises by Prithvi Diwanji

# This script tokenizes a basic Sanskrit sentence using whitespace

# Input sentence
sentence = "रामः वनं गच्छति।"

# Tokenize the sentence by splitting on whitespace
tokens = sentence.split()

# Print each token with its index
print("Tokenized Output:")
for idx, token in enumerate(tokens, start=1):
    print(f"{idx}: {token}")
