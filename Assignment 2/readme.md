# NLP Lab — Assignment 2  
**Finite State Transducer (FST) for Noun Morphology**

🔗 **Google Colab Notebook:** [Click here to open in Colab](https://colab.research.google.com/drive/1WKy6HNpQrYexlQnnx3f4otmDwrEBQwuW#scrollTo=fpOmS_AaDDTs)

---

## Objective
In this assignment, we design a **Finite State Transducer (FST)** that generates the **morphological features** of nouns from the **Brown Corpus**.  
The system outputs the root word, part of speech, and grammatical number.

---

## Input
- **File**: `brown_nouns.txt`
- Contains a list of nouns from the **Brown Corpus**.

---

## FST Rules Implemented
| Rule            | Description                                  | Example |
|-----------------|----------------------------------------------|--------|
| **E insertion** | Add **e** before `-s` if the word ends with **s, z, x, ch, sh** | `fox → foxes` |
| **Y replacement** | Replace **y** with **ies** if preceded by a consonant | `try → tries` |
| **S addition** | Simply add **s** for other nouns | `bag → bags` |

---

## Output Format
Each word is represented in the following format:  

