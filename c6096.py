p = []

for i in range(20) :
  p.append([])
  for j in range(20) :
    p[i].append(0)

for i in range(19) :
  a = input().split()
  for j in range(19) :
    p[i+1][j+1] = int(a[j])

n = int(input())
for i in range(n) :
  x, y = map(int, input().split())
  for j in range(1, 20) :
    if p[j][y] == 0 :
      p[j][y] = 1
    else :
      p[j][y] = 0

    if p[x][j] == 0 :
      p[x][j] = 1
    else :
      p[x][j] = 0

for i in range(1, 20) :
  for j in range(1, 20) :
    print(p[i][j], end = ' ')
  print()