#!/usr/bin/env bash
# git_clean_commit_hist.sh

git checkout --orphan latest_branch # Checkout new branch
git add -A                          # Add all files and commit them
git commit -am "init"               # Commit with message
git branch -D master                # Deletes the master branch
git branch -m master                # Rename the current branch to master
git push -f origin master           # Force push master branch to github
git gc --aggressive --prune=all     # remove the old files
