import pandas as pd
import os

# Absolute path to your TXT file
txt_file = "/Users/divyajaisansaria/Desktop/NLP/Assignment 1/tokenized_sentences.txt"

# Output Parquet file in the same folder
parquet_file = "/Users/divyajaisansaria/Desktop/NLP/Assignment 1/tokenized_sentences.parquet"

# Check if TXT exists
if not os.path.exists(txt_file):
    raise FileNotFoundError(f"{txt_file} not found!")

# Load sentences
with open(txt_file, "r", encoding="utf-8") as f:
    sentences = f.read().splitlines()

# Convert to DataFrame
df = pd.DataFrame({"sentence": sentences})

# Save as Parquet with Snappy compression
df.to_parquet(parquet_file, engine='pyarrow', index=False, compression='snappy')

print(f"Parquet file saved: {parquet_file} ({os.path.getsize(parquet_file)/1024/1024:.2f} MB)")
