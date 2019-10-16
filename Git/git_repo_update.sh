#!/bin/bash

listOfNames="repo_name1 repo_name2"
for projectName in $listOfNames
do
  cd $projectName
  echo "dir in $projectName"
  sudo git checkout master
  sudo git pull
  echo "git pull complate"
  cd ..
  echo "exit from $projectName"
done
