Questionnaire:

a. def is_palindrone(s):
    r=""
    for c in s:
        r = c +r
    for x in range(0, len(s)):
        if s[x] == r[x]:
            x = True
        else:
            return False
    return x

A palindrome is a word which is the same both forwards and backwards.
The code above works as follows: using an empty string r, iterate over every
character in string s and add the new letter to the front of r, meaning that r
is the backwards representation of s. Now, iterate over s, comparing the value
at each index to the value at the same index in r, ensuring they are the same.

If I were writing a palindrome function in Python, I would utilize string indexing.
In order to check if s is a palindrome, I would check if s == s[::-1], which
essentially checks if s is equal to the reverse of s.

This would be beneficial for two reasons: 1. It would requires fewer lines of code, 
thereby improving readability and clarity and 2. It would allow for one iteration
over the string s instead of two, saving time.

b. Compilation instructions: 

I installed the following libraries to import into my Python code:
pip3 install requests
pip3 install beautifulsoup4
pip3 install matplotlib

Within my VS Code editor, I ran the following in the terminal:

python3 main.py
