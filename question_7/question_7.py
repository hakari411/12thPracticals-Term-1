poem = open('./POEM.txt','r').read()
#Frequency of all vowels
def count_vowels(poem):
    vowels = {'A':0,'E':0,'I':0,'O':0,'U':0}
    p = poem.upper()
    for i in p:
        if i in vowels:
            vowels[i] += 1
    res = [ (str(key),str(value))for key,value in vowels.items()]
    res = [ '-'.join(i) for i in res ]
    return '\t'.join(res)
#count upper and lower
def count_upper_lower(poem):
    upper_t = 0
    lower_t = 0
    for i in poem:
        if i.isupper():
            upper_t+=1
        elif i.islower():
            lower_t += 1
    return f"Total number of uppercase characters: {upper_t}\nTotal Number of lower case characters: {lower_t}"
