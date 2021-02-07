'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC

Sample Output

2
'''

def count_substring(string, sub_string):
    
    string_count = 0
    com = ""
    for i in range(len(string)):
        com = string[i:i + len(sub_string)]
        if com == sub_string:
            string_count += 1
        
    
    return string_count