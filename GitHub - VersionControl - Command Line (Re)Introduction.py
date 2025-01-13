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

# to make commits, you need to have your user identity configured. 
# To set up your Gobal Git Identity (Applies too all repositories):
# git config --global user.name "Your Name"
# git config --global user.email "your.email@example.com"
# Then, we set up your Local Git Identity (specific to this repository only): If you want to set your
# identity for just this repository:
# git config user.name "Your Name"
# git config user.email "your.email@example.com"
# git config --list: see the user settings and information
