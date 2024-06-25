Title: Conventions for shell scripts
Date: 2024-06-25 12:00
Summary: Rules for well-behaved shell scripts.

Unix shells are a powerful tool, in a giving-you-enough-rope-to-hang-yourself
kinda way. A lot of their power comes from the fact that pretty much any
Unix-like system from the last 30 years will have a copy of Bash, meaning that
your shell script will work there. You don't have to worry about about
installing Python libraries (or Python itself); you don't need a compilation
step and have to worry about different architectures. It's just a simple file
that your users can download and run.

With great power comes great responsibility, and it's very, very easy to end up
writing scripts that are unusable and unmaintainable. Over the years I've
collected a few principles that can help make the difference between a handy
tool and a loaded footgun.

[TOC]

## Bail out on error: `set -e`

Unless you're doing something very exotic, every shell script should start with
`set -e` (see [The Set Builtin](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html)).

If a command in a script fails, the script should bail out rather than
continuing blindly, which at best would give confusing output, and at worst
could really mess things up.

## Include usage instructions

It's all too easy to spend all morning writing a script that does what you
need, give it a name like `docs.sh`, and walk away. But then the next person
that has to use the script (which might be you, in a few weeks' time) has no
real idea what the script actually does. In this case, something to do with
documentation, presumably, but does it generate documentation or something
else? Where does it put the generated documentation? Can I get it to put the
documentation somewhere else? And so on. The last thing I want to have to do is
start reverse-engineering a shell script.

At the very least, all scripts should start with a line or two of comments
saying what that script does. What are its inputs, where does it put its
outputs? What arguments does it take, if any? Do any environment variables
affect its behaviour?

Better yet, consider making it print out a usage message (when you run it with
the wrong arguments, or with `-h`) with that information. This can be a bit
overkill for a simple script, but if I had my way, every executable script in
the world would print out a detailed usage message when you run it with a `-h`
argument.

If you do support `-h`, there's not much point duplicating the text into a
comment (the two will only end up getting out of sync). Do make it easy to find
for *readers*, rather than *users*, of the script, though: for example, put it
in a `usage()` function near the top of the script.

## Don't rely on working directory

Scripts shouldn't rely on being run from a specific directory. If my project has a
script called `process`, I should be able to run it from the project directory
(as `./process`), but it shoud *also* work if I run it from somewhere
completely different, as `~/projects/myproj/process`.

This is often easy, but if your script runs other commands in your project, or
uses input data from your project, you may need to think about it a bit. In
these cases, `dirname "$0"` is your friend. It gives the directory containing
your script, no matter how your script was run.

Having said that:

## Avoid `cd`

If my `process` script takes an argument which is the name of the file to be
processed, what should happen when I run `~/projects/myproj/process input`?

Obviously, it ought to "process" the file called `input` *in the current
directory*. It should *not* process the file called `input` in some completely
different directory (such as `~/projects/myproj`).

It's often tempting to hardcode a `cd` command into a shell script, especially
if there are other sub-scripts which might need to be run, but of course that
will break this expectation. As a user, I can work around it by saying
``~/projects/myproj/process `pwd`/input``, but that's annoying and I'll
probably only realise I have to do it too late. In short, it does not match my
expectations as a user.

Any use of `cd` is a bit of a red flag, but it's particularly important to
avoid it in scripts that take filenames as arguments (or via environment
variables).

Instead, the best alternative is to make any references to other scripts or
data absolute. Instead of writing:

```sh
# Don't do this
cd `dirname "$0"`
./subprocess "$1"
```

... you can instead write:

```sh
projdir=`dirname "$0"`
"$projdir/subprocess" "$1"
```

Alternatively, you can convert each of your arguments to absolute paths (with
[`realpath`](https://man7.org/linux/man-pages/man1/realpath.1.html)) before
changing directory.

Either way, it's a bit more verbose, but at least you won't end up writing your
output  over something important.

## Correctly handle whitespace in filenames

Filenames with whitespace are a common pitfall for shell scripts. Handling them
correctly means remembering a few points.

* First of all, surround references to any variable that contains a filename
  with double quotes. In the example above, we wrote `"$projdir/subprocess"
  "$1"`. This is because either `$projdir` or `$1` might contain a space, and
  we want both parts of the command to be passed to the operating system as a
  complete word. (Note that `"$projdir/subprocess"` is equivalent to
  `"$projdir"/subprocess`. I just prefer the former, since it reflects that
  `$projdir/subprocess` is a complete unit.)

    You might reasonably ask at this point "what happens if my filename contains
  a double-quote?" And the answer is: nothing. The format above works just
  fine. Bash remembers that the `"` character came from a variable expanision,
  and leaves it in place when it later removes quotes.

* Always surround `$@` by double-quotes.

    The rule of quoting references to variable that might contain filenames also
  applies to the special variable `$@` which expands to the positional
  parameters (i.e., the command-line arguments, unless you're in a
  function). `$@` is magical, in that `"$@"` expands each parameter as a
  separate word — i.e., it is equivalent to `"$1" "$2" ...` — which means that
  we remember which spaces were inside filenames and which spaces were used to
  separate arguments.

    Aside: `$*` *also* expands to all the positional parameters, but doesn't
  have the same magic quoting behaviour. `$*` exists solely to cause bugs in
  shell scripts and should never, ever, be used.

* [Array  variables](https://www.gnu.org/software/bash/manual/html_node/Arrays.html)
  can be useful if, for example, you need to build up a list of arguments for
  another command. Instead of writing this, which will mangle the filenames if
  they contain whitespace:

    ```sh
    # Don't do this
    cmdargs="-in $infile -out $outfile"
    othercmd $cmdargs
    ```
  ... try this:

    ```sh
    cmdargs=(-in "$infile" -out "$outfile")
    othercmd "${cmdargs[@]}"
    ```
