# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"

total_racetime = input('Total race time in seconds: ')
pitstop_count = input('How many pit stops were made:')
pitstop_duration = input('Average pit stop duration in seconds: ')

total_pitstop_time = int(pitstop_count)* float(pitstop_duration)
pitstop_percentage = ((float(total_pitstop_time) / float(total_racetime)))*100

print(f"""The total amount of time you spent in the pit stop was {total_pitstop_time}(s).
 As a percentage of the race, you spent {round(pitstop_percentage,2)}% in the pitstop you fool
""")

if pitstop_percentage > 5:
    print("You need a new pit crew. 🛠️")