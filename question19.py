rows = 5
for i in range(1, rows + 1):
    aa = ""
    for _ in range(rows - i):
        aa += "  "
    for _ in range(i):
        aa  += "* "
    print(aa.strip())