# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 19:28:00 2020

@author: crein
"""

GIT CONFIG

With Git, there are many configurations and settings possible. git config is how to assign these settings. Two important settings are user user.name and user.email. These values set what email address and name commits will be from on a local computer. With git config, a --global flag is used to write the settings to all repositories on a computer. Without a --global flag settings will only apply to the current repository that you are currently in.

There are many other variables available to edit in git config. From editing color outputs to changing the behavior of git status. Learn about git config settings in the official Git documentation.

git config --global user.name "My Name"
git config --global user.email "user@domain.com"
git config --global core.editor "notepad++.exe -multiInst -nosession"
git config --global --list # a list of your configuration settings
git config --global -e # invokes your default editor with the git config file



Usage:

$ git config <setting> <command>
In Practice:

# Running git config globally
$ git config --global user.email "my@emailaddress.com"
$ git config --global user.name "Brian Kerr"

# Running git config on the current repository settings
$ git config user.email "my@emailaddress.com"
$ git config user.name "Brian Kerr"





GIT INIT

Initializes a git repository – creates the initial .git directory in a new or in an existing project. Example:

pwd --full pathname of the current working directory
ls -- listing the contents of a directory or directories
ls -al   
cd ..
git status
master branch is the default branch
notepad++ make_a_new_file

git ls-files  --list of files being tracked by git

git help log



GIT REMOTE
Working with remote repositories

To connect a local repository with a remote repository. A remote repository can have a name set to avoid having to remember the URL of the repository.

Usage:

# Add remote repository
$ git remote <command> <remote_name> <remote_URL>

# List named remote repositories
$ git remote -v
In Practice:

# Adding a remote repository with the name of beanstalk
$ git remote add origin git@account_name.git.beanstalkapp.com:/acccount_name/repository_name.git

# List named remote repositories
$ git remote -v
origin git@account_name.git.beanstalkapp.com:/acccount_name/repository_name.git (fetch)
origin git@account_name.git.beanstalkapp.com:/acccount_name/repository_name.git (push)
Note: A remote repository can have any name. It’s common practice to name the remote repository ‘origin’.



GIT CLONE
To create a local working copy of an existing remote repository, use git clone to copy and download the repository to a computer. Cloning is the equivalent of git init when working with a remote repository. Git will create a directory locally with all files and repository history.

Usage:

$ git clone <remote_URL>
In Practice:

$ git clone git@account_name.git.beanstalkapp.com:/acccount_name/repository_name.git
Cloning into 'repository_name'...
remote: Counting objects: 5, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 5 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (5/5), 3.08 KiB | 0 bytes/s, done.
Checking connectivity... done.



GIT LOG

To show the chronological commit history for a repository. This helps give context and history for a repository. git log is available immediately on a recently cloned repository to see history.

Usage:

# Show entire git log
$ git log

# Show git log with date pameters
$ git log --<after/before/since/until>=<date>

# Show git log based on commit author
$ git log --<author>="Author Name"
In Practice:

# Show entire git log
$ git log
commit 4c0f37c711623d20fc60b9cbcf393d515945952f
Author: Brian Kerr <my@emailaddress.com>
Date:   Tue Oct 25 17:46:11 2016 -0500

    Updating the wording of the homepage footer 
    
commit 0254c3da3add4ebe9d7e1f2e76f015a209e1ef67
Author: Ashley Harpp <my@emailaddress.com>
Date:   Wed Oct 19 16:27:27 2016 -0500

    My first commit message

# Show git log with date pameters
$ git log --before="Oct 20"
commit 0254c3da3add4ebe9d7e1f2e76f015a209e1ef67
Author: Ashley Harpp <my@emailaddress.com>
Date:   Wed Oct 19 16:27:27 2016 -0500

    My first commit message

# Show git log based on commit author
$ git log --author="Brian Kerr"
commit 4c0f37c711623d20fc60b9cbcf393d515945952f
Author: Brian Kerr <my@emailaddress.com>
Date:   Tue Oct 25 17:46:11 2016 -0500



ADDING CHANGES TO THE STAGING INDEX FROM THE WORKING DIRECTORY

git add .  to add all files in the working directory recursively
git add file (now file in staging index and git is tracking the file)
use git add -A  '''when using bashes mv command it stages all files, will add and
update any changes to the working directory'''
use git add -A  to add changes including nested recursive files 
to the staging index





COMMIT MESSAGING
git commit (for multiline commit messages)
git commit -m for commit with inline message
git commit -am to commit changes directly from the working directory to the local repository
change is now part of gits commit history
git commit -a  - commits changes with the a message from the editor of your choice
git commit --amend - change the last commit




unzip ~/Downloads/filename unzip a file into your git project file

git mv oldfilename newfilename




GIT STATUS

This command returns the current state of the repository.

git status will return the current working branch. If a file is in the staging area, but not committed, it shows with git status. Or, if there are no changes it’ll return nothing to commit, working directory clean.

Usage:

git status
In Practice:

# Message when files have not been staged (git add)
git status
On branch SecretTesting
Untracked files:
  (use "git add <file>..." to include in what will be committed)

  	homepage/index.html

# Message when files have been not been committed (git commit)
$ git status
On branch SecretTesting
Your branch is up-to-date with 'origin/SecretTesting'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   homepage/index.html

# Message when all files have been staged and committed 
$ git status
On branch SecretTesting
nothing to commit, working directory clean


GIT PULL

To get the latest version of a repository run git pull. This pulls the changes from the remote repository to the local computer.

Usage:

$ git pull <branch_name> <remote_URL/remote_name>
In Practice:

# Pull from named remote
$ git pull origin staging
From account_name.git.beanstalkapp.com:/account_name/repository_name
 * branch            staging    -> FETCH_HEAD
 * [new branch]      staging    -> origin/staging
Already up-to-date.

# Pull from URL (not frequently used)
$ git pull git@account_name.git.beanstalkapp.com:/acccount_name/repository_name.git staging
From account_name.git.beanstalkapp.com:/account_name/repository_name
 * branch            staging    -> FETCH_HEAD
 * [new branch]      staging    -> origin/staging
Already up-to-date.


GIT PUSH

Sends local commits to the remote repository. git push requires two parameters: the remote repository and the branch that the push is for.

Usage:

$ git push <remote_URL/remote_name> <branch>

# Push all local branches to remote repository
$ git push —all

In Practice:
# Push a specific branch to a remote with named remote
$ git push origin staging
Counting objects: 5, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 734 bytes | 0 bytes/s, done.
Total 5 (delta 2), reused 0 (delta 0)
To git@account_name.git.beanstalkapp.com:/acccount_name/repository_name.git
   ad189cb..0254c3d  SecretTesting -> SecretTesting




DELETE FILES
 
 git rm 'file name'
 
 rm -rf file removes file from the working tree and the index,
-r(Allow recursive removal when a leading directory name is given)
-f(force)
 
 git reset HEAD 'file name' '''to unstage the file deletion but does not 
 restore the file back to the file system'''
 
 git checkout -- 'file name' '''to restore the file back to the file system'''

   
git rm
Remove files or directories from the working index (staging area). With git rm, there are two options to keep in mind: force and cached. Running the command with force deletes the file. The cached command removes the file from the working index. When removing an entire directory, a recursive command is necessary.

Usage:

# To remove a file from the working index (cached):
$ git rm --cached <file name>

# To delete a file (force):
$ git rm -f <file name>

# To remove an entire directory from the working index (cached):
$ git rm -r --cached <directory name>

# To delete an entire directory (force):
$ git rm -r -f <file name>
In Practice:

# To remove a file from the working index:
$ git rm --cached css/style.css
rm 'css/style.css'

# To delete a file (force):
$ git rm -f css/style.css
rm 'css/style.css'

# To remove an entire directory from the working index (cached):
$ git rm -r --cached css/
rm 'css/style.css'
rm 'css/style.min.css'

# To delete an entire directory (force):
$ git rm -r -f css/
rm 'css/style.css'
rm 'css/style.min.css'



GIT MV

git mv 'file'  'new file name'  to move/rename filess git
will stage the change that a rename has taken place


mv  is bashes rename command  git will see this as two operations
as a delete file and a new file added must add to the staging index
use git add -A  to add changes including nested recursive files 
to the staging index

git mv to move a file to another directory

use git add -A  '''when using bashes mv command it stages all files, will add and
update any changes to the working directory'''

"git add -u" only adds currently tracked files 
(which have been modified) to the staging area
 and also checks if they have been deleted 
 (if yes, they are removed from staging area). 
 This means that it does not stage new files.



GIT HISTORY

GIT LOG
 
git log  # To show the chronological commit history for a repository. This helps give context and history for a repository. git log is available immediately on a recently cloned repository to see history.

git log --abbrev-commit # gives a shortened shah number id

git log -- oneline --graph --decorate '''compresses entries into 1 line with
an ascii graph showing the branching graph with annotations'''

git log shah....shah # this specifies a range of commits

git log --since='3 days ago' # date based searching
        --before
        --after
        
        
        
git log -- 'file name' # commits that involve that specific file

git log --follow -- 'path to the file' # follow the renames within that file path

git show 'shah number' # will display the commit history from that specific change set


Usage:

# Show entire git log
$ git log

# Show git log with date pameters
$ git log --<after/before/since/until>=<date>

# Show git log based on commit author
$ git log --<author>="Author Name"
In Practice:

# Show entire git log
$ git log
commit 4c0f37c711623d20fc60b9cbcf393d515945952f
Author: Brian Kerr <my@emailaddress.com>
Date:   Tue Oct 25 17:46:11 2016 -0500

    Updating the wording of the homepage footer 
    
commit 0254c3da3add4ebe9d7e1f2e76f015a209e1ef67
Author: Ashley Harpp <my@emailaddress.com>
Date:   Wed Oct 19 16:27:27 2016 -0500

    My first commit message

# Show git log with date pameters
$ git log --before="Oct 20"
commit 0254c3da3add4ebe9d7e1f2e76f015a209e1ef67
Author: Ashley Harpp <my@emailaddress.com>
Date:   Wed Oct 19 16:27:27 2016 -0500

    My first commit message

# Show git log based on commit author
$ git log --author="Brian Kerr"
commit 4c0f37c711623d20fc60b9cbcf393d515945952f
Author: Brian Kerr <my@emailaddress.com>
Date:   Tue Oct 25 17:46:11 2016 -0500





GIT BRANCHING

To determine what branch the local repository is on, add a new branch, or delete a branch.


git branch  list all of the global branches

git branch -a  to list local and remote branches

git branch 'name of branch'  to create a new branch

git checkout 'name of branch' to switch to another branch

git branch -m 'old name' 'new name' to rename a branch

git branch -d 'name of branch'  to delete a branch

git checkout -b 'name of branch'  creates a branch, then checks it out

git diff 'branch 1' 'branch 2'  see differences between branches

git difftool 'branch 1' 'branch 2'  see differences between branches

git merge 'name of source branch you want merged into the current branch'



Usage:

# Create a new branch
$ git branch <branch_name>

# List all remote or local branches
$ git branch -a

# Delete a branch
$ git branch -d <branch_name>
In Practice:

# Create a new branch
$ git branch new_feature

# List branches
$ git branch -a
* SecretTesting
  new_feature
  remotes/origin/stable
  remotes/origin/staging
  remotes/origin/master -> origin/SecretTesting
  
# Delete a branch
$ git branch -d new_feature
Deleted branch new_feature (was 0254c3d).
git checkout
To start working in a different branch, use git checkout to switch branches.

Usage:

# Checkout an existing branch
$ git checkout <branch_name>

# Checkout and create a new branch with that name
$ git checkout -b <new_branch>
In Practice:

# Switching to branch 'new_feature'
$ git checkout new_feature
Switched to branch 'new_feature'

# Creating and switching to branch 'staging'
$ git checkout -b staging
Switched to a new branch 'staging'



ADVANCED GIT COMMANDS


GIT ALIAS

git config --global alias.(name of the command) "git command you want aliased"
(gobal allows the alias to be available regardless of the repository)

alias will be in alias section of the .gitconfig file


OPEN GIT CONFIG FILE(USING NOTEPAD++)

notepad++ ~/.gitconfig



GIT IGNORE

files for git tracking to ignore

create .gitignore file and store those files you want git to ignore

can ignore directories, files, file patterns




VISUAL DIFF/MERGE TOOL

# configure your merge tool

git config --global merge.tool p4merge
git config --global mergetool.p4merge.path "C:/Program Files/Perforce/p4merge.exe"
git config --global diff.tool p4merge
git config --global difftool.p4merge.path "C:/Program Files/Perforce/p4merge.exe"


# do not prompt p4merge to launch every time you want to resolve a conflict 
git config --global difftool.prompt false
git config --global mergetool.prompt false


git diff  # working directory compared with the staging index

git difftool # working directory compared with the staging index


git diff HEAD # working directory compared to the last commit in the local repository

git difftool HEAD # working directory compared to the last commit in the local repository


git diff --staged HEAD # staging index compared to the last commit in the local repository

git difftool --staged HEAD # staging index compared to the last commit in the local repository



git diff -- 'File you want to compare' # comparing only the specified file in the working directory  to the last commit in the local repository
git difftool -- 'File you want to compare' # comparing only the specified file in the working directory  to the last commit in the local repository



git diff reference shah 1  HEAD # difference between all changes from reference shah1 to the latest commit
git diff reference shah 1  reference shah2 # difference between all changes from reference shah1 to reference shah2
git diff HEAD HEAD^ # difference between latest commit and latest commit  minus 1
git difftool reference shah 1  HEAD # difference between all changes from reference shah1 to the latest commit



git diff master origin/master # comparing the differenct branches of the local and remote repositories
git difftool master origin/master # comparing the differenct branches of the local and remote repositories



GIT MERGING

Integrate branches together. git merge combines the changes from one branch to another branch. For example, merge the changes made in a staging branch into the stable branch.

git merge 'name of source branch you want merged into the current branch'

git mergetool


FAST FORWARD MERGE
"""
In this most commonly used merge strategy, history is just one straight line. When you create a branch, 
make some commits in that branch, the time you’re ready to merge, there is no new merge on the master. 
That way master’s pointer is just moved straight forward and history is one straight line.

"""

RECURSIVE MERGE
"""
In Recursive merge, after you branch and make some commits, there are some new original commits
on the ‘master‘. So, when it’s time to merge, git recurses over the branch and creates a 
new merge commit. The merge commit continues to have two parents.

"""

Usage:

# Merge changes into current branch
$ git merge <branch_name>
In Practice:

# Merge changes into current branch
$ git merge new_feature
Updating 0254c3d..4c0f37c
Fast-forward
 homepage/index.html | 297 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 297 insertions(+)
 create mode 100644 homepage/index.html




GIT REBASE

git rebase master(source branch)

"""

Rebasing is changing the base of your branch 
from one commit to another making it appear as if 
you'd created your branch from a different commit. 
The primary reason for rebasing is to maintain a linear project history.
Will allow a fast forward merge when you are done working on secondary branch to master

"""

git rebase --abort    --to abort a rebase

git mergetool to resolve a merge conflict
git rebase --continue  after you have resolved the rebase conflict

git fetch -- updates the references between the remote and local repositories w/o merging the content in the local repository unlike git pull




-- from the local repository keep changes ahead of remote repository  with the benefit of the the changes made on the remote repository

git pull --rebase origin master





STASHING

"""
git stash temporarily shelves (or stashes) changes you've
made to your working copy so you can work on something
else, and then come back and re-apply them later on. 
Stashing is handy if you need to quickly switch context 
and work on something else, but you're mid-way through 
a code change and aren't quite ready to commit.

"""

git stash - to save the stash (will only stash tracked files  `git ls-files` )

git stash apply  - to reapply the saved stash to the working directory

git stash list - to list the stashes, the latest stash will be @index{0}

git stash drop - drops the last stash

git stash -u - git stash command will now include any untracked files that are not being excluded by git ignore

git stash pop  - applies the stash and drops the latest stash


git stash save "message" to differentiate when working with multiple stashes

`reflog syntax`
git stash show stash@{0} to show a specific stash
git stash apply stash@{0} to reapply a specific stash
git stash drop stash@{0} to drop a specific stash

git stash clear  to drop all remaining stashes

git stash branch "name of new branch" to save the latest stash to a new branch

"""
a new branch is created

switched into the new branch

the stash is applied

the stash is dropped

"""

Usage:

# Store current work with untracked files
$ git stash -u

# Bring stashed work back to the working directory
$ git stash pop
In Practice:

# Store current work
$ git stash -u
Saved working directory and index state WIP on SecretTesting: 4c0f37c Adding new file to branch
HEAD is now at 4c0f37c Adding new file to branch

# Bring stashed work back to the working directory
$ git stash pop
On branch SecretTesting
Your branch and 'origin/SecretTesting' have diverged,
and have 1 and 1 different commit each, respectively.
  (use "git pull" to merge the remote branch into yours)
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (3561897724c1f448ae001edf3ef57415778755ec)




TAGGING

# labels to mark signigicant events or milestones, or versions numbers in your source code

git tag 'name of tag' # Lightweight tag, will apply the tag to the current  commit

git tag --list # list of tags

git show 'name of tag' #Commit that's at that tag

git tag --delete # Delete tag


git tag -a 'name of tag' 'add message in your chosen text editor' #annotated tag has an equivalent commit message added (or git tag 'tag name' -m for an inline message)

git diff 'tag name 1' 'tag name 2'  #comparing differences between tags
git difftool 'tag name 1' 'tag name 2'  #comparing differences between tags


git tag -a 'name of tag' 'commit #' #to go back and apply a tag after the commit, will need to supply a new commit message

git tag -a 'name of tag' -f 'correct commit id to associate this tag with' #to change the commit id associated with an existing tag, will need to supply a new commit message

git push origin 'tag name'  #to push a single tag to your remote repository

git push origin 'name of branch' --tags #will synchronize your branch and push all of your local tags to your remote repository

git push origin: 'tag name'# with no new changes to push or push nothing

"""
this means push nothing with this tag name to your
remote repository effectively deleting it from 
your remote repository(it will still be on your local repsitory)

"""



GIT REFLOG
GIT RESET


git reflog - will actual show you the log , everthing you have done in the past 60 days

git reset soft - points the header pointer to a new location(least destructive)
git reset mixed(default) - reset the staging index,  moves head to your desired location(mixed destruction)
git reset hard - resets both the staging index and the working directory, moves head to your desired location(most destructive)


git reset HEAD^ - go up 1 commit
git reset HEAD^^^ - go up 3 commits
git reset HEAD@{2} - to move to that commit in the reflog

git reset `shah` - move to the commit associated with that shah



CHERRY PICK

"""
git cherry-pick enables arbitrary Git commits to be picked by reference
and appended to the current working HEAD. It allows the picking of a 
commit from one branch and applying it to another.
git cherry-pick can be useful for undoing changes. 

"""

git cherry pick `commit shah`






































README FILE

MARK DOWN FILE
# FIRST LEVEL HEADING

## SECOND LEVEL HEADING















        
        

 
 
 
 
 
 












