# Bloat Cipher
A highly impractical fatty cipher created just for fun!

## How does it work?
Every character in the alphabet has a value attached to it.
Whether it be that "a" is the first letter of the alphabet or
"a" is 97 in ASCII.

The bloat cipher takes the value (n) of every letter and outputs
a "key" n times.

### Basic Mode (Default)
Each letter's value corresponds to their position in the alphabet.
This only supports letters from the English alphabet (a-z).
This mode is case-insensitive.
Attempting to insert a non-alphabetic value will throw a ValueError.

Input:

`abc`

Output:
```
.
..
...
```

### ASCII / Unicode Mode
Each letter's character corresponds to their ASCII / Unicode value.
This mode supports every character in ASCII / Unicode.
This mode is case-sensitive.

Input:

`abc`

Output:
```
.................................................................................................
..................................................................................................
...................................................................................................
```
