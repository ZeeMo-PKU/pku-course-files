# N=int(input())
# for ia in range(2,N+1):
#     for ib in range(2,ia):
#         for ic in range(ib,ia):
#             for id in range(ic,ia):
#                 if ia**3==ib**3+ic**3+id**3:
#                     print(f'Cube = {ia}, Triple = ({ib},{ic},{id})')
mininum=0
def mergesort(arr):
    global mininum
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        Lptr = Rptr = ptr = 0
        while len(left) > Lptr and len(right) > Rptr:
            if left[Lptr] <= right[Rptr]:
                arr[ptr] = left[Lptr]
                Lptr += 1
            else:
                arr[ptr] = right[Rptr]
                Rptr += 1
                mininum += len(left) - Lptr
            ptr += 1

        while len(left) > Lptr:
            arr[ptr] = left[Lptr]
            ptr += 1
            Lptr += 1
        while len(right) > Rptr:
            arr[ptr] = right[Rptr]
            ptr += 1
            Rptr += 1


n = int(input())
arr = list(map(int, input().split()))
mergesort(arr)
print(mininum)