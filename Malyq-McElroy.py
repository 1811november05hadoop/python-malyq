#!/usr/bin/env python3
'''
Revature is building a new API! This API contains functions for validating data, 
solving problems, and encoding data. 
The API consists of 10 functions that you must implement.
Guidelines:
1) Edit the file to match your first name and last name with the format shown.
2) Provide tests in the main method for all functions, We should be able to run
this script and see the outputs in an organized manner.
3) You can leverage the operating system if needed, however, do not use any non
legacy command that solves the problem by just calling the command.
4) We believe in self commenting code, however, provide comments to your solutions
and be organized.
5) Leverage resources online if needed, but remember, be able to back your solutions
up since you can be asked.
6) Plagiarism is a serious issue, avoid it at all costs.
7) Don't import external libraries which are not python native
8) Don't change the parameters or returns, follow the directions.
9) Assignment is optional, but totally recommend to achieve before Monday for practice.
Happy Scripting!
© 2018 Revature. All rights reserved.
'''

'''
Use the main function for testing purposes and to show me results for all functions.
'''
def main():
	print('Reverse of "example": ' + reverse('example'))
	print('Acronym of "Portable-Network Graphics": ' + acronym('Portable-Network Graphics'))
	print('Triangle (3,4,5): ' + whichTriangle(3,4,5))
	print('Triangle (3,3,3): ' + whichTriangle(3,3,3))
	print('Triangle (3,2,3): ' + whichTriangle(3,2,3))
	print('Scrabble score "AlPhA": ' + str(scrabble('AlPhA')))
	print('Armstrong 153: ' + str(armstrong(153)))
	print('Prime factors 126: ' + str(primeFactors(126)))
	print('Pangram for "The quick brown fox jumps over the lazy dog": ' + str(pangram("The quick brown fox jumps over the lazy dog")))
	print('Sorting the list [2,4,5,1,3,1]: ' + str(sort([2,4,5,1,3,1])))
	print('Rotating (5,"omg"): ' + rotate(5,'omg'))
	print('Rotating (13,"GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT"): ' + rotate(13,'GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT'))
	evenAndOdds()
'''
1. Reverse a String. Example: reverse("example"); -> "elpmaxe"
Rules:
- Do NOT use built-in tools
- Reverse it your own way
param: str
return: str
'''
def reverse(string):
	temp = ""
	for i in range(len(string)-1,-1,-1):
		temp += string[i]

	return(temp)


'''
2. Convert a phrase to its acronym. Techies love their TLA (Three Letter
Acronyms)! Help generate some jargon by writing a program that converts a
long name like Portable Network Graphics to its acronym (PNG).
param: str
return: str
'''
def acronym(phrase):
	acronym = phrase[0]
	for i in range(0,len(phrase)-1):
		if (phrase[i] == ' ' or phrase[i] == '-') :
			acronym += phrase[i+1]
	return(acronym)

'''
3. Determine if a triangle is equilateral, isosceles, or scalene. An
equilateral triangle has all three sides the same length. An isosceles
triangle has at least two sides the same length. (It is sometimes specified
as having exactly two sides the same length, but for the purposes of this
exercise we'll say at least two.) A scalene triangle has all sides of
different lengths.
param: float, float, float
return: str -> 'equilateral', 'isoceles', 'scalene'
'''
def whichTriangle(sideOne, sideTwo, sideThree):
	if (sideOne == sideTwo and sideOne == sideThree) :
		return('equilateral')
	elif (sideOne != sideTwo and sideOne != sideThree and sideTwo != sideThree) :
		return('scalene')
	else : 
		return('isoceles')

'''
4. Given a word, compute the scrabble score for that word.
--Letter Values-- Letter Value A, E, I, O, U, L, N, R, S, T = 1; D, G = 2; B,
C, M, P = 3; F, H, V, W, Y = 4; K = 5; J, X = 8; Q, Z = 10; Examples
"cabbage" should be scored as worth 14 points:
3 points for C, 1 point for A, twice 3 points for B, twice 2 points for G, 1
point for E And to total:
3 + 2*1 + 2*3 + 2 + 1 = 3 + 2 + 6 + 3 = 5 + 9 = 14
param: str
return: int
'''
def scrabble(word):
	count = 0
	for i in word.lower():
		if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'l' or i == 'n' or i == 'r' or i == 's' or i == 't') :
			count += 1
		elif(i == 'd' or i == 'g') : 
			count += 2
		elif(i == 'b' or i == 'c' or i == 'm' or i == 'p') :
			count += 3
		elif(i == 'f' or i == 'h' or i == 'v' or i == 'w' or i == 'y') :
			count += 4
		elif(i == 'k') :
			count += 5
		elif(i == 'j' or i == 'x') :
			count += 8
		elif(i == 'q' or i == 'z') :
			count += 10
		else :
			count += 0
	return(count)

'''
5. An Armstrong number is a number that is the sum of its own digits each
raised to the power of the number of digits.
For example:
9 is an Armstrong number, because 9 = 9^1 = 9 10 is not an Armstrong number,
because 10 != 1^2 + 0^2 = 2 153 is an Armstrong number, because: 153 = 1^3 +
5^3 + 3^3 = 1 + 125 + 27 = 153 154 is not an Armstrong number, because: 154
!= 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190 Write some code to determine whether
a number is an Armstrong number.
param: int
return: bool
'''
def armstrong(number):
	sum = 0
	numberstr = str(number)
	for i in range(0,len(numberstr)):
		sum += int(numberstr[i]) ** len(numberstr)
	return(sum == number)

'''
6. Compute the prime factors of a given natural number.
A prime number is only evenly divisible by itself and 1.
 
Note that 1 is not a prime number.
param: int
return: list
'''
def primeFactors(number):
	factor_list = []
	return(primeCall(factor_list,number))

def primeCall(flist,number):	
	if(number % 2 == 0):
		flist.append(2)
		primeCall(flist,number / 2)
	elif(number % 3 == 0):
		flist.append(3)
		primeCall(flist,number / 3)
	elif(number % 5 == 0):
		flist.append(5)
		primeCall(flist,number / 5)
	elif(number % 7 == 0):
		flist.append( 7)
		primeCall(flist,number / 7)
	return(flist)
	
'''
7. Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan
gramma, "every letter") is a sentence using every letter of the alphabet at
least once. The best known English pangram is:
The quick brown fox jumps over the lazy dog.
 
The alphabet used consists of ASCII letters a to z, inclusive, and is case
insensitive. Input will not contain non-ASCII symbols.
 
param: str
return: bool
'''
def pangram(sentence):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	for i in alphabet:
		if(i not in sentence):
			return(False)
	return(True)

'''
8. Sort list of integers.
f([2,4,5,1,3,1]) = [1,1,2,3,4,5]
Rules:
- Do NOT sort it with .sort() or sorted(list) or any built-in tools.
- Sort it your own way
param: list
return: list
'''
def sort(numbers):
	less_than = []
	greater_than = []
	if(numbers == []):
		return numbers
	else :
		pivot = numbers[0]
		for n in numbers[1:len(numbers)] :
			if(n < pivot):
				less_than.append(n)
			else: 
				greater_than.append(n)
		return sort(less_than) + [pivot]  + sort(greater_than)
	

'''
9. Create an implementation of the rotational cipher, also sometimes called
the Caesar cipher.
The Caesar cipher is a simple shift cipher that relies on transposing all the
letters in the alphabet using an integer key between 0 and 26. Using a key of
0 or 26 will always yield the same output due to modular arithmetic. The
letter is shifted for as many values as the value of the key.
The general notation for rotational ciphers is ROT + <key>. The most commonly
used rotational cipher is ROT13.
A ROT13 on the Latin alphabet would be as follows:

Plain: abcdefghijklmnopqrstuvwxyz Cipher: nopqrstuvwxyzabcdefghijklm It is
stronger than the Atbash cipher because it has 27 possible keys, and 25
usable keys.
Ciphertext is written out in the same formatting as the input including
spaces and punctuation.
Examples: ROT5 omg gives trl ROT0 c gives c ROT26 Cool gives Cool ROT13 The
quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire
gur ynml qbt. ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The
quick brown fox jumps over the lazy dog.
param: int, str
return: str
'''
def rotate(key, string):
	alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
	alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	rotated_lower = alphabet_lower[key:] + alphabet_lower[:key]
	rotated_upper  = alphabet_upper[key:] + alphabet_upper[:key]
	
	alphabet = alphabet_lower + alphabet_upper
	rotated  = rotated_lower + rotated_upper
	
	table = str.maketrans(alphabet,rotated)
	return string.translate(table)

'''
10. Take 10 numbers as input from the user and store all the even numbers in a file called even.txt and
the odd numbers in a file called odd.txt.
param: none, from the keyboard
return: nothing
'''
def evenAndOdds():
	number = input("Enter 10 digits: ")
	even_file = open("even.txt","w+")
	odd_file = open("odd.txt","w+")
	
	for c in number:
		if(int(c) % 2 == 0):
			even_file.write(c)
		else:
			odd_file.write(c)
	even_file.close()
	odd_file.close()		








if __name__ == '__main__':
	main()
