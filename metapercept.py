#1 .to check longest word in string
str=( "dummy text of the printing and typesetting industry.")

word_list=str.split()

longest_word=max(word_list,key=len)

position=str.index(longest_word)

print("longest_word:",longest_word)


#2.To check email valid or not

import re
regex=(r'^[a-z 0-9]+[\._] ?[a-z 0-9]+[@]\w+[.]\w{2,3}$')
def check (email):
    if (re.search(regex,email)):
        print("Valid Email")
    else:
        print("Invalid Email")

if __name__=='__main__':

    email="test01*gmail.com"
    check(email)

    email="student01@gmail.com"
    check(email)
                

 #2 find maximum number of jagged array

def find_max_number(arr):
    max_num = float('-inf')
    for element in arr:
        if isinstance(element, list):
        
            max_num = max(max_num, find_max_number(element))
        else:
            
            max_num = max(max_num, element)
    return max_num


input_array = [2, 4, 10, [12, 4, [100, 99], 4], [3, 2, 99], 0]
result = find_max_number(input_array)
print("Maximum number in the jagged array:", result)


