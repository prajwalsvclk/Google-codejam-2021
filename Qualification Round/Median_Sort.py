from sys import stdout

def query(i, j, k):
    print i, j, k
    stdout.flush()
    return input()

def check(result):
    print " ".join(map(str, result))
    stdout.flush()
    ok = raw_input().strip()
    if ok != "1":  # error
        exit()

def median_sort():
    result = [1, 2]
    for i in xrange(3, N+1):  # Time: O(N)
        left, right = 0, len(result)-1
        while right-left >= 1:  # Time: O(logN)
            m1 = left + (right-left)//3
            m2 = right - (right-left)//3
            x = query(result[m1], result[m2], i)
            if x == result[m1]:
                right = m1-1
                if left == right:  # padded for the last query 
                    right += 1
            elif x == result[m2]:
                left = m2+1
                if left == right:  # padded for the last query 
                    left -= 1
            else:
                left, right = m1+1, m2-1
                if left == right:  # padded for the last query 
                    left -= 1                
        result.insert(left, i)  # Time: O(N)
    check(result)

T, N, Q = map(int, raw_input().strip().split())
for case in xrange(T):
    median_sort()
