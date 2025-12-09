Balanced Brackets
def is_balanced(brackets):
	stack=[]
	pair={')':'(',']':'[','}':'{'}
	for char in brackets:
		if char in "([{":
			stack.append(char)
		elif char in ")]}":
			if not stack or stack.pop() != pair[char]:
				return False

	return len(stack)==0
print(is_balanced("{[()]}"))
print(is_balanced("([)]"))
 
How to run code?
1. Save the code in a file: balanced.py
2. Open terminal / command prompt.
3. Run python balanced.py
logical explanation
A Balanced Brackets Validator checks whether every opening bracket has a matching closing bracket in the correct order. The brackets used are (), [], and {}. The logic is based on a stack, which follows the Last-In-First-Out (LIFO) rule. When the program reads an opening bracket, it pushes it onto the stack. When it reads a closing bracket, it pops from the stack and checks whether the types match. If there is a mismatch or the stack becomes empty early, the string is unbalanced. After processing the whole string, if the stack is empty, the brackets are balanced.