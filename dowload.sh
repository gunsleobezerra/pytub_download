#!/bin/bash

# Verifica se pelo menos dois argumentos foram fornecidos (pasta de destino e pelo menos um link)
if [ "$#" -lt 2 ]; then
    echo "Uso: $0 pasta_de_destino link1 [link2 ... linkN]"
    exit 1
fi

# Obtém a pasta de destino do primeiro argumento
dest_folder="$1"
shift

# Cria a pasta de destino se ela não existir
if [ ! -d "$dest_folder" ]; then
    mkdir -p "$dest_folder"
fi

# Itera sobre cada link fornecido
for link in "$@"; 
do
    # Executa o script Python para cada link, passando a pasta de destino
    python download_video.py "$link" "$dest_folder"
done