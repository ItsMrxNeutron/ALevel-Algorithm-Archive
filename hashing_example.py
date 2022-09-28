



def hash(x:str) -> int:         # a simple hashing function (this may cause collision)
    sum_ascii = 0
    for i in x:
        sum_ascii += ord(i)     # sum of all ASCII values
    return sum_ascii % 11       # mods 11 to return a value between 1 - 11


