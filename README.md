# The release kinda works.
> [!INFO]
> The counting feature has been removed, duplicate profiles will be delted with the
> latest profile being kept while the oldest delted.


## Welcome to PmPy aka. Password manger python... (still working on a better name)

> [!WARNING]
> This is in **Alpha**


### What can it do
It's simple really. It's a python password manager using Cryptography python library and json library to store passwords and raw python.
> [!NOTE]
> More features and libraries will be implemented in the future remember this is a prototype.
### Syntax
*Because every project of mine has one these days.*

| Syntax | Description |
| ----------- | ----------- |
| SHOW | Shows all stored passwords |
| GET | Shows a specific login |
|SAVE | Saves the temporary directory|
|NEW | Initializes prompt for new login |
|DELETE | Deletes specfied "profile" (Username password combo)|
|EXIT | Quits the program without saving the un-saved profiles|

### Goals

- [ ] Save passwords in a file (.txt, .json, .sql , etc.)
- [x] Be able to run this as a binary (.exe)
- [ ] MacOS support (for .app) has not been finished yet. 
- [ ] More security features.
- [x] And make the syntax applicable, as it doesn't work nor have an interface
  for it  yet


The release doen't work, upon further inspection I have a problem with the counting. The code counts upwards for each new profile, to remember the count it save it in a txt file. And that as of now doesn't work. You will be notified when this is worked out but for this week it is going to be left broken.
