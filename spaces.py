def spaces(n,y,t):
    Shared_Occupied_Spaces = 0
    for i in range(n):
        if y[i] == "C" and t[i] == "C":
            Shared_Occupied_Spaces = Shared_Occupied_Spaces + 1
    print(n)
    print(y)
    print(t)
    print(Shared_Occupied_Spaces)

spaces(3,"C.C","CC.")