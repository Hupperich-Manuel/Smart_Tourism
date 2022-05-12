# Smart_Tourism
Recommendation System for Experiences in a city


## Guide for Contributing to this Repository
<sub>Focus only on the Model repository at the moment since the _WebApp_ is focused soley on the development of the app, and it contains other programming languages than Python.</sub>

* [1. Download **Git**](#0)
* [2. Contribute to the Community](#1)


<a id='0'></a>
#### 1. Download **Git**
[Windows](https://youtu.be/pIbxvTsjqLw)

[MacOS](https://www.youtube.com/watch?v=hMEyBtsuAJE)

<a id='1'></a>
#### 2. Contribute to the Community

Get all the repository/forks in your local machine
```command
$git clone <repository>
```
Information about what changes have happened (In case you havent changed anything there wont appear any indications)
```command
$git status
```
**Do some changes in the repository**
<sub> IF you now run the previous _status_ command you will be able to see that there is a file the needs to be commited</sub>

Before you commit, you need to add the changes
Add a specific file:
```command
 $git add <file>
```
Add all changes:
```
$git add .
```
Now you just have to commit
```
$git commit -m <Text that breifly states the main changes you made. All in ''>
```
Reached this point you will be able to push the changes to _GiHub_
```
$git push origin <your selected branch/ The default one is 'main'>
```

### For forked repos

1. Click on the Fork button on the top right corner of the repository
This will create a copy on your github profile from where you will be able to start making changes

2. Clone the repository
3. Either checkout to a new branch or use the default one _main_ | _master_
4. Make the changes, add, commit and push

This will create a **pull request** which will then be evaluated by the main contributors of the repository and then if everything if fine and correct it will be merged to the original repo.

**Errors**:
In case you are not able to push the changes add the following lines in the command line:
```command
$git config --global --edit
```
 and 
```command
[credential]
  helper = osxkeychain
  useHttpPath = true
```

**To see past versions of a specific file**
```command
$git config --global alias.hist "log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short"
```
```command
$git hist
* fa3c141 2011-03-09 | Added HTML header (HEAD, master) [Alexander Shvets]
* 8c32287 2011-03-09 | Added standard HTML page tags [Alexander Shvets]
* 43628f7 2011-03-09 | Added h1 tag [Alexander Shvets]
* 911e8c9 2011-03-09 | First Commit [Alexander Shvets]
```
```command
$git checkout <hash>
```
```command
cat hello.html
```
```command
$git checkout 911e8c9
Note: checking out '911e8c9'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b new_branch_name

HEAD is now at 911e8c9... First Commit
```
```command
$ cat hello.html
Hello, World!
```
Get back to your default branch
```command
$git checkout master
```






  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

