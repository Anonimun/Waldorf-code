email = input("Kérem a vizsgálni kívánt címet: ")
db_1 = 0
db_2 = 0
email_db = 0
for i in email:
    if i in "@":
        db_1 += 1
    elif i in ".":
        db_2 += 1
if db_1 == 1:
    email_db += 1
if db_2 >= 0:
    email_db += 1
if email_db == 2:
    print("Érvényes email cím!")
else:
    print("Nem email cím!")