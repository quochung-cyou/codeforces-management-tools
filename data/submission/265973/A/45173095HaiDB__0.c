<<<<<<< Updated upstream
dulieu = input()
kt = dulieu.split()
n = int(kt[0])
k = int(kt[1])
dulieu = input()
kt = dulieu.split()
i = 0
while(i < len(kt)):
    kt[i] = int(kt[i])
    i = i+1

print(kt)
i = 0
dem = 0
while(i < len(kt)):
    j = i
    t = 0
    while(j < len(kt)):
        t = t + kt[j]
        if(t % k == 0):
            dem = dem+1
        j = j+1
=======
dulieu = input()
kt = dulieu.split()
n = int(kt[0])
k = int(kt[1])
dulieu = input()
kt = dulieu.split()
i = 0
while(i < len(kt)):
    kt[i] = int(kt[i])
    i = i+1

print(kt)
i = 0
dem = 0
while(i < len(kt)):
    j = i
    t = 0
    while(j < len(kt)):
        t = t + kt[j]
        if(t % k == 0):
            dem = dem+1
        j = j+1
>>>>>>> Stashed changes
    i = i+1