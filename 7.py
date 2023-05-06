


#Problem-7: Write a program to find a given 
# pattern from text using the first pattern matching algorithm
###### KMP Algorithm ##########
def PatternSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0] * M
    computeLPSarray(pat, M, lps)
    i = 0
    j = 0
    cnt=0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
        if j == M:
            print("Pattern found at position ",i - j)
            j = lps[j - 1]
            cnt += 1
    if cnt>0:
        print("Total pattern match : ", cnt)
    else:
        print("Pattern Not found")
def computeLPSarray(pat, M, lps):
    len = 0
    i = 1
    lps[0] = 0
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1
#main function
while True:
    print("\nPress 1 then go to pattern matching field.")
    print("Press 0 then exit.")
    press = int(input())
    if press==1 :
        txt = input("Enter the pattern field : ")
        pat = input("Enter the pattern : ")
        PatternSearch(pat, txt)
    else:
        print("Exit")
        break