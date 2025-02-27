def grade(score):
    if score >= 90:
        return "You have an A"
    elif score <=89:
        return "You have a A-"
    elif score <=84:
        return "You have a B+"
    elif score <=79:
        return "You have a B"
    elif score <=74:
        return "You have a B-"
    elif score <=69:
        return"You have a C+"
    elif score <=64:
        return "You have a C"
    elif score <=59:
        return "You have a C-"
    elif score <=54:
        return "You have a D+"
    elif score <=49:
        return "You have a D"
    elif score <=44:
        return "You have a D-"
    else:
        return "You have an E"
score = int(input("Enter your score: "))

                                             
