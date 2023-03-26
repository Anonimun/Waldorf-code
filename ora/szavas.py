#minden magánhangzó legyen "*".

szoveg = input("Bevitelt kérem: ")

maganh = "aouie"

# for i in maganh:
#     szoveg=szoveg.replace(i, "*")
# print(szoveg)
for i in szoveg:
    if i in maganh:
        szoveg=szoveg.replace(i,"*")
print(szoveg)