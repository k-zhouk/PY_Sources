def golomb(n):
    print("Iteration")
    if n== 1:
        return 1
    
    return 1+ golomb(n-golomb(golomb(n -1)))

def golomb_memo(n, cache):
    print("Iteration")
    if n== 1:
        return 1
    
    if n not in cache:
        cache[n]= 1+ golomb_memo(n-golomb_memo(golomb_memo(n -1, cache), cache), cache)
    return cache[n]

def main():
    n= 9
    #gol_num= golomb(n)
    gol_num= golomb_memo(n, {})
    print("\n{0}th Golom number: {1}\n".format(n, gol_num))

if __name__== "__main__":
    main()
