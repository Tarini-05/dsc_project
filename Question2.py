def remove_duplicates(arr):
    return list(dict.fromkeys(arr))
arr = list(map(int, input("Enter the sorted array elements separated by spaces: ").split()))
result = remove_duplicates(arr)
print(result)
