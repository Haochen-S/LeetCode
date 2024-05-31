#! /bin/bash

# user input name of javaFile
# read -p "Enter fullname: " fullname
echo -n "Type 1 for Unfinished folder, Type 2 for Finished folder: " 
read folderNumber

echo -n "Enter Fullname: " 
read fullname

if [ $folderNumber -eq 1 ]
then
    # ls ./Unfinished\ Problems/
    java ./Unfinished\ Problems/$fullname.java
    # rm ./Unfinished\ Problems/*.class
elif [ $folderNumber -eq 2 ]
then
    # ls ./Finished/
    javac ./Finished/$fullname.java
    java ./Finished/$fullname.java
    rm ./Finished/*.class
else
    echo "incorrect input, input 1 or 2"
fi

