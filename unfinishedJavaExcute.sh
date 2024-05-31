#! /bin/bash

echo -n "Enter fileName: " 
read fileName

javac ./Unfinished\ Problems/$fileName.java
java ./Unfinished\ Problems/$fileName.java
rm ./Unfinished\ Problems/*.class