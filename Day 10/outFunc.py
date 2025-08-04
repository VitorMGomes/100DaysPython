def format_name(first_name, last_name):
    """Return bla bla bla"""
    if first_name == "" and last_name == "":
        return "No valid inputs"
    
    full_name = first_name.title() + " " + last_name.title()
    
    return full_name



formatted = format_name("VITOR", "GOMEs")
print(formatted)



