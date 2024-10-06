# Fibonacic number calculation with memoization
def get_fib_num(n, cache):
    if n== 0 or n== 1:
        return n

    if n not in cache:
        cache[n]= get_fib_num(n- 1, cache)+ get_fib_num(n- 2, cache)

    return cache[n]

def main():
    n= 10
    fib_num= get_fib_num(n, {})
    print("\n{0}th Fibbonaci number is {1}\n".format(n, fib_num))

if __name__== "__main__":
    main()
