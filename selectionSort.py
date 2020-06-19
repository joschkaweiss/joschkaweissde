import sys

def selectionSort(A):

    for i in range(len(A)):

        minimum_index = i

        for j in range(i+1, len(A)):
            if A[minimum_index] > A[j]:
                min_idx = j

        A[i], A[minimum_index] = A[minimum_index], A[i]


