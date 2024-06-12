s={'apple','banana','cherry'}
s.add("orange")
print(s)

tropical={'pineapple','watermelon'}
s.update(tropical)
print(s)

def power_set(s):
    result=[[]]
    for element in s:
        result.extend([subset+[element] for subset in result])
    return [set(subset) for subset in result]

input_set={1,2,3}
powerset=power_set(input_set)
print(powerset)