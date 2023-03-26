# hangrend, betű halmazok
hrend_magas = "eéiíöőüű"
hrend_mely = "aáoóuú"
db_magas = 0
db_mely = 0
ossz = 0
# program leírás
print("A program a bevitt szövegnek a hangrendjét (magas, mély, vegyes) állapítja meg. ")
# szöveg bevétel
txt = str.lower(input("Kérem a szöveget: "))

# megszámolyuk a hrend_magas-okat a txt-ben
for betu in txt:
    if betu in hrend_magas:
        db_magas += 1
    if betu in hrend_mely:
        db_mely += 1
if db_magas > 0 and db_mely == 0:
    print("Magas szórendű bevitel!")
elif db_mely > 0 and db_magas == 0:
    print("Mély szórendű bevitel!")
elif db_magas > 0 and db_mely > 0:
    print("Vegyes szórendű bevitel!")
else:
    print("Nincs benne magánhangzó!")

#email cím vizsgálat: Ha van @ karakter és egy "." (FH)
