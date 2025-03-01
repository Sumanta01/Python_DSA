
def selection_sort(A, B, n):
    for i in range(n):
        min_index = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_index]:
                min_index = j

        A[i], A[min_index] = A[min_index], A[i]
        B[i], B[min_index] = B[min_index], B[i]

    return B



#A = [32, 4, 53, 2, 0, 18]
#B = [16, 11, 9, 3, 21, 36]
#n = 3

A=[91,4 ,37, 6 ,19 ,27 ,0 ,54, 11 ,16]
B=[43, 56, 35, 3 ,56 ,232 ,5, 6, 54 ,1]
n=6

sorted_B = selection_sort(A, B, n)
print(sorted_B)
