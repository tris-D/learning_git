# INTRODUCTION TO VERSION CONTROL AND GIT 

# VERSION CONTROL - create a piece of code, version number 1, multiple versions are safe points
# You can roll back to a previous version by using GIT, you can also compare side by side the new and saved versions

# RETOUCH COMMAND LINE COMMANDS:
# cd: change directory to './directory/location/or/path'
# mkdir: make new folder/directory called 'name'
# ls -a: used in GitBash to view as it shows all the names of files and directories in the current working directory, can also use to see the hidden files
# touch: create new file
# code: open file 'name.file' in VSC to code

# git init: initializes a new empty git repository inside of the current working directory
#                 story is currently the working directory


# OFFICIAL GIT COMMANDS
# next, we need to add the working directory into the staging area byy using:
# git status: checks to see what is currently inside the git staging area, if empty prompted to add by
# git add: adds 'file.name' to staging area/git respository - can write "git add chapter2.txt chapter 3.txt" instead of writing two lines--> even better, you can use: "git add ."
    # git restore --staged <file>: to unstage
# git commit -m "message": message is required to keep a log/track of the commit and versions you made, and best practice to keep message in present tense, for some reason
# git log: view commits you have made - gives you a HASH, assigned to the particular commit, and at the end, it shows your commit message
    # HEAD --> master: current position/state we are in, can move states and versions
# git diff: view differences in versions of "file.name"
# git checkout: roll back to the last saved version saved in the REPOSITORY from the saved version in the WORKING DIRECTORY

# to make commits, you need to have your user identity configured. 
# To set up your Gobal Git Identity (Applies too all repositories):
# git config --global user.name "Your Name"
# git config --global user.email "your.email@example.com"
# Then, we set up your Local Git Identity (specific to this repository only): If you want to set your
# identity for just this repository:
# git config user.name "Your Name"
# git config user.email "your.email@example.com"
# git config --list: see the user settings and information
    # git --no-pager config --list: see it without entering view pager made
    # HOWEVER, if you already entered pager mode, press "q" to quit pager mode

# *SUMMARY
# 1.after initializing git with <git init> command, so the current working directory becomes the official working directory as git 
#   will then track the changes made in the working directory and the local GIT repository

# 2.we then created a file inside our working directory and used <git add> to push it to the staging area - we need this intermediate 
#   staging area between the working directory and the repository because sometimes you want to pick and choose exactly what you want to add to the official repository
#   the STAGING AREA is a place where you can examine and choose all this before making the commits using <git commit>

# 3.now, if we mess up the file we are working on in the current directory, we now have version control, we can revert the changes we made in the working 
# directory by taking which version you want from the versions that you regularly committed from the local repository. Before reversion, we can see 
# the differences (changes made) between the version and the currently saved file in the cwd with <git diff 'file.name'>

# 4.all of this is looking at local version control, next we look at more interconnected version of git using GITHUB


# GITHUB AND REMOTE REPOSITORIES - create and push to a remote repository using Github
# -a remote repository is a repository that is hosted on someone else's server, on someone else's computer using GITHUB
# -to add remote repository:
# git remote add <name> <url>: telling your local repository that I have created a remote repository somewhere on the Internet, and I want to transfer all my commits over there
    # <name>'s default is origin, but you can change this to whatever you want, but hightly reccomended to be named origin, because people are very used to the default
# git push -u <remote name> <branch name>: pushes your local repository to the remote repository by using the -u option (which links up the two repositories)
    # git push -u origin main/master: pushes to the master/main branch of the remote repository
# MAIN BRANCH OF YOUR REMOTE REPOSITORY is where things are pushed to

# HOW TO USE .gitignore - CHOOSE WHICH FILES NOT TO TRACK
# -do not add sensitive files like passwords or api keys or even .DS_stores files
# touch .gitignore: git is looking specifically for this to read to see what files to ignore
# at github.com/github/gitignore, it has specifically made already .gitignore files for different languages that you can copy and paste the raw code from

# PULL FROM REMOTE REPOSITORY TO YOUR OWN LOCAL REPOSITORY AND WORKING DIRECTORY - using .git clone
# establish existing code and build on their code by improving your own version
    # you might want to EXTEND ITS FUNCTIONALITY or FIX A BUG 
    # e.g. self-hosting services for applications, servers

# FEATURE DEVELOPMENT WITH BRANCHES - sometimes you are developing new features, sometimes you are fixing bugs
# _______________________________________________________________________________________________________________
# Main          |v1.0|  ---------------> |v2.0| ------------------> |v3.0|---->|v4..0| ------> |v5.0|
# ____________________________________________________________________________^__________________________________
# ____________________________________________________________________________|__________________________________
# Feature 1                                     |v.alt3.0| --------------> |v4.0|  
# _______________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________
# Feature 2             |v.alt2.0| --------------> |v.alt.alt3.0| ----------------> |v.alt4.0|
# _______________________________________________________________________________________________________________
# MERGE FEATURES BACK INTO MAIN BRANCH OF CODE - FEATURE DEVELOPMENT WITH BRANCHES: .git merge name-of-branch
# git branch: to make a new branch, specify the name of your new branch 'branch_name'
    # without the name, it shows you back what branch you are on - * shows you which branch you are on
# git checkout 'branch_name': switches between branches you are committing to 