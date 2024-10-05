def get_triangle_num(n):
    if n== 1:
        return 1
    return n+ get_triangle_num(n-1)

def main():
    test_n= 36
    triangle_num= get_triangle_num(test_n)
    print("The {0}th traingle number is: {1}".format(test_n, triangle_num))

if __name__== "__main__":
    main()
