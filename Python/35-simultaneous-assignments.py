def swap(x, y):
    x, y = y, x
    return x, y

print(swap(3, 5))


def main():
    x, y, z = 2, 4, 5

    q, *w, e = [2, 4, 5, 6, 8, 23, 423, 234]

    print("x= ",x,"\ny=",y,"\nz= ",z,"\nq= ",q,"\nw= ",w,"\ne= ",e)

main()