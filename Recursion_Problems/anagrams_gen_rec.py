def anagrams(in_str, counter= 0):
    # List to store generated words at each step
    words= []

    # If the length of the input string is 1, then just return this string
    if len(in_str)==1:
        return in_str

    # List of substrings to store generated words in the "words" list
    substrings= anagrams(in_str[1:len(in_str)])

    # We take each string from the list of substrings, generate new words by inserting a first symbol
    # from the input string at every position of a substring and populate the "words" list
    # which at the next step will be return to the "substrings" list
    for string in substrings:
        # Symbol that's inserted in every substring
        sym= in_str[0]
        for i in range(len(string)+1):
            new_word= string[0:i]+ sym+ string[i:len(in_str)]
            words.append(new_word)

    return words

def main():
    anagr_test_str="abcdefghi"
    res= anagrams(anagr_test_str)
    print(f"Anagrams:")
    # print(res)
    print(f"\nThere are total {len(res)} anagrams")

if __name__ == "__main__":
    main()
