import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list = []

user_letters = int(input('how many letters\n'))
user_capital_letters = int(input('how many capitals\n'))
user_numbers =  int(input('how many numbers\n'))
user_symbols = int(input('how many symbols\n'))


password_list.append(random.choices(letters, k=user_letters))
password_list.append(random.choices(symbols, k=user_symbols))
password_list.append(random.choices(numbers, k= user_numbers))
password_list.append(random.choices(capital_letters, k= user_capital_letters))

print(password_list)
password_list = sum(password_list, [])
print(password_list)

generated_password = random.shuffle(password_list)

generated_password = ''.join(password_list)

print(generated_password)