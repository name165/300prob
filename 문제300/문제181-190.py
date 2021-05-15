#181
apart = [["101호","102호"],["201호","202호"],["301호","302호"]]
#182
stock = [["시가",100,200,300],["종가",80,210,330]]
#183
stok = {"시가":[100,200,300],"종가":[80,210,330]}
#184
stock = {"10/10":[80, 110, 70, 90],"10/11":[210, 230, 190, 200]}
#185
apart = [[101,102],[201,202],[301,302]]
for i in apart:
    for j in i:
        print(j,end = ' 호 ')
    print()
print("-----------")

#186
apart = [[101,102],[201,202],[301,302]]
for i in apart[2::-1]:
    for j in i:
        print(j,end = ' 호\n')
print("-----------")

#187
apart = [[101,102],[201,202],[301,302]]
for i in apart[2::-1]:
    for j in i[::-1]:
        print(j,end = ' 호\n')
print("-----------")

#188
apart = [[101,102],[201,202],[301,302]]
for i in apart:
    for j in i:
        print(j,end = ' 호\n')
        print("-------")


#189
apart = [[101,102],[201,202],[301,302]]
for i in apart:
    for j in i:
        print(j,end = ' 호\n')
    print("-------")


#190
apart = [[101,102],[201,202],[301,302]]
for i in apart:
    for j in i:
        print(j,end = ' 호\n')
print("-------")
