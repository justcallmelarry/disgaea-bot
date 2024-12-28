## The instruction file format
The instruction file consists of an action, a button, and an optional wait time.

The instructions are as follows:

| symbol | action  |
| ------ | ------- |
| #      | press   |
| >      | keyDown |
| <      | keyUp   |

If this is followed by a float, the script will sleep for the time specified after running the command.

Additionally you can add comments to the file (a line that starts with // is a comment).


## Useful combinations

### Select first char and choose Special
```
// start and choose first char
#k3.5
#k
#k
// then choose special
#s
#s
#k0.2
```

### Execute, wait for the attack animation, then click on bonus bar page and go back to stage select
```
// execute and back to stage select
#i
#k3.5
#k
#k1.2
```