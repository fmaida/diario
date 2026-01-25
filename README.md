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

### Come funziona la suddivisione del tempo

La suddivisione del tempo è basata su giorni, settimane, mesi, 
trimestri e anni in base allo standard ISO 8601, che prevede 
che la settimana standard inizi di lunedì e termini di domenica.

### Installazione

Per ora, bisogna scaricare tutto e dalla cartella del progetto bisogna eseguire questo comando:

```
pipx install --force .
```
