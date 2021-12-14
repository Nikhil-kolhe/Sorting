# Selection Sort :

def Selec_Sort(marks):
    for i in range(len(marks)):
        min_idx=i
        for j in range(i + 1, len(marks)):
            if marks[min_idx] > marks[j]:
                min_idx = j
        marks[i], marks[min_idx] = marks[min_idx], marks[i]

    print("Marks of students after performing Selection Sort : ")
    for i in range(len(marks)):
        print(marks[i])

# Bubble Sort :

def Bubble_Sort(marks):
    n=len(marks)
    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]

    print("Marks of students after performing Bubble Sort :")
    for i in range(len(marks)):
        print(marks[i])

# Top marks :

def top_five_marks(marks):
    print("Top",len(marks),"Marks are : ")
    print(*marks[::-1], sep="\n")


marks=[]
n = int(input("Enter number of students whose marks are to be displayed : "))
print("Enter marks for ",n," students: ")
for i in range(0, n):
    el=int(input())
    marks.append(el)
print("The marks of",n,"students are : \n",marks)


rev=1
while rev==1:
   
    print("\n1. Selection Sort of the marks")
    print("2. Bubble Sort of the marks")
    print("3. Exit")
    ch=int(input("\nEnter your choice (from 1 to 3) : "))

    if ch==1:
        Selec_Sort(marks)
        a=input("Do you want to display top marks from the list (yes/no) : ")
        if a=='yes':
            top_five_marks(marks)
        else:
            print("\n")
            rev=0

    elif ch==2:
        Bubble_Sort(marks)
        a=input("Do you want to display top five marks from the list (yes/no) : ")
        if a=='yes':
            top_five_marks(marks)
        else:
            print("\n")
            rev=0

    elif ch==3:
        print("\n")
        rev=0

    else:
        print("\ninvalid ")
        print("\n")
        rev=0