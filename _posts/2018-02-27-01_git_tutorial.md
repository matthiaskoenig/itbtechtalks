---
layout: post
title: 01 - A quick introduction to git
image: /talks/01_git/github.png
tags: [git, repository]
---

We are facing a reproducibility crisis in Computational Biology and Theoretical Biology. A key tool to make scientific research reproducible, allow cooperative work on files and versioning of resources are version control systems. This talks will give a short introduction to git, a free and open source distributed version control system with
* tiny footprint
* lighning fast performance
* working for everything from small to very large projects.

Articles about computational science are not the scholarship itself, but only advertisment for the scholarship. The actual scholarship it the complete set of instructions which generates the analysis, figures and results. Version control systems support us in making our research accessible and versioning models and computational resources.

## Tutorial
The tutorial gives a short introduction on how to setup a new repository, checking the status, versioning of files and submitting files to remote repositories.

For a online tutorial introducing these steps go to
https://try.github.io/levels/1/challenges/1


### Initialise the repository
A **directory** is a folder for storing multiple files.
A **repository** is a directory where git has been initialized for version 
controlling the files.

```
mkdir itbtechtalks
cd itbtechtalks
watch --color -n0 ls -al --color
watch --color -n0 tree . --al
```

To initialize a Git repository here, type the following command:
```
git init
```
This creates the '.git' directory used to track the files.

### Check status of repository
Next up, let's type the git status command to see what the current state of our project is:
```
git status
```

### Add files to repository
```
cp -R ../itbtechtalks2/01_git/ .
cp ../itbtechtalks2/README.md .
```

We now have untracked files in the repository
```
git status
```
* **staged**: files are ready to be commited
* **unstaged**: files with changes which have not been prepared to be committed
* **untracked**: files aren't tracked by git yet
* **deleted**: files that have been deleted and are waiting to be removed

```
git add README.md
git add 01_git
git status
```

### Commit changes
A commit is a snapshot of our repository. 
```
git commit -m"Add git presentation"
```

### See the change log
```
git log
```

### Add remote repository & push
To push our local repo to the GitHub server we'll need to add a remote repository.
We create a remote repository and add it to git
```
git remote add origin https://github.com/matthiaskoenig/itbtechtalks.git
```
Than we push our local changes to the remote repository.
```
git push -u origin master
```

### Pulling remotely
We can check for changes on our GitHub repository and pull down any new changes by running:
```
git pull origin master
```

### Looking at changes
In this case we want the diff of our most recent commit, which we can refer to using the HEAD pointer
```
git diff HEAD
```

### Reverting changes (Undo)
Files can be reverted to any commit, for instance last commit via
```
git checkout README.md 
```

### Working on a different branch
Branches are what naturally happens when you want to work on multiple features at the same time. You wouldn't want to end up with a master branch which has Feature A half done and Feature B half done.

Rather you'd separate the code base into two "snapshots" (branches) and work on and commit to them separately. As soon as one was ready, you might merge this branch back into the master branch and push it to the remote server.
```
git branch update-readme
git checkout update-readme
```
Make changes and commit.

### Merging changes in master & delete old branch
```
git checkout master
git merge update-readme
git branch -d update-readme
git push
```

## Resources
* https://try.github.io/levels/1/challenges/1
* Perez-Riverol, Y.; Gatto, L.; Wang, R.; Sachsenberg, T.; Uszkoreit, J.; Leprevost, F. d. V.;
Fufezan, C.; Ternent, T.; Eglen, S. J.; Katz, D. S.; Pollard, T. J.; Konovalov, A.; Flight, R. M.;
Blin, K. & Vizcaíno, J. A.
Ten Simple Rules for Taking Advantage of Git and GitHub.
PLoS computational biology, 2016, 12, e1004947
* Blischak, J. D.; Davenport, E. R. & Wilson, G.
A Quick Introduction to Version Control with Git and GitHub.
PLoS computational biology, 2016, 12, e1004668
* Ram, K.
Git can facilitate greater reproducibility and increased transparency in science.
Source code for biology and medicine, 2013, 8, 7
Tutorials
https://try.github.io/levels/1/challenges/1
● Information/Books
https://git-scm.com/
https://git-scm.com/book/en/v2

