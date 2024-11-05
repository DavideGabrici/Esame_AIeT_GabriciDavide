#!/bin/bash
# download file
wget https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/main/Nemo_6670.dat

# verifica download
if [ $? -eq 0 ] 
then
	echo "Download Nemo_6670.dat completato."
else
	echo "Download Nemo_6670.dat fallito."
fi

export file_path=`pwd`/Nemo_6670.dat

# permessi
chmod +rwx $file_path 

# esecuzione 
python3 Esame_AIeT_GabriciDavide.py $file_path
