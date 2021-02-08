def max_frequency(x):
    for i in x:
        n=0
        for j in x:
            if i == j :
                n += 1
                print("la lettera",i,"é ripetuta", n, "volte nella parola")
x= input("inserisci una parola:")
print(max_frequency(x))
