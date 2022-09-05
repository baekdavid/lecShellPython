#!/bin/bash
awk -F : "/seoul/{print $1}" 

awk '/seoul/ {print $0}' testfile
awk '/seoul|busan/ {print $0}' testfile
awk '(/seoul/ || /busan/) && ($3>25 && $3<60) {print $0}' testfile
grep "seoul" file
awk '{print NR}' file
awk '/seoul/ {print sqrt($3)} file
awk ls -al | awk '{print length($0)}
awk '/seoul/ {print length($0 " " systime() " " cos(3.14)}
awk 'BEGIN {print "seoul"} /seoul/{print} END {print "---"}' file
df -k | awk '{printf "%-15s %-20s\n",$1,$6}'
awk '{sum=0; for(i=2;i<5;i++) sum=sum+$i; print "sum: " sum}' grade.txt
awk -f sum.awk grade.txt

#!/bin/bash

read -p "input num1 num2 num3:" 

if [ "$1 -ge $2 && $1 -ge $3" ]; then

    echo "$1 is Max"
elif [ $2 -ge $1 && $2 -ge $3 ]; then
   echo '$2 is Max'
else
    echo "$3 is Max"
   

fi

#!/bin/bash
for file in $@; do
  if [ -f $file ]; then
    wc -l $file 
  elif [ -d $file]; then
    for subfile in $file/* do
        echo "${subfile}"
    do$file/*

  fi

done  
    echo "${file}"$@

BEGIN	{
    printf "%5 %7s %5s %5s \n", "SUM","AVG", "MAX", "SUBJ"
}
{   sum=0;
    max=0
    title[2]="FR";
    title[3]="EN";
    tigle[4]="MATH";
    
    grade[2]=70;
    grade[3]=80;
    grade[4]=90;
    
    for (i=2;i<=4 ;i++ ) {
        sum=sum+$i;
        if (max<$i) {max=$i; subj=i            
        }
        
    };
    printf "%5s %7.2f %5s %5s \n", sum, sum/3, max, title[subj]
}
    

