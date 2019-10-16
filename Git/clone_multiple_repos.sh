#!/bin/bash

token='Access_token'
user_name='git_user_name'
listOfNames="repo_name1 repo_name2 repo_name3 repo_name4"
for projectName in $listOfNames
do
  git clone https://$token@github.com/$user_name/$projectName.git
done
