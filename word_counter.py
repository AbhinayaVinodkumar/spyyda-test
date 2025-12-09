Word Frequency Counter
import re
paragraph=input("Enter a paragraph:")
text=paragraph.lower()
words=re.findall(r"[a-z]+",text)	
frequency={}
for word in words:
	frequency[word]=frequency.get(word,0)+1
sorted_words=sorted(frequency.items(),key=lambda x:x[1],reverse=True)
for word,count in sorted_words:
	print(f"{word} - {count}")
How to run the code?
1. Save the file as word_counter.py
2. Open cmd prompt/terminal
3. run python word_conuter.py
 