##  py.1



def can_form_palindrome(word):
    a = {}
    for char in word:
        if char in a:
            a[char] += 1
        else:
            a[char] = 1
            
    odd = 0
    
    for i in a.values():
        if i % 2 != 0:
            odd += 1
    
    if odd <= 1:
        return True
    else:
        return False

word=input()
print(can_form_palindrome(word))




##  py.2



def is_palindrome(s):
    return s == s[::-1]

def is_double_base_palindrome(n):
    decimal_str = str(n)
    binary_str = bin(n)[2:]  

    return is_palindrome(decimal_str) and is_palindrome(binary_str)


a=int(input())

if is_double_base_palindrome(a):
    print("True")
else:
    print("False")






## py.3




def list_into_chunks(num_list, chunk_size):
    chunked_list = [num_list[i:i + chunk_size] for i in range(0, len(num_list), chunk_size)]
    return chunked_list


user_input = input()
num_list = list(map(int, user_input.split()))  #
size = int(input())


result = list_into_chunks(num_list, size)
print(result)


