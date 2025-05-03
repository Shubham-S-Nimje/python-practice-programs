import random
def otp_required(function):
    def wrapper():
        gen_otp=random.randint(1000,9999)
        print(f'input {gen_otp} to perform transaction')
        in_otp=int(input("Input OTP "))
        if in_otp==gen_otp:
            function()
        else:
            print("Invalid OTP")
            return

    return wrapper
    

@otp_required
def deposit():
    print("this is deposit function")

@otp_required
def withdraw():
    print("this is withdraw function")


deposit()
withdraw()
