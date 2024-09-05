def merge_sorted_arrays(A: list[int], B: list[int]) -> list[int]:
    res = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
    if i < len(A):
        res.extend(A[i:])  # Use extend to append the rest of A
    else:
        res.extend(B[j:])  # Use extend to append the rest of B
    return res
    
A = [1, 1, 5]
B = [1, 1, 6]
result = merge_sorted_arrays(A, B)
print(result)
