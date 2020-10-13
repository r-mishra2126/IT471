import string
file=open('dictfile.txt')
counts=dict()
for line in file:
    #line=line.translate(string.punctuation)
    line=line.lower()
    words=line.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1

lst=list()
for key, val in counts.items():
    lst.append((val,key))
lst.sort(reverse=True)
for key,val in lst[:10]:
    print((key,val))
