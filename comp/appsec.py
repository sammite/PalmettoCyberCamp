# chatgpt generated code:

bank_account = 1000

while True:
    customer_name = input("Enter name of customer: ")
    number = float(input("Enter a number: "))
    action = input("Enter 'withdraw' or 'deposit': ")

    if action == "withdraw":
        bank_account -= number
    elif action == "deposit":
        bank_account += number

    print(f"Bank account balance: ${bank_account} customer name: {customer_name}")
