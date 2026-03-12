# Git condition 
## Definition of Git  : 
Git is a free and open-source distributed version control system, commonly used for managing and tracking changes in source code during software development. It was created by Linus Torvalds in 2005.

## What Git Does :  
**1- Tracks Changes:** Git records changes to files so you can recall specific versions later.

**2- Collaboration:** Multiple people can work on the same project simultaneously without overwriting each other's changes.

**3- Branching and Merging:** Developers can create branches to work on features independently and later merge them back into the main project.

## How Git Works 
**(1)Repository:** A repository (or "repo") is a directory tracked by Git. It contains the full history of changes to its files.- EXAMPLE: cd my-project
git init -> git status -> git add . -> git commit -m "First commit "  -> git log --oneline -> git checkout a3f9c12 > . 

**(2)Snapshots/Commits::** Git saves your changes as commits, which are like snapshots of your file system at a given point. EXAMPLE: cd my-project
git init -> git status -> git add . -> git commit -m "Snapshot 1: created homepage"  -> git add . -> git commit -m "Snapshot 2: added about page" git log --oneline -> git add . ->
git commit -m "Snapshot 3: updated homepage title" -> git log --oneline -> git checkout a1e3c22 -> git checkout b4f2a11 -> git checkout main -> git show a1e3c22  .  

**(3)Branches:** You can create separate branches to work on different features or bug fixes. The default branch is often called main or master. EXAMPLE: git add . -> git commit -m "First commit "  git branch -
-> git checkout main -> git merge "file name" -> git branch -d "file name" . 

**(4)Merge:** The 2 Types of MergeType 1 — Fast Forward Merge . Type 2 — 3-Way Merge . - You can combine changes from different branches together, which is called merging. EXAMPLE:  git merge <branch> -> Standard merge \ git merge --abort -> Cancel a merge in progress \ git status ->See conflict files
git log --merges ->View all merge commits .

**(5)Distributed:** Every developer has a complete copy of the repository history on their own machine. This means you can work offline easily. EXAMPLE : after add all commit -> git log --oneline ->git fetch origin ->git fetch origin ->   git push origin main -> git pull origin main -> 

## Basic Git Workflow
- Clone: Download a repository from a remote (like GitHub) to your local machine.
- Edit: Make changes to files in your project.
- Add: Stage the changed files with git add.
- Commit: Save the staged changes with git commit -m "message".
- Push: Upload your commits to the remote repository with git push.
- Pull: Get updates from the remote repository with git pull.

# GitHub 
GitHub is a website that hosts Git projects in the cloud, allowing developers to collaborate on the same project from anywhere in the world.

# What Does GitHub Do?
### Stores your code online
### Enables collaboration with your team
### Manages pull requests and code review
### Tracks issues and tasks
### Automates tasks such as testing and deployment

# How Does It Work?
1. Create a Repository → Start your project
2. Clone → Download it to your device
3. Commit → Save your changes
4. Push → Upload it to GitHub
5. Pull Request → Request to merge your code

# of The End  -> Git vs. GitHub
Git → A program on your device → Tracks changes locally .
GitHub → A website in the cloud → Shares and stores your code online. 



