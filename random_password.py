from random import choice

len_of_password = 10
valid_chars_for_password = "123456789!@#$%^&*()_+ASDFGHJKLZXCVBNMQWETYUIOPzxcvbnmasdfghjklqwertyuiop()"

#print(choice(valid_chars_for_password))

'''
password = []

for each_char in range(len_of_password):
    password.append(choice(valid_chars_for_password))

random_password = "".join(password)
print(random_password)
'''

random_password = "".join(choice(valid_chars_for_password) for each_char in range(len_of_password))
print(random_password)






