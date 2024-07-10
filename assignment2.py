import textwrap

def wrap_text(string, maxwidth):
    return textwrap.fill(string, maxwidth)

string = input("Enter a string: ")
maxwidth = int(input("Enter a max width: "))
print(wrap_text(string, maxwidth))

