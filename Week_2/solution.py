day_in_month = int(input("How many days are there in the month? "))
start_day = int(input("What day does your month start on? Enter 0 for Sunday, 1 for Monday, ..., 6 for Saturday: "))

days_of_week = ["S ", "M ", "T ", "W ", "T ", "F ", "S "]
print(" ".join(days_of_week))

calendar = ["-"] * start_day

for day in range(1, day_in_month + 1): #just doing day in the month will result in 1 day short
    calendar.append(f"{day:>2}")

for week_start in range(0, len(calendar), 7):
    print(" ".join(calendar[week_start:week_start + 7]))