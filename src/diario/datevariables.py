import datetime
import re

from diario.diaryfiles import DiaryFiles


class DateVariables:

    _pattern: re.Pattern = re.compile(r"\{\{\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\}\}")

    def __init__(self, files:DiaryFiles) -> None:
        self._day: datetime.date|None = None
        self._files = files
        self.day_name: str = ""
        self.day_name_short: str = ""
        self.day_name_short_2: str = ""
        self.day: str = ""
        self.month: str = ""
        self.month_name: str = ""
        self.month_name_short: str = ""
        self.year: str = ""
        self.year_short: str = ""
        self.quarter: str = ""
        self.yesterday_day_name: str = ""
        self.yesterday_day_name_short: str = ""
        self.yesterday_day_name_short_2: str = ""
        self.yesterday_day: str = ""
        self.yesterday_month: str = ""
        self.yesterday_month_name: str = ""
        self.yesterday_month_name_short: str = ""
        self.yesterday_year: str = ""
        self.yesterday_year_short: str = ""
        self.tomorrow_day_name: str = ""
        self.tomorrow_day_name_short: str = ""
        self.tomorrow_day_name_short_2: str = ""
        self.tomorrow_day: str = ""
        self.tomorrow_month: str = ""
        self.tomorrow_month_name: str = ""
        self.tomorrow_month_name_short: str = ""
        self.tomorrow_year: str = ""
        self.tomorrow_year_short: str = ""
        self.monday_day_name: str = ""
        self.monday_day_name_short: str = ""
        self.monday_day_name_short_2: str = ""
        self.monday_day: str = ""
        self.monday_month: str = ""
        self.monday_month_name: str = ""
        self.monday_month_name_short: str = ""
        self.monday_year: str = ""
        self.monday_year_short: str = ""
        self.sunday_day_name: str = ""
        self.sunday_day_name_short: str = ""
        self.sunday_day_name_short_2: str = ""
        self.sunday_day: str = ""
        self.sunday_month: str = ""
        self.sunday_month_name: str = ""
        self.sunday_month_name_short: str = ""
        self.sunday_year: str = ""
        self.sunday_year_short: str = ""
        self.daily_url: str = ""
        self.weekly_url: str = ""
        self.monthly_url: str = ""
        self.quarterly_url: str = ""
        self.yearly_url: str = ""
        self.today_url: str = ""
        self.yesterday_url: str = ""
        self.tomorrow_url: str = ""
        self.monday_url: str = ""
        self.tuesday_url: str = ""
        self.wednesday_url: str = ""
        self.thursday_url: str = ""
        self.friday_url: str = ""
        self.saturday_url: str = ""
        self.sunday_url: str = ""

    @staticmethod
    def calculate_yesterday(day:datetime.date):
        return day - datetime.timedelta(days=1)

    @staticmethod
    def calculate_tomorrow(day:datetime.date):
        return day + datetime.timedelta(days=1)

    @staticmethod
    def calculate_monday(day:datetime.date):
        return day - datetime.timedelta(days=day.isoweekday() - 1)

    @staticmethod
    def calculate_sunday(day:datetime.date):
        return day + datetime.timedelta(days=7 - day.isoweekday())

    @staticmethod
    def _assign_values(day:datetime.date):
        return (day.strftime("%A").title(),
                day.strftime("%a").title(),
                day.strftime("%a").title()[:2],
                day.strftime("%d"),
                day.strftime("%m"),
                day.strftime("%B").title(),
                day.strftime("%b").title(),
                day.strftime("%Y"),
                day.strftime("%y"))

    def _render(self, day:datetime.date) -> None:
        # Calcola i giorni
        yesterday = self.calculate_yesterday(day)
        tomorrow = self.calculate_tomorrow(day)
        monday = self.calculate_monday(day)
        sunday = self.calculate_sunday(day)

        # Giorno richiesto
        (self.day_name, self.day_name_short,
         self.day_name_short_2, self.day, self.month,
         self.month_name, self.month_name_short,
         self.year, self.year_short) = self._assign_values(day)

        # Ieri
        (self.yesterday_day_name, self.yesterday_day_name_short,
         self.yesterday_day_name_short_2, self.yesterday_day, self.yesterday_month,
         self.yesterday_month_name, self.yesterday_month_name_short,
         self.yesterday_year, self.yesterday_year_short) = self._assign_values(yesterday)

        # Domani
        (self.tomorrow_day_name, self.tomorrow_day_name_short,
         self.tomorrow_day_name_short_2, self.tomorrow_day, self.tomorrow_month,
         self.tomorrow_month_name, self.tomorrow_month_name_short,
         self.tomorrow_year, self.tomorrow_year_short) = self._assign_values(tomorrow)

        # Lunedì
        (self.monday_day_name, self.monday_day_name_short,
         self.monday_day_name_short_2, self.monday_day, self.monday_month,
         self.monday_month_name, self.monday_month_name_short,
         self.monday_year, self.monday_year_short) = self._assign_values(monday)

        # Martedì
        (self.tuesday_day_name, self.tuesday_day_name_short,
         self.tuesday_day_name_short_2, self.tuesday_day, self.tuesday_month,
         self.tuesday_month_name, self.tuesday_month_name_short,
         self.tuesday_year, self.tuesday_year_short) = self._assign_values(monday + datetime.timedelta(days=1))

        # Mercoledì
        (self.wednesday_day_name, self.wednesday_day_name_short,
         self.wednesday_day_name_short_2, self.wednesday_day, self.wednesday_month,
         self.wednesday_month_name, self.wednesday_month_name_short,
         self.wednesday_year, self.wednesday_year_short) = self._assign_values(monday + datetime.timedelta(days=2))

        # Giovedì
        (self.thursday_day_name, self.thursday_day_name_short,
         self.thursday_day_name_short_2, self.thursday_day, self.thursday_month,
         self.thursday_month_name, self.thursday_month_name_short,
         self.thursday_year, self.thursday_year_short) = self._assign_values(monday + datetime.timedelta(days=3))

        # Venerdì
        (self.friday_day_name, self.friday_day_name_short,
         self.friday_day_name_short_2, self.friday_day, self.friday_month,
         self.friday_month_name, self.friday_month_name_short,
         self.friday_year, self.friday_year_short) = self._assign_values(monday + datetime.timedelta(days=4))

        # Sabato
        (self.saturday_day_name, self.saturday_day_name_short,
         self.saturday_day_name_short_2, self.saturday_day, self.saturday_month,
         self.saturday_month_name, self.saturday_month_name_short,
         self.saturday_year, self.saturday_year_short) = self._assign_values(monday + datetime.timedelta(days=5))

        # Domenica
        (self.sunday_day_name, self.sunday_day_name_short,
         self.sunday_day_name_short_2, self.sunday_day, self.sunday_month,
         self.sunday_month_name, self.sunday_month_name_short,
         self.sunday_year, self.sunday_year_short) = self._assign_values(sunday)

        # Trimestre
        self.quarter = "Q" + str((day.month - 1) // 3 + 1)

        # Percorsi ai files
        self.yearly_url = self._files.get_relative_path(day, source_view="quarterly", destination_view="yearly")
        self.quarterly_url = self._files.get_relative_path(day, source_view="monthly", destination_view="quarterly")
        self.monthly_url = self._files.get_relative_path(day, source_view="weekly", destination_view="monthly")
        self.weekly_url = self._files.get_relative_path(day, source_view="daily", destination_view="weekly")
        self.daily_url = str(self._files.get(day, view="daily"))

        self.yesterday_url = self._files.get_relative_path(day, source_view="daily", destination_view="yesterday")
        self.today_url = self.daily_url
        self.tomorrow_url = self._files.get_relative_path(day, source_view="daily", destination_view="tomorrow")

        temp = monday
        self.monday_url = self._files.get_relative_path(temp, source_view="weekly", destination_view="daily")
        temp += datetime.timedelta(days=1)
        self.tuesday_url = self._files.get_relative_path(temp, source_view="weekly", destination_view="daily")
        temp += datetime.timedelta(days=1)
        self.wednesday_url = self._files.get_relative_path(temp, source_view="weekly", destination_view="daily")
        temp += datetime.timedelta(days=1)
        self.thursday_url = self._files.get_relative_path(temp, source_view="weekly", destination_view="daily")
        temp += datetime.timedelta(days=1)
        self.friday_url = self._files.get_relative_path(temp, source_view="weekly", destination_view="daily")
        temp += datetime.timedelta(days=1)
        self.saturday_url = self._files.get_relative_path(temp, source_view="weekly", destination_view="daily")
        temp = sunday
        self.sunday_url = self._files.get_relative_path(temp, source_view="weekly", destination_view="daily")

    def render(self, day:datetime.date):
        if self._day != day:
            self._render(day)
            self._day = day

    def _replace(self, match: re.Match) -> str:
        name = match.group(1)

        # escludi attributi interni o inesistenti
        if name.startswith("_"):
            return match.group(0)

        if not hasattr(self, name):
            return match.group(0)

        value = getattr(self, name)
        return str(value)

    def replace(self, text:str) -> str:
        return DateVariables._pattern.sub(self._replace, text)