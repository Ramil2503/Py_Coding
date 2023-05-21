n, m, k = map(int, input("Enter dimensions of chocolate (n m) and number of slices to break off (k): ").split())

if (k % n == 0 and k <= n * m) or (k % m == 0 and k <= n * m):
    print("yes")
else:
    print("no")
