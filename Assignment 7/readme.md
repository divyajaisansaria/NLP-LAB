# NLP Lab - Assignment 7

## Overview
Assignment 7 focuses on analyzing **tokenized Hindi sentences** from Assignment 1. The main goals are:

1. Build **Unigram and Bigram Language Models**  
2. Compute **PMI (Pointwise Mutual Information) scores** for bigrams  
3. Vectorize sentences using **TF-IDF**  
4. Find **Nearest Neighbor sentences** in validation and test sets  

This README explains the concepts, formulas, and workflow step-by-step.

---

## 1. Unigram & Bigram Models

### Unigram Model
A **unigram model** considers the probability of each word independently.

\[
P(w_i) = \frac{\text{Count}(w_i)}{\text{Total number of words}}
\]

- `w_i` = word in the corpus  
- Count = frequency of the word  

### Bigram Model
A **bigram model** considers the probability of a word given the previous word:

\[
P(w_i \mid w_{i-1}) = \frac{\text{Count}(w_{i-1}, w_i)}{\text{Count}(w_{i-1})}
\]

- Count(w_{i-1}, w_i) = frequency of word pair (bigram)  
- Count(w_{i-1}) = frequency of the first word  

---

## 2. PMI (Pointwise Mutual Information)

PMI measures how strongly two words are associated compared to chance:

\[
PMI(w_1, w_2) = \log_2 \frac{P(w_1, w_2)}{P(w_1) \cdot P(w_2)}
\]

Where:

- \(P(w_1, w_2)\) = probability of bigram  
- \(P(w_1)\), \(P(w_2)\) = unigram probabilities  

**Interpretation:**  

- PMI > 0 → words co-occur more than expected  
- PMI = 0 → words are independent  
- PMI < 0 → words co-occur less than expected  

**Tip:** Use **log base 2** for intuitive "bits of information."

---

## 3. TF-IDF (Term Frequency – Inverse Document Frequency)

TF-IDF is used to vectorize sentences, giving importance to **rare but informative words**.

### Formulas

1. **Term Frequency (TF):**

\[
TF(t, d) = \frac{\text{Count of term t in document d}}{\text{Total terms in document d}}
\]

2. **Inverse Document Frequency (IDF):**

\[
IDF(t) = \log \frac{N}{1 + DF(t)}
\]

- N = total number of documents  
- DF(t) = number of documents containing term t  

3. **TF-IDF:**

\[
TFIDF(t, d) = TF(t, d) \times IDF(t)
\]

**Tip:** Always compute **IDF on the training set** and use it for validation/test sets.

---

## 4. Nearest Neighbor Sentences

Using TF-IDF vectors, we can compute **sentence similarity**.

- **Cosine Similarity** formula:

\[
\text{cosine\_similarity}(A, B) = \frac{A \cdot B}{\|A\| \|B\|}
\]

- \(A\) and \(B\) = TF-IDF vectors of two sentences  
- \(\|A\|\) = L2 norm of vector A  

**Workflow:**

1. Compute TF-IDF vectors for all sentences  
2. For each sentence in validation/test set, compute cosine similarity with all sentences in that set  
3. Choose the sentence with **highest similarity** → nearest neighbor  

---

## 5. Tips for Large NLP Data

1. **Use Parquet instead of TXT/CSV**  
   - Parquet compresses large text (~180 MB → ~50 MB)  
   - Maintains data types and column names  

2. **Virtual Environment**  
   - Keep Python packages isolated  
   - Example packages: `pandas`, `pyarrow`, `scikit-learn`  

3. **Avoid committing large files**  
   - Files >100 MB need Git LFS  
   - Keep compressed files ≤50 MB for GitHub  

---

## 6. Suggested Workflow

1. Load tokenized sentences from Parquet  
2. Build unigram & bigram counts  
3. Compute PMI scores and save as Parquet  
4. Vectorize sentences using TF-IDF  
5. Find nearest neighbors for validation/test sets  
6. Save all outputs as **Parquet files**  

---
