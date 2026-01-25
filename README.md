# Diario

Gestisce un diario personale ispirato al bullet journal.  

Diario è un’applicazione fortemente opinionata: le scelte 
di struttura, formato e suddivisione del tempo sono 
intenzionali e non configurabili. Quello che invece è 
configurabile da parte dell'utente sono i file modello 
in formato Markdown all'interno della cartella `templates`.    

L'app nasce per rispondere a questi problemi:

* Volevo un sistema di gestione delle note personali, suddiviso per giorni, settimane, mesi, trimestri e anni.
* Volevo un sistema mantenibile e gestibile nel lungo periodo, idealmente per tutta la vita dell’utente.
* Volevo che i dati dell'app non dipendessero dall’applicazione stessa. **Anche se la mia app smettesse di funzionare o non fosse più mantenuta, tutti i documenti resterebbero leggibili, modificabili e utilizzabili come semplici file Markdown organizzati in cartelle.**
* Volevo un sistema del quale fosse facile e banale creare una copia di sicurezza. In questo caso specifico, basta copiare una singola cartella.
* Volevo un sistema che all'occorrenza fosse facilmente versionabile con Git
* Volevo un sistema talmente semplice da poter essere usato con un semplice editor di testo
* Volevo che i file giornalieri referenziassero automaticamente i file settimanali, e che i file settimanali referenziassero automaticamente i file mensili, e così via
* Volevo che tutto fosse basato semplicemente su cartelle annidate e file di testo, per essere sicuro che anche fra 20 anni i dati siano facilmente leggibili e scrivibili
* Volevo usare come formato file il Markdown, per poter scrivere facilmente in formato testo puro ma poter gestire qualche elemento di stile e formattazione. Il formato Markdown è l'ideale perché rappresenta un'idea di come rappresentare gli stili in un semplice file di testo puro, più che essere un formato documento vero e proprio
* Volevo che tutti i file Markdown potessero essere modificati manualmente in qualsiasi momento da qualsiasi applicazione di testo
* Volevo che tutto ciò che si trova all’interno di ogni sottocartella, ad eccezione del file `_index.md`, venisse considerato implicitamente come ALLEGATO al documento del giorno, della settimana, del mese, del trimestre o dell’anno corrispondente.
* Volevo utilizzare solo funzioni presenti nella libreria standard di Python 3.10-3.13, in modo da garantire la massima compatibilità e manutenibilità del software nel lungo periodo.

### Come funziona la suddivisione del tempo

La suddivisione del tempo è basata su giorni, settimane, mesi, 
trimestri e anni in base allo standard ISO 8601, che prevede 
che la settimana standard inizi di lunedì e termini di domenica.

* Giornalieri: `{destinazione}/diary/daily/YYYY/MM/DD/`
* Settimanali: `{destinazione}/diary/weekly/YYYY/WW/`
* Mensili: `{destinazione}/diary/monthly/YYYY/MM/`
* Trimestrali: `{destinazione}/diary/quarterly/YYYY/QQ/`
* Annuali: `{destinazione}/diary/yearly/YYYY/`

> Nota 1: `WW` è un numero da 00 a 53 che rappresenta la settimana in base allo standard ISO 8601.  
> Nota 2: `QQ` è un numero da 01 a 04 che rappresenta il trimestre.

### Installazione

Per ora, bisogna scaricare tutto e dalla cartella del progetto bisogna eseguire questo comando:

```
pipx install --force .
```

L'app si aspetta che esista un file di configurazione chiamato 
`config.json` all'interno della cartella `~/.config/diario/`. 
Se questo file, cartella o entrambi non esistono, provvederà 
a crearli automaticamente con delle impostazioni predefinite.

È possibile modificare sia la cartella di destinazione che 
l'editor di testo predefinito modificando il file di 
configurazione `~/.config/diario/config.json`.

Questi sono i parametri di default dell'applicazione:

```json
{
  "path": "~/.config/diario/data",
  "locale": "en_US",
  "editor": "nano"
}
```

### Uso

Per lanciare l'app e creare un documento per il giorno corrente, 
da terminale è necessario eseguire questo comando:

```
diario
```

Dopo aver lanciato il comando, l'app creerà tutti i documenti 
richiesti ed invocherà l'editor di testo definito nel file di 
configurazione. Per default, l'app tenterà di invocare l'editor 
`nano`.

Se invece si desidera creare un documento per un giorno 
specifico, è possibile eseguire questo comando:

```
diario 24-12-2027
```

Se si desidera creare un documento per il giorno 
successivo a quello odierno, è possibile eseguire:

```
diario --tomorrow
```

Per creare automaticamente tutti i documenti a partire da oggi e 
per i prossimi 365 giorni, è possibile eseguire:

```
diario --populate
```

Per altri usi, rimando al semplice aiuto in linea invocabile 
con il comando:

```
diario --help
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