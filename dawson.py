if __name__ == '__main__':
    import sys
    import re

    a = sys.stdin.readline().strip().split()
    s = []
    p1 = re.compile('[0-9]+[-][0-9]+')
    p2 = re.compile('[0-9]+[-][a-z]+')
    p3 = re.compile('[0-9]+[-][A-Z]+')
    p4 = re.compile('[a-z]+[-][0-9]+')
    p5 = re.compile('[a-z]+[-][a-z]+')
    p6 = re.compile('[a-z]+[-][A-Z]+')
    p7 = re.compile('[A-Z]+[-][A-Z]+')
    p8 = re.compile('[A-Z]+[-][0-9]+')
    p9 = re.compile('[A-Z]+[-][a-z]+')
    p9 = re.compile('[A-Z]+[-][a-z]+')

    for i in a:
        if i.isalpha():
            s.append(i)
        elif i.isdigit():
            s.append(i)
        elif re.search(p1, i) or re.search(p2, i) or re.search(p3, i) or re.search(p4, i) or re.search(p5,
                                                                                                       i) or re.search(
                p6, i) or re.search(p7, i) or re.search(p8, i) or re.search(p9, i):
            s.append(i)
        else:
            tmp = ''
            for j in i:
                if j.isalpha() or j.isdigit():
                    tmp += j
                else:
                    tmp += ' '
            if len(tmp) != 0:
                tmp = ' '.join([t for t in tmp.split() if t.isalpha() or t.isdigit()])
                s.append(tmp)
    s = ' '.join(reversed(s)).split()
    s = [i for i in s if i != ' ']
    print(' '.join(s))

