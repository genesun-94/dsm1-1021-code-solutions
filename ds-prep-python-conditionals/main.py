day_of_week = "tuesday"

if day_of_week in ("saturday", "sunday"):
  print("Have a good weekend!")
else:
  print("It's a weekday!")

student_1_score = 85
pass_or_fail = "You passed!" if (student_1_score > 70) else "You failed!"

print(student_1_score, pass_or_fail)

student_2_score = 95

if student_2_score < 60:
  letter_grade = "F"
elif 60 < student_2_score < 70:
  letter_grade = "D"
elif 70 < student_2_score < 80:
  letter_grade = "C"
elif 80 < student_2_score < 90:
  letter_grade = "B"
elif 90 < student_2_score < 100:
  letter_grade = "A"
else:
  letter_grade = "A+"

print(letter_grade)

def get_season_info(x):
  if x == "summer":
    print("Statistically, it's likely to be hotter today than in 6 months from now. Don't sweat it, though.")
  elif x == "spring":
    print("The flowers are blooming while it's spring, but that correlation, not causation.")
  elif x == "autumn":
    print("The leaves seem to regress to warmer colors as autumn approaches its end.")
  elif x == "winter":
    print("There may only be a high likelihood of it being cold today, but there's a 100 percent chance of me wanting that sweater.")
  else:
    print("That's not a season. Most likely.")

get_season_info("summer")
get_season_info("spring")
get_season_info("autumn")
get_season_info("winter")
get_season_info("hello")

age = 42
print("adult") if age > 18 else print("child")
