def reverse_string(word: str) -> str:
    i = 0
    j = len(word) -1

    list_str = list(word)

    while i < j:
        list_str[i] , list_str[j] = list_str[j], list_str[i]
        i += 1
        j -= 1
    
    return "".join(list_str)


print(reverse_string("adfsag"))
