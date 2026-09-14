def password_strength(pas):
    score=0
    if len(pas)>=8:
        score+=1
    if any( ch.isupper() for ch in (pas)):
        score+=1
    if any( ch.islower() for ch in (pas)):
        score+=1
    if any( ch.isdigit() for ch in (pas)):
        score+=1
    if any( not ch.isalnum() for ch in (pas)):
        score+=1

    if score<=2:
        return("Week")
    elif score==3 or score==4:
        return("Medium")
    else:
        return("Strong")

passs=input("Enter Password:")
print("Password Strength:",password_strength(passs))