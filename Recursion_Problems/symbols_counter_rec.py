def symbols_count(str_arr):
    if len(str_arr)== 0:
        return 0
    
    def inner_count(in_str):
        if len(in_str)== 0:
            return 0
        else:
            return 1+ inner_count(in_str[1:len(in_str)])

    total_sym_counter= 0
    for string in str_arr:
        total_sym_counter += inner_count(string)
    
    return total_sym_counter

def main():
    test_list=["ab", "c", "def", "ghij", "abcde"]
    res= symbols_count(test_list)
    
    print("Number of symbols: {0}".format(res))
    
if __name__== "__main__":
    main()
