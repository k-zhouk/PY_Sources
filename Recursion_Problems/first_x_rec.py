def get_first_x(string):
    if len(string)==0:
        return 0

    if string[0]=='x':
        return 0
    else:
        return get_first_x(string[1:len(string)])+ 1
    
def main():
    test_str= "abcdexfghijklmnopqrstuvwxyz"
    print(f"Test string: {test_str}")
    index= get_first_x(test_str)
    print(f"Number of \"x\"s: {index}")

if __name__ == "__main__":
    main()
