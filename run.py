from round import normal_rounds_data
from round.utilities import Cumulative_Round

ROUND = 10
STARTING_CASH = 650

round_up_to = Cumulative_Round(final_round=ROUND, round_data=normal_rounds_data)

print(round_up_to.total_damage())