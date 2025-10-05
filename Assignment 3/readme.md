# NLP Lab – Assignment 3  
**Google Colab Notebook** → [Open Here](https://colab.research.google.com/drive/1mFG0G0-dTkuoTIBSTNPnRe9MRy_djn7s#scrollTo=99LuxSrSLOGf)

---

## **Overview**
This assignment focuses on implementing **tries**, **stemming analysis**, **frequency distributions**, and **stop word removal** on a given dataset.

---

## **Tasks**

### **Q1. Prefix & Suffix Tries for Stemming**
- Built **prefix trie** and **suffix trie** using the `brown_nouns.txt` dataset.
- Identified the **stem** and **suffix** for each word.
- Compared results of prefix vs suffix tries.

**Example Output:**
# NLP Lab – Assignment 3  
**Google Colab Notebook** → [Open Here](https://colab.research.google.com/drive/1mFG0G0-dTkuoTIBSTNPnRe9MRy_djn7s#scrollTo=99LuxSrSLOGf)

---

## **Overview**
This assignment focuses on implementing **tries**, **stemming analysis**, **frequency distributions**, and **stop word removal** on a given dataset.

---

## **Tasks**

### **Q1. Prefix & Suffix Tries for Stemming**
- Built **prefix trie** and **suffix trie** using the `brown_nouns.txt` dataset.
- Identified the **stem** and **suffix** for each word.
- Compared results of prefix vs suffix tries.

**Example Output:**
Prefix Trie Results:
investigation = in+vestigation
primary = p+rimary
evidence = e+vidence
...
Suffix Trie Results:
investigation = investigati+on
primary = primar+y
evidence = evidenc+e
...


**Observation:**  
- **Suffix trie** performs better for stemming because suffixes are consistent and branch later in the trie.  
- **Prefix trie** struggles in cases where stems vary but suffixes remain consistent.

---

### **Q2. Word Frequency Distribution & Stop Word Removal**
- Used **tokenized dataset** from **Assignment 1** (`tokenized_sentences.txt` stored in Google Drive).
- Implemented a **custom frequency counter** without using NLTK or other libraries.
- Plotted the **top 100 most frequent words**.
- Identified **stop words** using a frequency threshold and removed them.
- Plotted **three additional graphs** after removing stop words using thresholds:
  - **High frequency stop words** removed (e.g., freq > 5000)
  - **Moderate stop words** removed (e.g., freq > 2000)
  - **Low frequency stop words** removed (e.g., freq > 500)

---

## **Results & Visualizations**

### **1. Top 100 Most Frequent Words**
*(Before stop word removal)*  
📊 A bar graph showing the highest occurring 100 words.

### **2. Frequency Distribution After Stop Word Removal**
Three separate graphs plotted for different thresholds:
- **Threshold 1:** High-frequency stop words removed  
- **Threshold 2:** Moderate stop words removed  
- **Threshold 3:** Low-frequency stop words removed  

---

## **Files**
- `brown_nouns.txt` → Dataset for Q1  
- `tokenized_sentences.txt` → Tokenized dataset from Assignment 1  
- `assignment3.ipynb` → Google Colab notebook with full implementation  
- `frequency_distribution_plots.png` → Visualization of word frequencies  

---

## **How to Run**
1. Open the notebook in [Google Colab](https://colab.research.google.com/drive/1mFG0G0-dTkuoTIBSTNPnRe9MRy_djn7s#scrollTo=99LuxSrSLOGf).  
2. Mount Google Drive to access `tokenized_sentences.txt`.  
3. Run all cells sequentially to:
   - Build prefix & suffix tries.
   - Generate stems and suffixes.
   - Calculate frequency distribution.
   - Plot graphs before and after stop word removal.

---

## **Conclusion**
- **Suffix tries** are better suited for stemming English nouns than prefix tries.
- High-frequency words dominate the dataset and need removal for better NLP tasks.
- Removing stop words significantly improves the clarity of frequent token distributions.

---
