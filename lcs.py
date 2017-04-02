import csv 
import pandas as pd
from tabulate import tabulate 
#Function to return the length of the longest common subsequence for two strings and the longest common subsequence itself.
def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0 for x in xrange(n+1)] for x in xrange(m+1)]
    for i in xrange(1, m+1):
        for j in xrange(1, n+1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
 
    index = L[m][n]
    lcs = [""] * (index+1)
    lcs[index] = "\0"
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i-=1
            j-=1
            index-=1
        elif L[i-1][j] > L[i][j-1]:
            i-=1
        else:
            j-=1
    return (L[m][n],''.join(lcs))


listofstrings = [(0,'TTCTACGGGGGGAGACCTTTACGAATCACACCGGTCTTCTTTGTTCTAGCCGCTCTTTTTCATCAGTTGCAGCTAGTGCATAATTGCTCACAAACGTATC'), 
                (1,'TCTACGGGGGGCGTCATTACGGAATCCACACAGGTCGTTATGTTCATCTGTCTCTTTTCACAGTTGCGGCTTGTGCATAATGCTCACGAACGTATC'), 
                (2,'TCTACGGGGGGCGTCTATTACGTCGCCAACAGGTCGTATGTTCATTGTCATCATTTTCATAGTTGCGGCCTGTGCGTGCTTACGAACGTATTCC'), 
                (3,'TCCTAACGGGTAGTGTCATACGGAATCGACACGAGGTCGTATCTTCAATTGTCTCTTCACAGTTGCGGCTGTCCATAAACGCGTCCCGAACGTTATG'), 
                (4,'TATCAGTAGGGCATACTTGTACGACATTCCCCGGATAGCCACTTTTTTCCTACCCGTCTCTTTTTCTGACCCGTTCCAGCTGATAAGTCTGATGACTC'), 
                (5,'TAATCTATAGCATACTTTACGAACTACCCCGGTCCACGTTTTTCCTCGTCTTCTTTCGCTCGATAGCCATGGTAACTTCTACAAAGTTC'), 
                (6,'TATCATAGGGCATACTTTTACGAACTCCCCGGTGCACTTTTTTCCTACCGCTCTTTTTCGACTCGTTGCAGCCATGATAACTGCTACAAACTTC')]
#Draw a table of all the longest common subsequences for all pairs of strings
'''
results = []
index1 = []
index2 = []
for m in range (0,7):
    for n in range (m+1, 7):
        index1.append(m)
        index2.append(n)
        this_result = lcs(listofstrings[m][1], listofstrings[n][1])
        results.append(this_result)
lengths = []
strings = []
for l in results:
    this_length = l[0]
    this_string = l[1]
    lengths.append(this_length)
    strings.append(this_string)
raw_data = {'Index1': index1, 'Index2': index2, 'Length': lengths, 'String': strings}
df = pd.DataFrame(raw_data, columns = ['Index1','Index2','Length','String'])
df.to_csv('grades.csv')
#Draw a table of lengths of the longest common subsequences for all pairs of strings
table = BeautifulTable()
table.column_headers 
for x in range(0,7):
    this_row = []
    for y in range(0,7):
        this_len = lcs(listofstrings[x][1],listofstrings[y][1])
        this_row.append(this_len)
    table.append_row(this_row)
print table
'''
def lcs3(X, Y, Z):
    m = len(X)
    l = len(Y)
    n = len(Z)
    subs = [[[0 for k in range(n+1)] for j in range(l+1)] for i in range(m+1)]

    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            for k, z in enumerate(Z):
                if x == y and y == z:
                    subs[i+1][j+1][k+1] = subs[i][j][k] + 1
                else:
                    subs[i+1][j+1][k+1] = max(subs[i+1][j+1][k], 
                                              subs[i][j+1][k+1], 
                                              subs[i+1][j][k+1])
    # return subs[-1][-1][-1] #if you only need the length of the lcs
    lcs = ""
    while m > 0 and l > 0 and n > 0:
        step = subs[m][l][n]
        if step == subs[m-1][l][n]:
            m -= 1
        elif step == subs[m][l-1][n]:
            l -= 1
        elif step == subs[m][l][n-1]:
            n -= 1
        else:
            lcs += str(X[m-1])
            m -= 1
            l -= 1
            n -= 1

    return lcs[::-1]
print lcs3(listofstrings[0][1], listofstrings[1][1], listofstrings[2][1])

