def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    next_num = n + 1
    while not is_prime(next_num):
        next_num += 1
    return next_num

def modify_text(input_text):
    ignored_letters = set('BCEGKMQSWbcegkmqsw')
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    prime = 2
    result = []

    for char in input_text:
        if char in ignored_letters:
            result.append(char)
        elif char in lowercase:
            index = lowercase.index(char)
            new_index = (index + prime) % 26
            result.append(lowercase[new_index])
            prime = next_prime(prime)
        elif char in uppercase:
            index = uppercase.index(char)
            new_index = (index + prime) % 26
            result.append(uppercase[new_index])
            prime = next_prime(prime)
        else:
            result.append(char)

    return ''.join(result)

# Test the function
input_text = input("Enter your text: ")
modified_text = modify_text(input_text)
print("Modified text:", modified_text)
