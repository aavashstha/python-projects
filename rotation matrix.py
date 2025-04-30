


def rotate_matrix():
    
    #asking for values
    print("Enter the value of the variables such that the 2x2 matrix is: [a  b]") 
    print("                                                              [c  d]")

    while True:
        a = input("Enter the value of a: ")
        if a.isdigit():
            a = int(a)
            break
        else:
            print("INVALID INPUT! Please enter a valid number!")
            continue

    while True:
        b = input("Enter the value of b: ")
        if b.isdigit():
            b = int(b)
            break
        else:
            print("INVALID INPUT! Please enter a valid number!")
            continue

    while True:
        c = input("Enter the value of c: ")
        if c.isdigit():
            c = int(c)
            break
        else:
            print("INVALID INPUT! Please enter a valid number!")
            continue

    while True:
        d = input("Enter the value of d: ")
        if d.isdigit():
            d = int(d)
            break
        else:
            print("INVALID INPUT! Please enter a valid number!")
            continue

    
    #calculations

    image_a = (a * 0) + (b * (-1))
    image_b = (a * 1) + (b * 0)
    image_c = (c * 0) + (d * (-1))
    image_d = (c * 1) + (d * 0)


    #results

    print()
    print("---------- RESULTS ----------")
    print(f"The matrix [{a} {b}] when rotated to 90° is: [{image_a} {image_b}]")
    print(f"           [{c} {d}]                         [{image_c} {image_d}]")


rotate_matrix()