import time
import hashlib
#name2 = [["J","A","C","O","B","Y","E","E"], ["j", "a", "c", "o", "b", "y","e","e"]]
#list1 = ""
#name3 = [["J","A","K","E","K","Y","E","E"], ["j", "a", "k", "e", "k", "y","e","e"]]
#list2 = ""
#name4 = [["J","A","K","E","Y","E","E"],["j", "a", "k", "e", "y","e","e"]]
#list3 = ""


oneletter =[["J"],["j"]]
twoletter = [["J", "A"], ["j", "a"]]
threeletter1 = [["J", "A", "C"], ["j", "a", "c"]]
threeletter2 = [["J", "A", "K"], ["j", "a", "k"]]
fourletter1 = [["J", "A", "C", "O"], ["j", "a", "c", "o"]]
fourletter2 = [["J", "A", "K", "E"], ["j", "a", "k", "e"]]
fiveletter1 = [["J", "A", "C", "O", "B"], ["j", "a", "c", "o", "b"]]
fiveletter2 = [["J", "A", "K", "E", "K"], ["j", "a", "k", "e", "k"]]
fiveletter3 = [["J", "A", "K", "E", "Y"], ["j", "a", "k", "e", "y"]]
sixletter1 = [["J","A","C","O","B","Y"], ["j", "a", "c", "o", "b", "y"]]
sixletter2 = [["J","A","K","E","K","Y"], ["j", "a", "k", "e", "k", "y"]]
sixletter3 = [["J","A","K","E","Y","E"],["j", "a", "k", "e", "y","e"]]

list1 =""
list2 = ""
list3 = ""
list4 = ""
list5 = ""
list6 = ""

for a in range(2):
    tempname = oneletter[a][0]
    tempname = tempname.encode('utf-8')
    tempname = tempname.hex()
    list1 = list1 + "'" + tempname + "'" + ", "

for a in range(2):
    for b in range(2):
        tempname = twoletter[a][0] + twoletter[b][1]
        tempname = tempname.encode('utf-8')
        tempname = tempname.hex()
        list2 = list2 + "'" + tempname + "'" + ", "

for a in range(2):
    for b in range(2):
        for c in range(2):
            tempname = threeletter1[a][0] + threeletter1[b][1] + threeletter1[c][2]
            tempname = tempname.encode('utf-8')
            tempname = tempname.hex()
            list3 = list3 + "'" + tempname + "'" + ", "
            tempname = threeletter2[a][0] + threeletter2[b][1] + threeletter2[c][2]
            tempname = tempname.encode('utf-8')
            tempname = tempname.hex()
            list3 = list3 + "'" + tempname + "'" + ", "

for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                tempname = fourletter1[a][0] + fourletter1[b][1] + fourletter1[c][2] + fourletter1[d][3]
                tempname = tempname.encode('utf-8')
                tempname = tempname.hex()
                list4 = list4 + "'" + tempname + "'" + ", "
                tempname = fourletter2[a][0] + fourletter2[b][1] + fourletter2[c][2] + fourletter2[d][3]
                tempname = tempname.encode('utf-8')
                tempname = tempname.hex()
                list4 = list4 + "'" + tempname + "'" + ", "

for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    tempname = fiveletter1[a][0] + fiveletter1[b][1] + fiveletter1[c][2] + fiveletter1[d][3] +fiveletter1[e][4]
                    tempname = tempname.encode('utf-8')
                    tempname = tempname.hex()
                    list5 = list5 + "'" + tempname + "'" + ", "
                    tempname = fiveletter2[a][0] + fiveletter2[b][1] + fiveletter2[c][2] + fiveletter2[d][3] +fiveletter2[e][4]
                    tempname = tempname.encode('utf-8')
                    tempname = tempname.hex()
                    list5 = list5 + "'" + tempname + "'" + ", "
                    tempname = fiveletter3[a][0] + fiveletter3[b][1] + fiveletter3[c][2] + fiveletter3[d][3] +fiveletter3[e][4]
                    tempname = tempname.encode('utf-8')
                    tempname = tempname.hex()
                    list5 = list5 + "'" + tempname + "'" + ", "


for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        tempname = sixletter1[a][0] + sixletter1[b][1] + sixletter1[c][2] + sixletter1[d][3] + sixletter1[e][4] + sixletter1[f][5]
                        tempname = tempname.encode('utf-8')
                        tempname = tempname.hex()
                        list6 = list6 + "'" + tempname + "'" + ", "
                        tempname = sixletter2[a][0] + sixletter2[b][1] + sixletter2[c][2] + sixletter2[d][3] + sixletter2[e][4] + sixletter2[f][5]
                        tempname = tempname.encode('utf-8')
                        tempname = tempname.hex()
                        list6 = list6 + "'" + tempname + "'" + ", "
                        tempname = sixletter3[a][0] + sixletter3[b][1] + sixletter3[c][2] + sixletter3[d][3] + sixletter3[e][4] + sixletter3[f][5]
                        tempname = tempname.encode('utf-8')
                        tempname = tempname.hex()
                        list6 = list6 + "'" + tempname + "'" + ", "



#Adding quotation marks changes the characters in the file to chinese ones. 
list1.encode('utf8')
print(list1)
print("/////////////////////////////////////////////////////////////////////")
list2.encode('utf8')
print(list2)
print("/////////////////////////////////////////////////////////////////////")
list3.encode('utf8')
print(list3)
print("/////////////////////////////////////////////////////////////////////")
list4.encode('utf8')
print(list4)
print("/////////////////////////////////////////////////////////////////////")
list5.encode('utf8')
print(list5)
print("/////////////////////////////////////////////////////////////////////")
list6.encode('utf8')
print(list6)

f = open("searchforhexname.txt", "w")
f.write(list1)
f.write(list2)
f.write(list3)
f.write(list4)
f.write(list5)
f.write(list6)


f.close()
f = open("searchforhexname.txt", "r")
print(f.read())

