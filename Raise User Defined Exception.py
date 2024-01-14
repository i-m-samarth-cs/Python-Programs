class InvalidPassword(Exception):
    pass
def verify_pass(pswd):
    if str(pswd)!="abc":
        raise InvalidPassword
    else:
        print("Valid Password")
verify_pass("abc")
verify_pass("xyz")
