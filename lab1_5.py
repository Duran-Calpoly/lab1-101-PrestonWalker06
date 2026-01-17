def check_multiple (number):
    if number % 3 == 0 and number % 5 == 0:
        return True
    else:
        return False

def check_password (input_string):
    if input_string == "Python123":
        return "access granted"
    else: 
        return "access denied"
    
def calculate_federal_tax (salary):
    if salary <= 11000:
        return (1000.0)
    elif salary <= 50000:
        return (11000.0)
    else:
        return (24000.0)
        
