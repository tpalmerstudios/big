# Help with using `git`

## What is `git`?
Git is a "version control system." It allows you and others to keep track of multiple versions of the same project at the same time. In addition it allows you to experiment with your files without committing to them.

## Pulling and Pushing
Because you can work with other users and on different branches, you need to make sure your copy of the files (repository) is up to date before you edit it or tell others that you have the newest version. This is called pulling. Telling others what the new version is, is called pushing.

Whenever you start work for the day and before you push your work you should always `pull`.
    git pull

Once you have edited some files and `commit`ed them, you must push them.
    git push

You may need to push with the branch name or to a different remote location
    git push -u origin branch-name
    git push -u github branch-name

That just makes sure the other users can see the new version and don't accidently start editing an old version.

## Branching
Anytime you start work on a new part of a project, you should create a branch for that part. This is to make sure the rest of the project is not edited and so that you can revert if you mess up.

To create a new branch
    git branch feature-name
To create a branch and switch to it:
    git switch -c feature-name
To switch to a branch that was already created
    git switch feature-name

If you have edited files but not committed them, note that you will commit them to the branch you commit to. Not the branch you started editing on. If you want to switch to another branch after you edited something, you need to stash the edits, then pop them once you go to the branch you want to save them on.

To temporarily hide your edits (if you want to switch branches)
    git stash
To bring back the files you were working on, but didn't commit
    git stash pop

## Committing
When editing files, they are only edited in your area. If you have other people working on the project or multiple features you're working on simutaneously, you need to save your work in small manageable clumps called `commit`s. These are distinct changes that can be described in a sentence or two. Limit yourself to only editing a few files by a few dozen lines of code (LOC) before committing. Once you commit, it still stays in your area until you push to everyone else. But you cannot push without committing, and you could have several commits per push.

First add all related edits.
    git add filename.txt
    git add file2.css
    git add otherfile.pdf
    git add folder/randomfile.txt

Or if you were organized about it:
    git add .
That adds every file that has been changed in the current folder and it's children

Then commit
    git commit
An editor should pop up and allow you to write a message describing the changes

Or to save a few seconds
    git commit -m "I edited the homepage paragraph"

## Tagging
Once you have a good stopping point you can add tags or version numbers.
We'll try to use "semantic versioning."

This just means the first number are major improvements or changes in how everything works. Often times these are used when you are breaking an older version.

The second number are feature additions or major bug fixes, but not major rewrites.

The third number is for any small updates or bug fixes.

    Major.Minor.Patch-Build_Type
    0.0.24-alpha

We can use this by tagging on the main branch
    git switch main
    git tag v0.1.0-rc

If you mess up you versioning you can add or delete tags like this
    git log --oneline --decorate
    git tag -d v1.0.0 # deletes the tag
    git tag -a v1.0.1 c43e56b
You can add a tag to a commit listed in the git log command

## Merging
I've already mentioned merging in general, but here's a few more specifics. Branches should be used for any unique feature that won't touch other aspects of the project. Any work that is done should not be done on the main branch. The main branch is only for the finalized project, not for day-to-day edits.

To combine your completed work with the current branch
    git merge completed-branch

The key is to make sure you're on the branch that you want to be updated and you have pulled already. If you run into errors in merging. Stop. This is one part where you can easily ruin several hours of work if you're not careful. Fixing merge errors is beyond the scope of this. Ask me if you have questions, and even then, I'll probably have to Google and look things up for several minutes.

## Examples
    git pull # do this before you start editing anything
    git switch -c friday-edits # pick better names for your branches

    # edit your files. focus on specific things. don't edit too much at once. keep them related to the name of your branch

    git add . # that says all files in this folder are part of one issue I worked on
    git commit -m "here's what I did today" # this is you "saving" your work
    git push -u origin friday-edits # make sure everyone has access to your new work
    git switch main # go to the main branch
    git merge friday-edits # now the main branch has your edits
    git branch -d friday-edits # you don't need that branch anymore, so delete it
    git tag v0.1.3 # this will give the most recent commit on main a version

If you need help
    git help branch
    git help merge
    etc.