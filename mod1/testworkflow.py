## Paste the consecutive lines into one cell; the blank line means new cell.
## In Python, whitespace has meaning, so make sure you include the tabs and newlines

S = "STRING"
print (S[0:6])

ci = ord(S[5])
print (ci)
print (chr(ci + 1))

Y = list([0,2,6,3,1,7])
print (sum(Y))

Y[3] = 0
print (sum(Y))

cumsum = 0
for i in range(INTEGER):
    cumsum += i
    print (cumsum)

cumsum = 0
R = iter(range(5))
while True:
    try:
        i = next(R)
        cumsum += i
        print cumsum
    except StopIteration:
        break

