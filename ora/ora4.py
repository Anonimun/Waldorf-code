maganh = "aáeéuúoóöőüűií"
szov = input("kérem a szöveget: ")

for betu in maganh:
    szov = szov.replace(betu, betu + "f" + betu)

print(szov)
