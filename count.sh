#!/bin/bash
#loads file from server if file is not already in current directory
#idea from: https://devconnected.com/how-to-check-if-file-or-directory-exists-in-bash/
FILENAME="./README"
if ! [[ -f $FILENAME ]]
then 
    wget 'ftp://sunsite.informatik.rwth-aachen.de/pub/mirror/ibiblio/gnome/README'
fi
#converts upper to lowercase, removes punctuation,converts spaces to new lines,sorts words alphabetically,  counts most frequent words, sorts by word occurences, ectracts 2nd word of each line and prints the first 10 words
#used ideas from:
#https://stackoverflow.com/questions/18234378/using-sed-to-split-a-string-with-a-delimiter for spliiting the words on delimiter
#https://unix.stackexchange.com/questions/41479/find-n-most-frequent-words-in-a-file for finding the 10 most frequent words
#https://stackoverflow.com/questions/25491847/extract-the-second-word-in-a-line-from-a-text-file for exttraction of words without numbers
output=$(cat $FILENAME| tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]'| sed 's/[[:space:]]/\n/g'| sort | uniq -c |sort -nr | awk '{print $2}'| head -10) 
echo $output


