#!/bin/bash

git checkout mbranch
echo "on branch mbranch"
read -p "commit message: " -e commit_msg
cd /workspaces/FlappyExplosion/src
git pull
git add *
git commit -am $commit_msg
echo "Code committed ---------------------------------------------------------------------------------------------"
git push
git merge rohansbranch
git push

git checkout rohansbranch
git pull
git merge mbranch
git push

git checkout mbranch
git merge rohansbranch
git push