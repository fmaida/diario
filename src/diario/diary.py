# Questa riga serve perchè al momento
# di eseguire il codice ancora non
# sa cosa sia il Diary.Contents
# restituito da Diary.get_day()
from __future__ import annotations

import datetime
import locale
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator
from diario.config import Config
from diario.templates import Templates
from diario.diaryfiles import DiaryFiles


class Diary:

    class Contents:

        def __init__(self):
            self.index:Path|None = None
            self.attachements:list[Path] = []

        def __iter__(self) -> Iterator[Path]:
            if self.index is not None:
                yield self.index
            yield from self.attachements

        def __len__(self) -> int:
            return 1 + len(self.attachements)

    @dataclass
    class ContentsList:
        daily: Diary.Contents | None
        weekly: Diary.Contents | None
        quarterly: Diary.Contents | None
        monthly: Diary.Contents | None
        yearly: Diary.Contents | None

    def __init__(self, config_file:Path = None):
        self.config = Config(config_file=config_file)
        if self.config.settings.get("locale") is not None:
            locale.setlocale(locale.LC_TIME, self.config.settings.get("locale") + ".UTF-8")
        #self.today = datetime.date.today()
        base_dir = Path(self.config.settings["path"])
        if base_dir.is_dir() and base_dir.exists():
            self.files = DiaryFiles(base_dir=base_dir)
            self.templates = Templates(path=base_dir / "templates", files=self.files)
        else:
            raise ValueError(f"Invalid base directory: {base_dir}")

    def _build_contents(self, file_path: Path, template_text: str) -> Diary.Contents:

        # Crea la cartella se non esiste
        file_path.mkdir(parents=True, exist_ok=True)

        contents = Diary.Contents()
        contents.index = file_path / "_index.md"

        # Se il file indice non esiste lo crea
        if not contents.index.exists():
            contents.index.write_text(template_text, encoding="utf-8")

        # Aggiunge tutti gli altri file
        # nella cartella come allegati
        for file in file_path.iterdir():
            if file.is_file() and file.name != "_index.md":
                contents.attachements.append(file)

        return contents

    def get(self, day:datetime.date = None) -> Diary.ContentsList:

        day = self.today if day is None else day

        return Diary.ContentsList(
            yearly=self.get_single(day, view="yearly"),
            quarterly=self.get_single(day, view="quarterly"),
            monthly=self.get_single(day, view="monthly"),
            weekly=self.get_single(day, view="weekly"),
            daily=self.get_single(day, view="daily"),
        )

    # -=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_-=-_

    def get_single(self, day:datetime.date = None, view:str="daily") -> Diary.Contents:

        day = self.today if day is None else day

        file_path = self.files.get(day, view=view)
        if view == "daily":
            template = self.templates.get_daily(day)
        elif view == "weekly":
            template = self.templates.get_weekly(day)
        elif view == "monthly":
            template = self.templates.get_monthly(day)
        elif view == "quarterly":
            template = self.templates.get_quarterly(day)
        elif view == "yearly":
            template = self.templates.get_yearly(day)
        else:
            raise ValueError(f"Invalid view: {view}")

        return self._build_contents(file_path=file_path, template_text=template)