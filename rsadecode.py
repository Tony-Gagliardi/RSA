#! /usr/bin/python

def computePow (m,n,e): 
    """ The idea is to compute m^e mod n """
    p = m # p will hold m^{2^j}
    r = 1 # r is the result
    while ( e > 0):
        if (e %2 == 1):
            r = (r * p)%n
        p = (p*p) % n
        e = e / 2
    return r %n


def encodeMessageString (s, n, e):
    """ Encode a string as a sequence of RSA numbers """
    l = list(s)
    l1 = map ( lambda c: ord(c), l)
    l2 = map ( lambda j: computePow(j,n,e), l1)
    return l2


def decodeMessageList (l, n, d):
    l = map( lambda j: computePow(j,n,d) % 256, l)
    l1 = map ( chr, l)
    s = ''.join(l1)
    return s


# if __name__ == "__main__":
#     import sys
#     l = encodeMessageString(str(sys.argv[1]),int(sys.argv[2]), int(sys.argv[3]))
#     print l

if __name__ == "__main__":
    import sys
    print 'Enter filename to decode:',
    encFile = raw_input()
    f1 = open (encFile,'r')
    dlist = []
    for line in f1:
        dlist.append(int(line))
    print '   >> OK! Encoded msg:', str(dlist)
    f1.close()
    print 'Enter key file: ',
    keyFile = raw_input()
    print '   >> I will read keys from: ', keyFile
    f = open(keyFile,'r')
    n = int(f.readline())
    e = int(f.readline())
    print '   >> n=',n,' d= ',e
    s = decodeMessageList(dlist,n,e)
    print '   >> decoded message: ', s
    
    
