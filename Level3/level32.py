#prepare for bunnies escapes
def solution(map):
    # Your code here
    d = (len(map) - 1, len(map[0]) - 1)
    v = set()
    q = [[True, 1, (0, 0)]]
    while q:
        e = q.pop(0)
        r, s, n = e[0], e[1], e[2]
        if (r, n) in v:
            continue
        v.add((r, n))
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = n[0] + dy, n[1] + dx
            if 0 <= ny <= d[0] and 0 <= nx <= d[1]:
                if (ny, nx) == d:
                    return s + 1
                elif map[ny][nx] == 0:
                    q += [[r, s + 1, (ny, nx)]]
                elif r:
                    q += [[False, s + 1, (ny, nx)]]
        q = sorted(q, key=lambda x: x[1] + d[0] - x[2][0] + d[1] - x[2][1] + 1) 

arr = [[0 for i in range(4)] for j in range(4)]
arr[0][1] = 1
arr[0][2] = 1
arr[1][3] = 1
arr[2][0] = 1
arr[2][1] = 1
arr[3][0] = 1
arr[3][1] = 1
arr[3][2] = 1
a = solution(arr)
print("ans is: ",a)
for r in arr:
    print(r)


'''
def solution(map):
    # Your code here
    door = (len(map) - 1, len(map[0]) - 1)
    visited = set()
    queue = [[True, 1, (0, 0)]]
    while queue:
        e = queue.pop(0)
        removal, steps, node = e[0], e[1], e[2]
        if (removal, node) in visited:
            continue
        visited.add((removal, node))
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = node[0] + dy, node[1] + dx
            if 0 <= ny <= door[0] and 0 <= nx <= door[1]:
                if (ny, nx) == door:
                    return steps + 1
                elif map[ny][nx] == 0:
                    queue += [[removal, steps + 1, (ny, nx)]]
                elif removal:
                    queue += [[False, steps + 1, (ny, nx)]]
        queue = sorted(queue, key=lambda x: x[1] + door[0] - x[2][0] + door[1] - x[2][1] + 1)
'''