Nella repository sono presenti tre file:

   1. Un file Esame_AIeT_GabriciDavide.py per la creazione dei grafici richiesti, di cui segue una breve descrizione;
   2. Un file [...]_installazione.sh, per la creazione di una cartella di lavoro nella Home e in cui copiare gli altri due file e salvare le immagini prodotte;
   3. Un file [...]_esecuzione.sh per il download del file Nemo_6670.dat e l'esecuzione del codice Python.

Codice Python. Questo codice, una volta eseguito, produce quattro grafici, salvandoli poi in formato .png nella cartella in cui è stato copiato assieme al codice di esecuzione.

   1. Il primo grafico riporta il Diagramma H-R del campione di stelle in analisi. La selezione delle classi d'età è tale da rendere gli intervalli sempre più ampi al crescere dell'età stellare per una migliore leggibilità del diagramma;
   2. Il secondo grafico riporta la distribuzione della metallicità delle stelle. Queste sono suddivise in tre classi d'età e per ciascuna sono stampate media e mediana e i loro valori sono riportati sul grafico sotto forma di linee verticali;
   3. Il terzo grafico riporta le metallicità espresse in funzione della massa stellare. Viene mantenuta la suddivisione nelle tre classi d'età e i punti sono stampati con gradi di trasparenza diversi nel tentativo di rendere il risultato più apprezzabile;
   4. Il quarto grafico riporta le curve di densità delle distribuzioni di punti nel diagramma precedente nel tentativo di migliorarne ulteriormante la leggibilità.

Per l'esecuzione:

   1. Scaricare i tre file presenti nella repository, un file .py e due file .sh;
   2. Dalla cartella di download, aprire un terminale e fornire in ordine i comandi "chmod +x Esame_AIeT_GabriciDavide_installazione.sh" e "./Esame_AIeT_GabriciDavide_installazione.sh";
   3. Spostarsi nella cartella appena creata in Home, chiamata "Esame_GabriciDavide", e fornire il comando "./Esame_AIeT_GabriciDavide_esecuzione.sh".
