## Explanation

The **shell environment** is a collection of settings and variables that control how your shell (like Bash or Zsh) operates. You can change your environment temporarily (for the current session) or permanently (by editing configuration files like `~/.bashrc` or `~/.bash_profile`).

**Common reasons to change the shell environment:**

- Add or change environment variables (like `PATH`, `EDITOR`)
- Define shell aliases (shortcuts for commands)
- Set shell prompts (customize how your prompt looks)
- Configure startup commands (run scripts or set variables automatically)


## Real Linux Commands with Examples

### 1. View Current Environment Variables

```bash
printenv
```

- Lists all current environment variables.

```bash
echo $PATH
```

- Shows the current `PATH` variable (where the shell looks for executables).


### 2. Set an Environment Variable (Temporary)

```bash
export MYVAR="HelloWorld"
echo $MYVAR
```

- `export` creates a variable for the current session.
- It disappears when you close the terminal.


### 3. Make Environment Changes Permanent

**Edit your `~/.bashrc` file:**

```bash
nano ~/.bashrc
```

- Add a line at the end, for example:

```bash
export EDITOR=vim
export PATH=$PATH:$HOME/scripts
alias ll='ls -la'
PS1='\u@\h:\w\$ '
```

- Save and exit (`Ctrl+O`, `Ctrl+X`).

**Apply changes immediately:**

```bash
source ~/.bashrc
```

- This reloads your configuration without logging out and back in.


### 4. Add an Alias

**Example:**

```bash
echo "alias gs='git status'" >> ~/.bashrc
source ~/.bashrc
gs
```

- Now, typing `gs` runs `git status`.


### 5. Change Your Prompt

**Example:**

```bash
echo "PS1='\[\e[32m\]\u@\h:\w\$ \[\e[0m\]'" >> ~/.bashrc
source ~/.bashrc
```

- This sets your prompt to green and shows `user@host:cwd$`.


### 6. Practice: Customizing and Testing

1. **Set a temporary variable and check it:**

```bash
export TESTVAR="CyberShell"
echo $TESTVAR
```

2. **Add a permanent alias:**

```bash
echo "alias ltr='ls -ltrh'" >> ~/.bashrc
source ~/.bashrc
ltr
```

3. **Change your PATH to include a custom scripts directory:**

```bash
mkdir -p ~/scripts
echo "export PATH=\$PATH:\$HOME/scripts" >> ~/.bashrc
source ~/.bashrc
echo $PATH
```


## Output Examples

- After setting `MYVAR`:

```
HelloWorld
```

- After adding and using alias:

```
(output of ls -ltrh)
```

- After changing prompt:

```
user@hostname:/current/directory$
```


## Key Takeaways

- Temporary changes (with `export`) last only for the session.
- Permanent changes require editing `~/.bashrc` or `~/.bash_profile`.
- Use `source ~/.bashrc` to apply changes instantly.
- Aliases and environment variables can greatly speed up and personalize your workflow.
- Always be careful editing your shell config files—syntax errors can affect your login shell.


## Try It Yourself

1. Add an alias to your `~/.bashrc` for a command you use often.
2. Change your prompt to include the current time by adding `\t` to `PS1`.
3. Set a variable called `LABUSER` with your username in `~/.bashrc`, and echo it after sourcing.