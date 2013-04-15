#coding: utf-8
data = []
uniq = []
for a in range(0,100):
    for b in range(0,100):
        for c in range(0,100):
            if a + b + c == 100:
                d = sorted([a,b,c])
                if d  not in uniq:
                    uniq.append(d)
                    data.append(d)
                else:
                    print "already"

print len(data)


