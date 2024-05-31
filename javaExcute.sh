#! /bin/bash

echo -n -e "1 for Unfinished\n2 for Finished\n3 for Optimized: "

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
elif [ $folderNumber -eq 3 ]
then
    # ls ./Optimized/
    javac ./Optimized/$fileName.java
    java ./Optimized/$fileName.java
    rm ./Optimized/*.class
else
    echo "incorrect input, input 1 or 2"
fi

