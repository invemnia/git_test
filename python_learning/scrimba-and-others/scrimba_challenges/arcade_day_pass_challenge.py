# Write your code here :-)
# 🕹️ Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game
customer_name = 'bob'
number_passes = 100
tokens_per_pass = 2
price_per_pass = 2.5
tokens_required = 3
#
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
total_tokens = number_passes * tokens_per_pass
total_cost = number_passes * price_per_pass

games_available = total_tokens // tokens_required

#
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens
#    - total cost
#    - games available

print(f'Hello {customer_name}, you purchased {number_passes}, while using {total_tokens} with a total of ${total_cost,2f} with {games_available} games available')
