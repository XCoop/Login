# Feedback

### Strengths:
1. **Basic Structure**: The program has a clear structure with functions for login, registration, and post-login actions.
2. **File Handling**: The use of a file (`test.txt`) to store user credentials is a good starting point for a simple authentication system.
3. **Recursive Calls**: The program uses recursion to allow users to retry operations like login or registration.

---

### Issues and Suggestions for Improvement:

#### 1. **Infinite Recursion Risk**:
   - Functions like `main()`, `Register()`, and `Logged_In()` call themselves recursively on invalid input or failed attempts. This can lead to a `RecursionError` if the user repeatedly enters invalid data.
   - **Fix**: Use loops instead of recursion for better control and to avoid stack overflow.

   ```python
   def main():
       while True:
           choice = input("Login - 1, Register - 2, Quit - 3: ")
           if choice == "1":
               Log_In()
           elif choice == "2":
               Register()
           elif choice == "3":
               break
           else:
               print("Invalid Choice")
   ```

---

#### 2. **File Handling Issues**:
   - The `Register()` function opens the file multiple times without closing it properly. This can lead to resource leaks.
   - **Fix**: Use `with open()` for all file operations to ensure proper file handling.

   ```python
   def Register():
       NewUser = input("Username? ")
       with open("test.txt", "r") as file:
           for line in file:
               row = line.rstrip().split(",")
               if NewUser == row[0]:
                   print("Username Already Taken")
                   return Register()
       NewPass = input("Password? ")
       if len(NewPass) <= 4:
           print("Password must be 4 or more characters")
       else:
           with open("test.txt", "a") as file:
               file.write(f"{NewUser},{NewPass}\n")
   ```

---

#### 3. **Security Concerns**:
   - Storing passwords in plain text (`test.txt`) is insecure.
   - **Fix**: Use a hashing library like `bcrypt` or `hashlib` to store hashed passwords instead of plain text.

   ```python
   import bcrypt

   salt = b"$2b$12$ieYNkQp8QumgedUo30nuPO"

   # Hashing a password
   hashed_password = bcrypt.hashpw(password.encode(), salt=salt)

   # Verifying a password
   if bcrypt.checkpw(input_password.encode(), hashed_password):
       print("Login successful!")
   ```

---

#### 4. **Error Handling**:
   - The program lacks error handling for file operations. If the file `test.txt` does not exist, the program will crash.
   - **Fix**: Add error handling for file operations.

   ```python
   try:
       with open("test.txt", "r") as file:
           # File operations
   except FileNotFoundError:
       print("No users registered yet.")
   ```

---

#### 5. **Logic Issues in `Log_In()`**:
   - The `Log_In()` function checks if `Username + Password == row[0] + row[1]`. This is not a reliable way to validate credentials because it concatenates the username and password, which could lead to false positives.
   - **Fix**: Compare the username and password separately.

   ```python
   if Username == row[0] and Password == row[1]:
       data1 = 1
       Logged_In()
   ```

---

#### 6. **Incomplete Functionality**:
   - The `Logged_In()` function does not implement password change functionality.
   - **Fix**: Implement the password change feature.

   ```python
   def Logged_In():
       while True:
           choice = input("Change Password - 1, Logout - 2: ")
           if choice == "1":
               NewPassword = input("New Password? ")
               if len(NewPassword) <= 4:
                   print("Password must be 4 or more characters")
               else:
                   # Update password in the file
                   with open("test.txt", "r") as file:
                       lines = file.readlines()
                   with open("test.txt", "w") as file:
                       for line in lines:
                           row = line.rstrip().split(",")
                           if row[0] == Username:
                               file.write(f"{row[0]},{NewPassword}\n")
                           else:
                               file.write(line)
                   print("Password changed successfully!")
           elif choice == "2":
               break
           else:
               print("Invalid choice")
   ```

---

#### 7. **Code Readability**:
   - The code could benefit from better formatting and comments to improve readability.
   - **Fix**: Add comments explaining the purpose of each function and improve indentation.