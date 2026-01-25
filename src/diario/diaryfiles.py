import datetime
import os
from pathlib import Path


class DiaryFiles:

    def __init__(self, base_dir: Path, folder_name: str = "diary"):
        self.base_dir = base_dir
        self.diary_dir = base_dir / folder_name
        self.daily_dir = self.diary_dir / "daily"
        self.weekly_dir = self.diary_dir / "weekly"
        self.monthly_dir = self.diary_dir / "monthly"
        self.quarterly_dir = self.diary_dir / "quarterly"
        self.yearly_dir = self.diary_dir / "yearly"

    # -=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_

    def _get_day_path(self, day:datetime.date) -> Path:
        # Struttura: {folder_name}/daily/YYYY/MM/DD/
        return self.daily_dir / f"{day:%Y}" / f"{day:%m}" / f"{day:%d}"

    # -=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_

    def _get_week_path(self, day: datetime.date) -> Path:
        # Struttura: {folder_name}/weekly/YYYY/VV/
        iso_year, iso_week, _ = day.isocalendar()
        return self.weekly_dir / f"{iso_year}" / f"{iso_week:02d}"

    # -=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_

    def _get_month_path(self, day: datetime.date) -> Path:
        # Struttura: {folder_name}/monthly/YYYY/MM/
        return self.monthly_dir / f"{day:%Y}" / f"{day:%m}"

    # -=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_

    def _get_quarter_path(self, day: datetime.date) -> Path:
        # Struttura: {folder_name}/quarterly/YYYY/QQ/
        quarter = str((day.month - 1) // 3 + 1).zfill(2)
        return self.quarterly_dir / f"{day:%Y}" / quarter

    # -=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_

    def _get_year_path(self, day: datetime.date) -> Path:
        # Struttura: {folder_name}/yearly/YYYY/
        return self.yearly_dir / f"{day:%Y}"

    # -=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_

    def get(self, day: datetime.date, view: str = "daily") -> Path:
        if view == "daily":
            return self._get_day_path(day)
        elif view == "weekly":
            return self._get_week_path(day)
        elif view == "monthly":
            return self._get_month_path(day)
        elif view == "quarterly":
            return self._get_quarter_path(day)
        elif view == "yearly":
            return self._get_year_path(day)
        elif view == "yesterday":
            return self._get_day_path(day - datetime.timedelta(days=1))
        elif view == "tomorrow":
            return self._get_day_path(day + datetime.timedelta(days=1))
        else:
            raise ValueError(f"Invalid view: {view}")

    # -=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_

    def get_relative_path(self, day: datetime.date, source_view: str, destination_view: str) -> str:

        # Origin
        source_path = self.get(day, view=source_view)
        destination_path = self.get(day, view=destination_view) / "_index.md"

        relative = os.path.relpath(destination_path, source_path)
        return relative


