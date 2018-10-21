from heapq import heapify, heappop, heappush

File = open('puretext.txt')
a = [ tuple(x.strip().split()) for x in File.readlines()]

print(a)

heap = [[int(wt), [sym, ""]] for sym, wt in a]

heapify(heap)
while len(heap) > 1:
    lo = heappop(heap)
    hi = heappop(heap)
    for pair in lo[1:]:
        pair[1] = '0' + pair[1]
    for pair in hi[1:]:
        pair[1] = '1' + pair[1]
    print("LO ",lo[0])
    heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    print(heap)

# print(heap)

a = [1,2]
b = [3,4]
print(a+b)