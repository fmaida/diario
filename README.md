# Diario

Gestisce un diario personale ispirato al bullet journal.  

L'app nasce per rispondere a questi problemi:

* Volevo un sistema di gestione delle note personali, suddiviso per giorni, settimane, mesi, trimestri e anni.
* Volevo un sistema del quale fosse facile e banale creare una copia di sicurezza. In questo caso specifico, basta copiare una singola cartella.
* Volevo un sistema che all'occorrenza fosse facilmente versionabile con Git
* Volevo un sistema talmente semplice da poter essere usato con un semplice editor di testo
* Volevo che i file giornalieri referenziassero automaticamente i file settimanali, e che i file settimanali referenziassero automaticamente i file mensili, e così via
* Volevo che tutto fosse basato semplicemente su cartelle annidate e file di testo, per essere sicuro che anche fra 20 anni i dati siano facilmente leggibili e scrivibili
* Volevo usare come formato file il Markdown, per poter scrivere facilmente in formato testo puro ma poter gestire qualche elemento di stile e formattazione
* Volevo che tutti i file markdown potessero essere modificati manualmente in qualsiasi momento da qualsiasi applicazione di testo

### Come funziona la suddivisione del tempo

La suddivisione del tempo è basata su giorni, settimane, mesi, 
trimestri e anni in base allo standard ISO 8601, che prevede 
che la settimana standard inizi di lunedì e termini di domenica.

* Giornalieri: `{destinazione}/diary/daily/YYYY/MM/DD/`
* Settimanali: `{destinazione}/diary/weekly/YYYY/WW/`
* Mensili: `{destinazione}/monthly/YYYY/MM/`
* Trimestrali: `{destinazione}/quarterly/YYYY/QQ/`
* Annuali: `{destinazione}/yearly/YYYY/`

> Nota 1: `WW` è un numero da 00 a 53 che rappresenta la settimana in base allo standard ISO 8601.  
> Nota 2: `QQ` è un numero da 01 a 04 che rappresenta il trimestre.

### Installazione

Per ora, bisogna scaricare tutto e dalla cartella del progetto bisogna eseguire questo comando:

```
pipx install --force .
```

### Esempio di struttura creata dall'app

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