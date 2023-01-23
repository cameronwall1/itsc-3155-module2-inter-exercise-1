
# -------------------------------------------------------------
# First exercise of Intermediate Python Exercises 1

def uniqueElements () :
    x = 0
    my_list = []
    unique_list = []
    print ("Enter seven integers")
    while (x < 7) :
        my_list.append(input(str(x + 1) + ". "))
        x+=1

    for i in my_list :
        if (unique_list.__contains__(i)) :
            print ("", end = "")
        else :
            unique_list.append(i)

    print (my_list)
    print (unique_list)

# uniqueElements()