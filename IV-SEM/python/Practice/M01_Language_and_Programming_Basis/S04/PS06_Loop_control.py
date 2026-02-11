corr_pass = "1 2 3 4 5"
for _ in range(1,4):
    passw = input()
    if passw == corr_pass:
        print("Login Successful")
        break
    else:
        print("Incorrect password")
else:
    print("Account Locked")