#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
  secs_hours = int(secs / 3600)
  secs_mint = int(secs / 60)

  return secs_hours, secs_mint

#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))