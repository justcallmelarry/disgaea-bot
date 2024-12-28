## Installation

Use [uv](https://docs.astral.sh/uv/) to run. This will automatically handle that the correct dependencies, and the correct Python version is used.

```
uv run main ./path-to-instruction-file.txt --iterations 100
```

Once you have run the script, make sure that you are on the correct stage in stage select, then press F8 to start.

## The Instruction File Format

The instruction file consists of an action, a button, and an optional wait time.

The instructions are as follows:

| Symbol | Action  |
| ------ | ------- |
| #      | press   |
| >      | keyDown |
| <      | keyUp   |

If this is followed by a float, the script will sleep for the time specified after running the command.

Additionally you can add comments to the file (a line that starts with `//` is a comment).

## Examples

### CoO3 With Winged Slayer

```
// start and choose first char
#k3.5
#k
#k
// then choose special
#s
#s
#k0.2
// then choose winged slayer
#s
#s
#s
#k
// face the correct way, then move char in winged slayer select mode
#d
>i
#d
<i
#k
// execute and back to stage select
#i
#k3.5
#k
#k1.2
```

### Demonhall Mirror With Winged Slayer

```
// start and choose first char
#k3.5
#k
#k
// then choose special
#s
#s
#k0.2
// then choose winged slayer
#s
#s
#s
#k
// face the correct way, then move char in winged slayer select mode
#w
>i
>w0.8
<w
<i
#k
// execute and back to stage select
#i
#k3.5
#k
#k1.2
```

### Tera Star At CoO3

```
// start and choose first char
#k3.5
#k
#k
// then choose special
#s
#s
#k0.2
// choose tera star
#e
#e
#k
// choose 3x3
#d
#d
#k
// select the enemies
#d
#d
#d
#k
// execute and back to stage select
#i
#k3.5
#k
#k1.2
```
