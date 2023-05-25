import hashlib

pin_hash = "b0439fae31f8cbba6294af86234d5a28"
secret_sentence = """
Look at these cool penguins 
        (o_
(o_    //\\
(/)_   V_/_ 
"""

while True:
    user_pin = input("Enter the secure password: ")

    # Hash the user's input
    user_pin_hash = hashlib.md5(user_pin.encode()).hexdigest()

    if user_pin_hash == pin_hash:
        print("Access granted!\n")
        print(secret_sentence)
        break
    else:
        print("Incorrect PIN. Try again.\n")