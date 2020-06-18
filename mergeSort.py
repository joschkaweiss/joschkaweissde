# Erstelle zwei Subarrays von arr[]. 
# Erstes Subarray ist arr[l..m] 
# Zweites Subarray arr[m+1..r] 
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    # Erstelle temporäre Arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Kopiere die Daten in die temporären Arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # Packe die temporären Arrays zurück in arr[l..r] 
    i = 0     # Initialisierungsindex des ersten Subarrays 
    j = 0     # Initialisierungsindex des zweiten Subarrays
    k = l     # Initialisierungs Index des zusammengeführten Subarrays 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Wenn Elemente von L[] übrig sind, kopiere diese 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Wenn Elemente von R[] übrig sind, kopiere diese
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
# l ist für den linken Index und r ist für den rechten Index 
# des Subarrays von arr 
def mergeSort(arr,l,r): 
    if l < r: 
  
        # Dasselbe wie (l+r)//2 aber verhindert Stack Overflow für L und R
        
        m = (l+(r-1))//2
  
        # Sortiere erste und zweite Hälften 
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 
  
  
# Test von Merge Sort
arr = [420, 23, 69, 81, 333] 
n = len(arr) 
print ("Gegebenes Array: ") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
mergeSort(arr,0,n-1) 
print ("\n\nSortierte Permutation: ") 
for i in range(n): 
    print ("%d" %arr[i]),
