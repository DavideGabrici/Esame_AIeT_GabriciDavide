#!/bin/bash
# creazione di una cartella in home e copia in essa di Esame_AIeT_GabriciDavide_esecuzione.sh ed Esame_AIeT_GabriciDavide.py
path_esame="$HOME/Esame_GabriciDavide"
mkdir -p "$path_esame"
cp Esame_AIeT_GabriciDavide_esecuzione.sh Esame_AIeT_GabriciDavide.py "$path_esame"

# permessi
chmod +x "$path_esame/Esame_AIeT_GabriciDavide_esecuzione.sh"

# variabili da aggiornare
var_agg=0
# controllo che la cartella sia nel PATH
if [[ ":$PATH:" != *":$path_esame:"* ]]
then
    echo "export PATH=\"$path_esame:\$PATH\"" >> "$HOME/.bashrc"
    var_agg=1
fi
# controllo che la cartella sia nel PYTHONPATH
if [[ ":$PYTHONPATH:" != *":$path_esame:"* ]]
then
    echo "export PYTHONPATH=\"$path_esame:\$PYTHONPATH\"" >> "$HOME/.bashrc"
    var_agg=1
fi

# aggiorna se necessario
if [[ $var_agg -eq 1 ]]
then
    source "$HOME/.bashrc"
fi
