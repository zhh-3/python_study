for i in range(9):
    for j in range(i+1):
        print(i+1, "*", j+1, "=", (1+i)*(1+j), end="\t")
    print()