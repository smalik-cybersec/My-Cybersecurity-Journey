Certainly! Below is a **complete and detailed lab session** covering the entire module **"Manage Files from the Command Line"** based on the RH124 material and best Linux system administration practices. This lab is structured to give you hands-on mastery of file management commands, shell features, and command-line efficiency.

# Lab: Manage Files from the Command Line

### Lab Objectives

- Navigate the Linux file system and list files/directories.
- Create, copy, move, rename, and delete files and directories.
- Use wildcards and shell expansions to specify files.
- Create and manage symbolic and hard links.
- Use `find` to locate files.
- Use Bash command-line editing and history shortcuts to improve efficiency.
- Understand file types and display file contents.


## Step 1: Prepare Your Environment

```bash
mkdir -p ~/cli_lab/{docs,images,scripts,archive}
cd ~/cli_lab
```

- Creates a lab directory structure for practice.


## Step 2: Create Sample Files

```bash
touch docs/readme.txt images/logo.png scripts/install.sh
echo "Welcome to the CLI lab" > docs/readme.txt
echo "echo Hello World" > scripts/install.sh
```

- Creates files and adds sample content.


## Step 3: List Files and Directories

```bash
ls -l
ls -l docs
ls -a docs
ls -lhR
```

- Use `-l` for detailed listing, `-a` to show hidden files, `-h` for human-readable sizes, and `-R` for recursive listing.


## Step 4: Copy, Move, and Rename Files

```bash
cp docs/readme.txt archive/
mv images/logo.png docs/
mv scripts/install.sh scripts/setup.sh
```

- Copy `readme.txt` to `archive`.
- Move `logo.png` into `docs`.
- Rename `install.sh` to `setup.sh`.


## Step 5: Remove Files and Directories

```bash
rm archive/readme.txt
rmdir images  # Will only succeed if empty
rm -r images  # Use this if images is not empty
```

- Remove file and directory safely.


## Step 6: Use Wildcards to Manage Multiple Files

```bash
touch docs/file{1..3}.txt
ls docs/*.txt
rm docs/file*.txt
ls docs
```

- Create multiple files with brace expansion.
- List and remove files using wildcards.


## Step 7: Find Files by Name

```bash
find . -name "*.sh"
find ~/cli_lab -type f -name "readme.txt"
```

- Locate files by pattern and type.


## Step 8: Create Links Between Files

### Hard Link

```bash
ln docs/readme.txt docs/readme_hard.txt
ls -li docs/readme.txt docs/readme_hard.txt
```

- Both files share the same inode.


### Symbolic Link

```bash
ln -s docs/readme.txt docs/readme_symlink.txt
ls -l docs/readme_symlink.txt
```

- Symlink points to the original by name.


## Step 9: View and Edit File Contents

```bash
cat docs/readme.txt
head -n 5 docs/readme.txt
tail -n 5 docs/readme.txt
less docs/readme.txt
```

- Use various commands to view file content.


## Step 10: Use Bash Command Line Shortcuts and History

- Press **Tab** for command and filename completion.
- Use **UpArrow** and **DownArrow** to navigate command history.
- Use **Ctrl + A** to jump to start of line.
- Use **Ctrl + E** to jump to end of line.
- Use `history` to view past commands.
- Re-execute commands with `!number` or `!string`.

Example:

```bash
history
!25   # Runs command number 25 from history
```


## Step 11: Practice Shell Expansions (Globbing)

```bash
ls *.txt
ls file?.txt
ls file[1-3].txt
ls [a-z]*.sh
```

- Use wildcards to match filenames.


## Step 12: Clean Up Your Lab Environment

```bash
cd ~
rm -rf ~/cli_lab
```

- Remove all lab files and directories.


# Summary of Key Commands

| Command | Purpose | Example |
| :-- | :-- | :-- |
| `ls` | List files/directories | `ls -lhR ~/cli_lab` |
| `cp` | Copy files/directories | `cp file1.txt file2.txt` |
| `mv` | Move or rename files/directories | `mv oldname.txt newname.txt` |
| `rm` | Remove files/directories | `rm -r mydir` |
| `mkdir` | Create directories | `mkdir -p parent/child` |
| `touch` | Create empty files or update timestamps | `touch newfile.txt` |
| `find` | Search files by name/type | `find . -name "*.sh"` |
| `ln` | Create hard link (`ln`) or symbolic link (`ln -s`) | `ln -s target linkname` |
| `cat`, `head`, `tail`, `less` | View file contents | `head -n 10 file.txt` |
| `history` | Show command history | `history` |
| Shell shortcuts | Command-line editing and completion | `Tab`, `Ctrl+A`, `Ctrl+E`, `!string` |

# Suggested Follow-up Lab Exercises

1. Create a nested directory structure with files, then use `find` and wildcards to manipulate them.
2. Create symbolic links to directories and practice navigating through them.
3. Use command-line shortcuts to efficiently repeat and edit commands.
4. Experiment with file permissions (`chmod`) and ownership (`chown`) for files you create.