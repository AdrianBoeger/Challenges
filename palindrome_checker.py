# Create a function to check if a given string is a palindrome (reads the same backward as forward).

word = 'maoam'


def palindrome(w1):
    list_w1 = list(w1)
    reverse_list_w1 = list_w1.copy()
    reverse_list_w1.reverse()
    if list_w1 == reverse_list_w1:
        print(''.join(list_w1) + ' is a palindrome')
    else:
        print(''.join(list_w1) + ' is not a palindrome')


palindrome(word)
