def reverse_string(in_str):
    if len(in_str)==1:
        return in_str[0]
    return reverse_string(in_str[1: len(in_str)])+ in_str[0]

def main():
    test_str= "asdfghjkl"
    print(f"Test string to reverse: {test_str}")
    rev_str= reverse_string(test_str)
    print(f"Reversed string: {rev_str}")

if __name__ == "__main__":
    main()
