def golomb(n):
    print("Iteration")
    if n== 1:
        return 1
    
    return 1+ golomb(n-golomb(golomb(n -1)))

def main():
    n= 9
    gol_num= golomb(n)
    print("\n{0}th Golom number: {1}\n".format(n, gol_num))

if __name__== "__main__":
    main()
