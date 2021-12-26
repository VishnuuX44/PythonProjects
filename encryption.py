def encrypt(sentence):

	 result = []

	 for letter in sentence:

	 	l = ord(letter) -20
	 	result.append(l)


    
	 for numbers in result:
	 	print(numbers, end='')
	 	print(" ", end='')

	 	print()
	 	decrypt(result)

def decrypt(result):
	end_string = ""

	for numbers in result:

		l = int(numbers)
		l = l + 20
		l = chr(l)
		end_string = end_string + l
		
	print("your decrypted message is: ")
	print(end_string)


def main():
	s = input("input a sentence: ")
	encrypt(s)

if __name__ == '__main__':
	main()