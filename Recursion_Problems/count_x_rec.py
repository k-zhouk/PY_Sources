def count_x(string):
    if len(string)==0:
        return 0

    if string[0]=='x':
        return count_x(string[1:len(string)])+ 1
    else:
        return count_x(string[1:len(string)])
    
def main():
    test_str= "xxxaxbxcxxx"
    print(f"Test string: {test_str}")
    res= count_x(test_str)
    print(f"Number of \"x\"s: {res}")

if __name__ == "__main__":
    main()