def how_many_seconds(hours):
    seconds_per_hour = 60 * 60
    return seconds_per_hour * hours


print(how_many_seconds(4))

def football_points(wins, draws, losses):
    points = wins * 3 + draws
    points -= losses
    return points


print(football_points(4,2,1))