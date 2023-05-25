password = "hunter2"
secret_sentence = """
Look at these cool penguins 
        (o_
(o_    //\\
(/)_   V_/_ 
"""

while True:
    user_password = input("Enter the password: ")

    if user_password == password:
        print(secret_sentence)
        break
    else:
        print("Incorrect password. Try again.")