def approximate_pi(n_terms):
    #pass replace pass with your code
    list_of_numbers = []
    x = []
    for i in range(n_terms):
        list_of_numbers.append(i)
    for i in list_of_numbers:
        x.append (((-1) ** i)/(2*i + 1))
    pi1 = 0
    for i in x:
        pi1 += i
    pi = 4*pi1
    print (pi)


approximate_pi(100)
