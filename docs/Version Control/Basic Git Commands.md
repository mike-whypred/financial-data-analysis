# Basic Git Commands

**-Initialize a Repository**: Create a new Git repository in your project directory.

```bash
git init

```
**-Clone a Repository**: Copy an existing Git repository from a remote server (such as Github) to your local machine.

```bash
git clone https://github.com/username/repository.git

```
**-Check Status**: See the status of your files in the working directory and staging area.

```bash
git status

```


**-Add Files**: Add files to the staging area, preparing them for a commit.

```bash
git add filename
# or add all files
git add .

```

**-Commit Changes**: Save your changes to the local repository with a descriptive message.

```bash
git commit -m "Your commit message"

```


**-Push Changes**: Upload your local commits to a remote repository.

```bash
git push origin branch-name

```

**-Pull Changes**: Fetch and merge changes from a remote repository to your local repository.

```bash
git pull origin branch-name

```


**-Create a Branch**: Create a new branch to work on a separate feature or analysis.

```bash
git branch branch-name

```


**-Switch Branches**: Switch to a different branch.

```bash
git checkout branch-name

```


**-Merge Branches**: Merge changes from one branch into another.

```bash
git checkout main
git merge branch-name

```


**-View Commit History**: See the history of commits in your repository.

```bash
git log

```