import json
from pathlib import Path


class Config:

    def __init__(self, config_file:Path = None):
        if config_file is not None:
            self.config_file = config_file
        else:
            # Default config file
            self.config_file = Path.home() / '.config' / 'diario' / 'config.json'
        # Crea la cartella principale se non esiste
        self.config_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.config_file.exists():
            # Crea un file di configurazione di default se il file non esiste
            base_dir = Path.home() / ".local" / "share" / "diario"
            base_dir.mkdir(parents=True, exist_ok=True)
            default_config = {}
            default_config["path"] = str(base_dir)
            default_config["locale"] = "en_US"
            default_config["editor"] = "nano"
            self.config_file.write_text(
                json.dumps(default_config, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
        self.settings = json.load(self.config_file.open())