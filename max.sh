#!/bin/bash

read -p "input num1 num2 num3:"

if [[ $1 -ge $2 && $1 -ge $3 ]]; then

    echo "$1 is Max"
elif [[ $2 -ge $1 && $2 -ge $3 ]]; then
   echo "$2 is Max"
else
    echo "$3 is Max"
   

fi

