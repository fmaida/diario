import datetime
import subprocess
import sys

from diario.diary import Diary


def info_quit(code:int=1) -> None:
    msg = "Uso: diario [--tomorrow | --yesterday | --populate | GG/MM/AAAA | GG-MM-AAAA]"
    if code == 0:
        print(msg)
        raise SystemExit(0)
    raise SystemExit(msg)

def _parse_date(s: str) -> datetime.date:
    try:
        return datetime.datetime.strptime(s, "%d/%m/%Y").date()
    except ValueError as e:
        try:
            return datetime.datetime.strptime(s, "%d-%m-%Y").date()
        except ValueError as e:
            raise SystemExit(f"Data non valida: '{s}'. Formato atteso: GG/MM/AAAA o GG-MM-AAAA (es. 20/12/2026 o 20-12-2026).") from e

def main() -> None:

    # diario            -> oggi
    # diario GG/MM/AAAA -> giorno specifico

    diario = Diary()
    today = datetime.date.today()
    day = None

    args = sys.argv[1:]
    if len(args) == 0:
        day = today
    elif len(args) == 1:
        arg = args[0].lower().strip()
        if arg == "--tomorrow":
            day = today + datetime.timedelta(days=1)
        elif arg == "--yesterday":
            day = today - datetime.timedelta(days=1)
        elif arg == "--populate":
            day = today + datetime.timedelta(days=365)
            for i in range(366):
                collezione = diario.get(day=day - datetime.timedelta(days=i))
            quit(0)
        elif arg == "--help" or arg == "-h":
            info_quit(0)
        else:
            day = _parse_date(args[0])
    else:
        info_quit()

    collezione = diario.get(day)
    #print(collezione.daily.index)
    #print(collezione.weekly.index)
    #print(collezione.monthly.index)
    #print(collezione.quarterly.index)
    #print(collezione.yearly.index)

    editor = diario.config.settings.get("editor", "nano")
    subprocess.run(
        [
            #"open",
            #"-a",
            editor,
            #str(collezione.yearly.index),
            #str(collezione.quarterly.index),
            #str(collezione.monthly.index),
            str(collezione.weekly.index),
            str(collezione.daily.index),
        ],
        check=False,
    )

if __name__ == "__main__":
    main()