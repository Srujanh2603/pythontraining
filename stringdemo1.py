str=input("Enter String ")
print(str)
print(len(str))
print(str.upper())
s=str.upper()
l=str.lower()
print(s, l)
print(s.isupper())

print("Capitalization",str.capitalize())
print("Capitalized every word:",str.title())

substring=input("Enter Substring ")
print("Occurences of",substring,"in the string",str.count(substring))

prefix=input("Enter a prefix to check if the string starts with it:")
print("Starts with",prefix,":",str.startswith(prefix))

suffix=input("Enter a suffix to check if the string ends with it:")
print("Ends with",suffix,":",str.endswith(suffix))

old_substring=input("Enter a substring to replace:")
new_substring=input("Enter a substring:")
print("After replacement: ",str.replace(old_substring,new_substring))

delimiter=input("Enter a delimiter to split the string: ")
print("Split string: ",str.split(delimiter))

substrings=input("ENter substrings to join(separated by space):").split()
join_delimiter=input("Enter delimiter to join the substrings:")
print("Joined String:",join_delimiter.join(substrings))

print(str.strip())
print(str.rfind('l'))
print(str.rindex('l'))

