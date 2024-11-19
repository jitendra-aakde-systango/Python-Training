def transaction(func):
    def wrapper():
        print("transaction Start")
        func()
        print("transaction finish")
    return wrapper
# @transaction
def tra():
    print("Tra called")
hello = transaction(tra)
# tra()
hello()