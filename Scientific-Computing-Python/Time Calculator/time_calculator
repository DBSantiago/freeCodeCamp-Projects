def add_time(start, duration, starting_day='0'):
    a = start.split()
    period = a[1]

    b = a[0].split(':')

    start_hours = b[0]
    start_minutes = b[1]

    c = duration.split(':')

    duration_hours = c[0]
    duration_minutes = c[1]

    new_period = period 
    new_hours = int(start_hours) + int(duration_hours)
    new_minutes = int(start_minutes) + int(duration_minutes)

    days_passed = 0

    if new_hours == 11 and new_minutes > 59:
      if new_period == 'AM':
        new_hours += 1
        new_minutes -= 60
        new_period = 'PM'
      elif new_period == 'PM':
        new_hours += 1
        new_minutes -= 60
        new_period = 'AM'
        days_passed += 1


    while new_hours > 12:

      if new_period == 'AM':
          new_period = 'PM'
          new_hours -= 12
          continue
      elif new_period == 'PM':
          new_period = 'AM'
          new_hours -= 12
          days_passed += 1
          continue

    if new_hours == 11 and new_minutes > 59:
      if new_period == 'AM':
        new_hours += 1
        new_minutes -= 60
        new_period = 'PM'
      elif new_period == 'PM':
        new_hours += 1
        new_minutes -= 60
        new_period = 'AM'
        days_passed += 1


    if new_minutes > 59:
        new_hours += 1
        new_minutes -= 60
  

    weekdays = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}

    day = 0  
    for key,val in weekdays.items():
        if starting_day.capitalize() == val:
          day = key
   
    
    
    day_week = weekdays[(day + days_passed) % 7]
    new_minutes = str(new_minutes)
    if days_passed == 0:
        if starting_day == '0':
            new_time = '{}:{} {}'.format(new_hours,new_minutes.zfill(2),new_period)
        else:
            new_time = '{}:{} {}, {}'.format(new_hours,new_minutes.zfill(2),new_period,starting_day.capitalize())
    elif days_passed == 1:
        if starting_day == '0':
          new_time = '{}:{} {} (next day)'.format(new_hours,new_minutes.zfill(2),new_period)
        else:
          new_time = '{}:{} {}, {} (next day)'.format(new_hours,new_minutes.zfill(2),new_period,day_week)
    else:
        if starting_day == '0':
            new_time = '{}:{} {} ({} days later)'.format(new_hours,new_minutes.zfill(2),new_period,days_passed)
        else:
            new_time = '{}:{} {}, {} ({} days later)'.format(new_hours,new_minutes.zfill(2),new_period,day_week,days_passed)

    return new_time
