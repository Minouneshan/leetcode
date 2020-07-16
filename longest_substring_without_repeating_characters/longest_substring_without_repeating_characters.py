
def run(s: str) -> int:
    l = []
    maximum = 0
    count = 0 
    for i in range(len(s)):
        if  s[i] not in l:
            l.append(s[i])
            count += 1
            if count > maximum:
                maximum = count
        else:
            l = l[l.index(s[i])+1:]
            l.append(s[i])
            count = len(l)
    return maximum
