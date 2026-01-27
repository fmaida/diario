# Diario

A personal diary application inspired by the bullet journal method.

Diario is a strongly opinionated application: decisions about structure, format, and time subdivision are intentional and not configurable. What *is* configurable by the user are the Markdown template files located in the `templates` directory.

The application was created to address the following needs:

* I wanted a personal note management system organized by days, weeks, months, quarters, and years.
* I wanted a system that is maintainable over the long term, ideally for the entire lifetime of the user.
* I wanted the application data not to depend on the application itself. Even if the app stopped working or was no longer maintained, all documents would remain readable, editable, and usable as simple Markdown files organized in directories.
* I wanted a system for which creating a backup is trivial. In this specific case, it is enough to copy a single directory.
* I wanted a system compatible with common cloud storage services (Dropbox, iCloud, Google Drive, …) and efficiently versionable with Git.
* I wanted a system simple enough to be used directly with a plain text editor.
* I wanted daily files to automatically reference weekly files, weekly files to reference monthly files, and so on.
* I wanted everything to be based on nested directories and simple UTF-8 encoded text files, to ensure that the data will still be easily readable and writable even 20 years from now.
* I wanted to use Markdown as the file format, so that writing could be done in plain text while still allowing some basic structure and formatting. Markdown is ideal because it represents an approach to expressing style in plain text, rather than being a full document format.
* I wanted all Markdown files to be manually editable at any time using any text editor.
* I wanted everything inside each subdirectory—except the `_index.md` file—to be implicitly treated as an attachment to the corresponding day, week, month, quarter, or year document.
* I wanted to rely only on functions available in the Python standard library (>= 3.11), in order to ensure maximum compatibility and long-term maintainability.

## Time subdivision

Time is subdivided into days, weeks, months, quarters, and years according to the ISO 8601 standard, which defines the week as starting on Monday and ending on Sunday.

* Daily: `{destination}/diary/daily/YYYY/MM/DD/`
* Weekly: `{destination}/diary/weekly/YYYY/WW/`
* Monthly: `{destination}/diary/monthly/YYYY/MM/`
* Quarterly: `{destination}/diary/quarterly/YYYY/QQ/`
* Yearly: `{destination}/diary/yearly/YYYY/`

> Note 1: `WW` is a number from 01 to 53 representing the ISO 8601 week number.  
> Note 2: `QQ` is a number from 01 to 04 representing the quarter.

## Installation

The application can be installed using `pipx` by running the following command:

```
pipx install diario-cli
```

The application expects a configuration file named `config.json` to exist inside the `~/.config/diario/` directory. If the file, the directory, or both do not exist, they will be created automatically with default settings.

Both the destination directory and the default text editor can be changed by editing the configuration file located at `~/.config/diario/config.json`.

These are the default configuration parameters:

```json
{
  "path": "~/.local/share/diario",
  "locale": "en_US",
  "editor": "nano"
}
```

The `editor` parameter can be either a string or a list of strings, for example: `["open", "-a", "/Applications/MarkEdit.app/Contents/MacOS/MarkEdit"]`

## Usage

To start the application and create a document for the current day, run:

```
diario
```

After running the command, the application will create all required documents and invoke the text editor defined in the configuration file. By default, the application will attempt to use the `nano` editor.

To create a document for a specific day, run:

```
diario 24-12-2027
```

To create a document for the day after the current one, run:

```
diario --tomorrow
```

To automatically create all documents starting from today and covering the next 365 days, run:

```
diario --populate
```

For additional options, refer to the built-in help:

```
diario --help
```

## Example directory structure created by the application

```
/Users/cesco/Documents/Diario/
├── diary
│   ├── daily
│   │   ├── 2026
│   │   │   ├── 01
│   │   │   │   ├── 25
│   │   │   │   │   └── _index.md
│   │   │   │   ├── 26
│   │   │   │   │   └── _index.md
│   │   │   │   ├── 27
│   │   │   │   │   └── _index.md
│   │   │   │   ├── 28
│   │   │   │   │   └── _index.md
│   │   │   │   ├── 29
│   │   │   │   │   └── _index.md
│   │   │   │   ├── 30
│   │   │   │   │   └── _index.md
│   │   │   │   └── 31
│   │   │   │       └── _index.md
│   │   │   ├── 02
│   │   │   │   ├── 01
│   │   │   │   │   └── _index.md
│   │   │   │   ├── 02
│   │   │   │   │   └── _index.md
.   .   .   .   .   .
│   ├── monthly
│   │   ├── 2026
│   │   │   ├── 01
│   │   │   │   └── _index.md
│   │   │   ├── 02
│   │   │   │   └── _index.md
│   │   │   ├── 03
│   │   │   │   └── _index.md
│   │   │   ├── 04
│   │   │   │   └── _index.md
│   │   │   ├── 05
│   │   │   │   └── _index.md
│   │   │   ├── 06
│   │   │   │   └── _index.md
│   │   │   ├── 07
│   │   │   │   └── _index.md
│   │   │   ├── 08
│   │   │   │   └── _index.md
│   │   │   ├── 09
│   │   │   │   └── _index.md
│   │   │   ├── 10
│   │   │   │   └── _index.md
│   │   │   ├── 11
│   │   │   │   └── _index.md
│   │   │   └── 12
│   │   │       └── _index.md
.   .   .
│   ├── quarterly
│   │   ├── 2026
│   │   │   ├── 01
│   │   │   │   └── _index.md
│   │   │   ├── 02
│   │   │   │   └── _index.md
│   │   │   ├── 03
│   │   │   │   └── _index.md
│   │   │   └── 04
│   │   │       └── _index.md
.   .   .
│   ├── weekly
│   │   ├── 2026
│   │   │   ├── 04
│   │   │   │   └── _index.md
│   │   │   ├── 05
│   │   │   │   └── _index.md
│   │   │   ├── 06
│   │   │   │   └── _index.md
│   │   │   ├── 07
.   .   .   .
│   └── yearly
│       ├── 2026
│       │   └── _index.md
└── templates
    ├── daily.md
    ├── monthly.md
    ├── quarterly.md
    ├── weekly.md
    └── yearly.md
```
