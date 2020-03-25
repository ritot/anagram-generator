import time
import profile


def get_anagram(my_word, min_len):

    def get_fits(word):
        fits = set()
        replace = str.replace

        for n in dictionary:
            temp = word
            for l in n:
                if l in temp:
                    temp = replace(temp, l, "", 1)
                else:
                    break
            else:
                fits.add((n, temp))

        return sorted(fits)

    def add_anagrams(word, chain, prev):
        for fit, remainder in get_fits(word):
            if not chain:
                dictionary.remove(prev)
                prev = fit

            chain.append(fit)

            if len("".join(chain)) == length and chain == sorted(chain):
                anagrams.add(tuple(chain))

            add_anagrams(remainder, chain, prev)
        else:
            try:
                del chain[-1]
            except IndexError:
                pass

    f = open("dictionary.txt")
    #f = open("word_list_english_uppercase_spell_checked.txt")
    # Torsten Brischalle (http://www.aaabbb.de/WordList/WordList_en.php)
    strip = str.strip
    dictionary = {strip(w) for w in f.readlines()}
    f.close()

    my_word = my_word.replace(" ", "").upper()

    if my_word in dictionary:
        dictionary.remove(my_word)

    dictionary = [x[0] for x in get_fits(my_word)]

    print()
    print(len(dictionary), "unique words fit into", my_word + ":")
    dictionary.sort(key=len)
    print(dictionary)
    print()

    if min_len != "":
        min_len = int(min_len)
        at_least = [x for x in dictionary if len(x) >= min_len]
        print(len(at_least), "unique words that contain at least", min_len, "letters fit into", my_word + ":")
        print(at_least)
        print()

    dictionary.sort(key=len)
    dictionary.append("?")

    length = len(my_word)

    anagrams = set()

    add_anagrams(my_word, [], "?")

    print(len(anagrams), "unique anagrams from", my_word + ":")

    anagrams = sorted(anagrams)
    print("Sorted alphabetically")
    print(anagrams)
    print()

    anagrams.sort(key=len)
    print("Sorted by number of words")
    print(anagrams)
    print()


user_input = input("Word: ")
min_len_input = input("Minimum number of letters to create word (optional): ")
start_time = time.time()
get_anagram(user_input, min_len_input)
stop_time = time.time()
print("This program took", round(stop_time - start_time, 2), "seconds to run")
