import sys

li1 = []
for line in sys.stdin:
    li1.append(line.rstrip())
li1.sort(key=len)
li = []
first = li1[0]
if len(first) != 1:
    for n in range(len(li1)):
        if len(first) < len(li1[n]):
            li.append(li1[n])
        else:
            li.append(first)
            first = li1[n]
    for i in range(len(first), 0, -1):
        for p in range(len(first) - i):
          #  if p == 0:
           #     substr = first[:i]
            #else:
            substr = first[p:p + i - 1]
            print(substr)
            is_found = True
            for j in range(len(li)):
                if substr in li[j]:
                    if li[j].index(substr) >= 0:
                        continue
                    else:
                        is_found = False
                        break
                else:
                    is_found = False
                    break
            if is_found:
                print(substr)
                sys.exit(0)
else:
    print(first)