my_str='noon'#02022020
my_str=my_str.casefold()
rev_str=reversed(my_str)
if list(my_str)==list(rev_str):
   print("The string is palindrome.")
else:
   print("This string is not palindrome.")
