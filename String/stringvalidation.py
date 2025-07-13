if __name__ == '__main__':
    s = input()
    
print(any(let.isalnum() for let in s))
print(any(let.isalpha() for let in s))
print(any(let.isdigit() for let in s))
print(any(let.islower() for let in s))
print(any(let.isupper() for let in s))