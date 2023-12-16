from datetime import datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):

    birthday_dict = defaultdict(list)
    
    # Getting current date
    today = datetime.today().date()
    #today = datetime(2023, 12, 17).date()
    
    # Loop users
    for user in users:
        # Date converting
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year = today.year)

        # Check date this year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year = today.year + 1)

        # Comparing to the current date
        delta_days = (birthday_this_year - today).days

        # Checking the week day and Monday shifts if needed
        if delta_days < 7:
            day_of_week = (today + timedelta(days=delta_days)).strftime('%A')

            if day_of_week in ['Saturday', 'Sunday']:
                day_of_week = 'Monday'
                
            birthday_dict[day_of_week].append(name)

        else:
            continue

    for day, names in birthday_dict.items():
        print(f"{day}: {', '.join(names)}")
