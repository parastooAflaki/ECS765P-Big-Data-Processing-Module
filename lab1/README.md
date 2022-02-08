Lab 1, week 2
---

We’ll be using ’mrjob’ for our ’MapReduce’ programmes. This Python package provides a higher level API over the existing Hadoop Streaming mechanism.

Q1. How many times does the word Sherlock appear in the file?
    
    python q1-wordcount.py input/sherlock.txt > out1.txt
    # 345
    
Q2. How many words appear 10 or more times in the document?
   
    python q2-wordcount.py input/sherlock.txt > out2.txt
    # 3965
    
Q3. In total, how many occurrences of words does the document have (including duplicates, but only counting words with 10+ occurrences)?
  
    python q3-wordcount.py input/sherlock.txt > out3.txt
    wc -l out3.txt
    # 513066
    
Q4. What is the length of the longest word(s) in the dataset?
    
    python q4-wordcount.py input/sherlock.txt > out4.txt
    # 3 : The

Q5. What is the most frequent word length?

    python q4-wordcount.py input/sherlock.txt > out4.txt
    # 63644 : len 3

