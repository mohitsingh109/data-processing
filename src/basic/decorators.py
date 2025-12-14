def check_auth(func): # decorator to check authentication
    def wrapper():
        print("Checking authentication...")
        func()
        print("Authentication checked.")
    return wrapper

@check_auth
def delete_dashboard():
    print("Deleting dashboard...")

delete_dashboard()