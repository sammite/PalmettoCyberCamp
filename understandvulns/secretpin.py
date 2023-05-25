pin = "1337"
secret_sentence = """
Look at these cool penguins 
        (o_
(o_    //\\
(/)_   V_/_ 
"""

while True:
    user_pin = input("Enter the PIN: ")

    if user_pin == pin:
        print("Access granted!\n")
        print(secret_sentence)
        break
    else:
        print("Incorrect PIN. Try again.\n")