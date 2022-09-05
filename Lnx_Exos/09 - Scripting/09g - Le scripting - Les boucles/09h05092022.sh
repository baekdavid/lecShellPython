function monGenerateurDeMotDePasse () { # ./monGMDP $1
    len=$1
    if [ -z $1 ]; then
         len == 8 # if $1 == nul then len==8u
   
    fi
    
randomString=$(tr -dc A-Za-z0-9 </dev/urandom | head -c $len ;
     echo 'votre MDP est : $randomString')


}


=================================================================

#!/bin/bash

echo 'Bjr $1'


000000000000000000000000000000000000000000000000000000000000000000000
#Linuxhint.com
while read -r line; do
replaced=$(echo -e "${string}" | sed -e 's/find/replace/g')

    echo "[$line"
done < fichier.conf






echo "sample header" > "/path/to/file"
echo # Empty line
for line in "${lines[@]}"; do
    echo "${line}" >> "/path/to/file" # >> means append
done

cat >"FichierConverti.txt" <<EOF
first line
second line
...
EOF

fx