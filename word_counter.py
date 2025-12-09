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

logic explanation
The main objective of this program is to count how many times each unique word appears in a given paragraph and display the result in descending order of frequency. The logic is designed to be simple, accurate, and efficient while handling different text formats such as punctuation and uppercase letters.

First, the program takes the paragraph as input from the user using the input() function. This allows the user to enter any sentence or group of sentences. Since words like “Hello” and “hello” must be treated as the same word, the entire input text is converted to lowercase using the lower() method. This ensures the counting logic is case-insensitive and avoids duplicate records due to letter case differences.

Next, the program removes punctuation and non-letter symbols to extract only valid words. This is done using Python’s regular expression method re.findall() with the pattern [a-z]+. This pattern scans the paragraph and selects only continuous groups of alphabetic characters. As a result, special characters such as commas, periods, quotation marks, and symbols are completely ignored. For example, the word "hello," becomes "hello" and is counted correctly as a normal word.

After extracting the clean list of words, the program counts the frequency of each word using a dictionary. A dictionary is chosen because it can store data in key–value pairs, where the word becomes the key and its count becomes the value. The program loops through each word in the list. If the word already exists in the dictionary, its count is increased by one. If the word is not present, it is added to the dictionary with a starting count of one. This method ensures accurate tracking of every occurrence of each word in the paragraph.

Once the dictionary is fully populated, the next step is sorting. The task requires words to be displayed in descending order of frequency. The program uses Python’s sorted() function along with a lambda expression that sorts the dictionary items based on their frequency values. By setting reverse=True, the words with the highest counts appear at the top of the output list.

Finally, the program prints the sorted results in the required output format: word - count. A loop iterates over the sorted list and prints each word along with its corresponding frequency on a new line. This provides a clear, readable display of results where the most commonly used words appear first, followed by less frequent words.

The overall logic is effective because it performs all required operations in structured steps: input reading, case normalization, word extraction, frequency counting, sorting, and formatted output. The use of regular expressions prevents text-formatting issues, and the dictionary ensures efficient counting with minimal complexity. As a result, the program accurately converts any paragraph input into a clean and organized word frequency list in descending order, meeting all assignment requirements.


 
