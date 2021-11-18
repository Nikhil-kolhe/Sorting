import array as arr

def accept_perc():
    a = arr.array('f', [])
    no_stud = int(input("Enter the number of Students : "))
    for i in range(0, no_stud):
        a.append(float(input("Enter percentage : ".format(i))))
    return a

def print_perc(a):
    for i in range(0, len(a)):
        print("\t {0:.2f}".format(a[i]), end=" ")
    print()

def shell_sort(a):
    n = len(a)
    gap = n // 2
    
    while gap > 0:

        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2
    return a


def ins_sort(a):
    
    for i in range(1, len(a)):

        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a



def top_five(a):
    print("Top five score are : ")
    cnt = len(a)

    if cnt < 5:
        start, stop = cnt - 1, -1  
    else:
        start, stop = cnt - 1, cnt - 6

    for i in range(start, stop, -1):
        print("\t {0:.2f}".format(a[i]), end=" ")

if __name__ == "__main__":

    unsort_A = arr.array('f', [])
    ins_sort_A = arr.array('f', [])
    shell_sort_A = arr.array('f', [])
    flag = 1

    while flag == 1:
        print("\n 1. Accept array elements \n 2. Display the Elements \n 3. Insertion Sort \n 4. Shell Sort \n 5. exit")
        choice = int(input("Enter your choice : "))

        if choice == 1:
            unsort_A = accept_perc()

        elif choice == 2:
            print_perc(unsort_A)

        elif choice == 3:
            print("Elements after sorting using Insertion Sort :")
            ins_sort_A = ins_sort(unsort_A)
            print_perc(ins_sort_A)
           

        elif choice == 4:
            print("Elements after sorting using Shell Sort :")
            shell_sort_A = shell_sort(unsort_A)
            print_perc(shell_sort_A)
           

        else:
            print("Wrong choice")
            flag = 0

