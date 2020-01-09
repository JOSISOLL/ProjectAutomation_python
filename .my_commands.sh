#!/bin/bash

function create(){
    cd
    python create.py $1
    echo Redirecting to projects folder...
    cd /Users/josiooo/Developer/projects/2020_projects/$1
    git init
    git remote add origin https://github.com/JOSISOLL/$1.git
    touch README.md
    git add .
    git commit -m "initial commit"
    git push -u origin master
    open .
}


#source ~/.my_commands.sh 
