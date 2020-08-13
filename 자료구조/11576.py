A, B = map(int, input().split())
m = int(input())
N = list(map(int, input().split()))
dec, cnt = 0, 0
ans = []
for c in N[::-1]:
    dec += c * (A ** cnt)
    cnt += 1
while dec:
    ans.append(str(dec % B))
    dec = dec // B
print(' '.join(ans[::-1]))
