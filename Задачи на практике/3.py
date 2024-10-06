def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    ind = len(arr) // 2
    left = merge_sort(arr[:ind])
    right = merge_sort(arr[ind:])
    return merge(left, right)

def merge(left, right):
    global inv
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            inv += len(left) - i
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

inv = 0
N = int(input())
ls = list(map(int, input().split()))
ls = merge_sort(ls)
print(inv)