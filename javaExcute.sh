#! /bin/bash

echo -n "Type 1 for Unfinished folder, Type 2 for Finished folder: " 
read folderNumber

echo -n "Enter fileName: " 
read fileName

if [ $folderNumber -eq 1 ]
then
    # ls ./Unfinished\ Problems/
    javac ./Unfinished\ Problems/$fileName.java
    java ./Unfinished\ Problems/$fileName.java
    rm ./Unfinished\ Problems/*.class
elif [ $folderNumber -eq 2 ]
then
    # ls ./Finished/
    javac ./Finished/$fileName.java
    java ./Finished/$fileName.java
    rm ./Finished/*.class
else
    echo "incorrect input, input 1 or 2"
fi

