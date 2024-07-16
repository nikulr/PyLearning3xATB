# match with function

def allowed_to_python_class(name):
    match name:
        case "Dell":
            print("Dell is allowed")
        case "HP":
            print("Dell is allowed")
        case "Lenovo":
            print("Dell is allowed")
        case "Apple":
            print("Dell is allowed")
        case _:
            print("Not allowed")


allowed_to_python_class("Asus")
