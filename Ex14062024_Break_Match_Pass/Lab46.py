browser = input("Enter your name:")
browser = browser.lower()
match browser:
    case "chrome":
        print("Execute the code for Chrome browser")
    case "firefox":
        print("Execute the code for Firefox browser")
    case _:
        print("No Idea")