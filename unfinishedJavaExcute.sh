#! /bin/bash

echo -n "Enter fileName: " 
read fileName

if [ $folderNumber -eq 1 ]
then
    # ls ./Unfinished\ Problems/
    java ./Unfinished\ Problems/$fileName.java
    # rm ./Unfinished\ Problems/*.class
elif [ $folderNumber -eq 2 ]
then
    # ls ./Finished/
    javac ./Finished/$fileName.java
    java ./Finished/$fileName.java
    rm ./Finished/*.class
else
    echo "incorrect input, input 1 or 2"
fi

