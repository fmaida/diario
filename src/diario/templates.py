import datetime
from dataclasses import dataclass
from pathlib import Path

from diario.datevariables import DateVariables
from diario.diaryfiles import DiaryFiles


class Templates:

    def __init__(self, path: Path, files:DiaryFiles):
        self.path = path
        self.path.mkdir(parents=True, exist_ok=True)
        self.files = files
        self.dates = DateVariables(files=self.files)

    def _return_template(self, filename:str, day:datetime.date):
        temp = self.path / filename
        if temp.is_file() and temp.exists():
            self.dates.render(day)
            text = temp.read_text(encoding="utf-8")
            return self.dates.replace(text)
        else:
            return ""

    def get_daily(self, day:datetime.date) -> str:
        return self._return_template(filename="daily.md", day=day)

    def get_weekly(self, day:datetime.date) -> str:
        return self._return_template(filename="weekly.md", day=day)

    def get_monthly(self, day:datetime.date) -> str:
        return self._return_template(filename="monthly.md", day=day)

    def get_quarterly(self, day:datetime.date) -> str:
        return self._return_template(filename="quarterly.md", day=day)

    def get_yearly(self, day:datetime.date) -> str:
        return self._return_template(filename="yearly.md", day=day)