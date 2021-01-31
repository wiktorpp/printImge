data = """
000a000a
ffffff00ffffff00ffffff0000ffff0000ffff0000ffff0000ffff00ffffff00ffffff00ffffff00
ffffff00ffffff0000ffff00ffffff00ffffff00ffffff00ffffff0000ffff00ffffff00ffffff00
ffffff0000ffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff0000ffff00ffffff00
00ffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff0000ffff00
00ffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff0000ffff00
00ffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff0000ffff00
00ffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff0000ffff00
ffffff0000ffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff0000ffff00ffffff00
ffffff00ffffff0000ffff00ffffff00ffffff00ffffff00ffffff0000ffff00ffffff00ffffff00
ffffff00ffffff00ffffff0000ffff0000ffff0000ffff0000ffff00ffffff00ffffff00ffffff00

""".replace("\n", "")
transparencyMaskStr = """
1110000111
1100000011
1000000001
0000000000
0000000000
0000000000
0000000000
1000000001
1100000011
1110000111

"""[1:-1].splitlines()
transparencyMask = []
for i in range(len(transparencyMaskStr)):
    transparencyMask.append([])
    for j in range(len(transparencyMaskStr[0])):
        transparencyMask[i].append(
            bool(int(transparencyMaskStr[i][j]))
        )