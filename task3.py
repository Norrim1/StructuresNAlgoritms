def recursive_poly(word, left=0, right=None):
    if right is None:
        right = len(word) - 1
    if left >= right:
        return "YES" #Базовый
    if word[left] != word[right]:
        return "NO" #Базовый
    return recursive_poly(word, left + 1, right - 1) #Рекурсивный

print(recursive_poly("AvavAs"))