letters = ['a', 'b', 'c', 'd', 'e', 'i', 'j', 'o', 'u']
letters_tuple = ('a', 'b', 'c', 'd', 'e', 'i', 'j', 'o', 'u')
letters_set = {'a', 'b', 'c', 'd', 'e', 'i', 'j', 'o', 'u'}


# filter the vowels from above list -> a,e,i,o,u

def filter_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels


result_vowels = filter(filter_vowel, letters)
print(list(result_vowels))
