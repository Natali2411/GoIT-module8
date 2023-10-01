from __future__ import annotations

import enum
from datetime import date, datetime, timedelta
from collections import defaultdict
from typing import Any


class DayNames(enum.Enum):
    """
    Class enum with the day names
    """
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


def get_weeek_dates_per_year() -> dict[tuple, dict[str, Any]]:
    """
    Method returns the information about next 7 days from today.
    :return: Dictionary with dates and day names.
    """
    today_date = date.today()
    week_info = defaultdict(dict)
    for _day in range(7 + 1):
        week_date: datetime.date = today_date + timedelta(days=_day)
        week_info[(week_date.day, week_date.month)] = {
            "date": week_date,
            "day_name": week_date.strftime('%A')
        }
    return dict(week_info)


def get_birthdays_per_week(users: dict[str, Any]) -> dict[str, list]:
    """
    Method returns the dictionary where the key is a name of the day (Monday, Tuesday
    etc.) and the value is a list of names (people who have birthdays in that day).
    :param users: The list of users with names and their birtdays.
    :return: The dictionary where the key is a name of the day (Monday, Tuesday
    etc.) and the value is a list of names (people who have birthdays in that day).
    """
    week_info = get_weeek_dates_per_year()
    week_birthdays = defaultdict(list)
    for user in users:
        user_birthday: datetime = user.get("birthday")
        user_birthday_info = week_info.get((user_birthday.day, user_birthday.month))
        if user_birthday_info:
            user_first_name = user.get("name").split()[0]
            day_name: str = user_birthday_info.get("day_name")
            day_name: str | DayNames = day_name if day_name not in (
            DayNames.SATURDAY.value,
            DayNames.SUNDAY.value) \
                else DayNames.MONDAY.value
            week_birthdays[day_name].append(user_first_name)
    return dict(week_birthdays)


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Nataliia Tiutiunnyk", "birthday": datetime(1992, 1, 2).date()},
    ]

    result = get_birthdays_per_week(users)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
