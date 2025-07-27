from dice import Die

six_die = Die()
for i in range(10): six_die.roll_die()
ten_die = Die(10)
for i in range(10): ten_die.roll_die()
twenty_die = Die(20)
for i in range(10): twenty_die.roll_die()