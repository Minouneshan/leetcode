
def run(s :str, numRows:int):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    n = numRows
    dic = {}
    for i in range(n):
        dic[i] = []
    while len(s) > 0:
        if n > 1:
            for i in range(2*n-2):
                if len(s) > 0:
                    if i < n-1:
                        dic[i] += s[0]
                        s = s[1:]
                    else:
                        dic[2*n-i-2] += s[0]
                        s = s[1:]
        else:
            for i in range(len(s)):
                dic[0] += s[0]
                s = s[1:]
    c = ''
    for i in dic:
        for j in dic[i]:
            c += j
    return c                  