import datetime
if __name__ == "__main__":
    """Calculates the year you turn 100"""
def calc_year_to_turn_100(age):
    present_year = datetime.datetime.year().now
    year_to_turn_100 = present_year + (100 - age)
    return year_to_turn_100

def main():
    name = input("Enter Your Name: ")
    age = int(input("Enter Your Age: "))
    year_to_turn_100 = calc_year_to_turn_100(age)
    print(f"Hello {name}. You will turn 100 years in the year {year_to_turn_100}.")
