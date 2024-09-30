def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars_converted=d.replace("$","")
    return float(dollars_converted)

def percent_to_float(p):
    percentage_without_symbol=p.replace("%","")
    percentage=float(percentage_without_symbol)/100
    return percentage


main()