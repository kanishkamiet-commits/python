# -------------------------------------------------
# Program: Validate Username and Password
# -------------------------------------------------

# Predefined credentials (example)
correct_username = "admin"
correct_password = "Admin@123"

# Input
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

# Validation
if username == correct_username and password == correct_password:
    print("Login Successful.")
else:
    print("Invalid Username or Password.")




#--------------------------------------------------------
'''output
Enter username: admin
Enter password: Admin@123
Login Successful.
#--------------------------------------------------------
Enter username: user
Enter password: pass
Invalid Username or Password.
'''