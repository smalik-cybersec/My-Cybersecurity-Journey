Certainly! Here is a custom quiz based on the "Match File Names with Shell Expansions" section, particularly drawing from the quiz on page 83 of the *rh124-9.0-student-guide.pdf*, along with comprehensive explanations from across the provided sources.

---

### Custom Quiz: Matching File Names with Shell Expansions

**Instructions:** Choose the best pattern that matches the description of the file names.

**Questions:**

1.  Which pattern matches **only** file names that end with "b"?
    a. `b*`
    b. `*b`
    c. `*b*`
    d. `[!b]*`

2.  Which pattern matches **only** file names that begin with "b"?
    a. `b*`
    b. `*b`
    c. `*b*`
    d. `[!b]*`

3.  Which pattern matches **only** file names where the first character is **not** "b"?
    a. `b*`
    b. `*b`
    c. `*b*`
    d. `[!b]*`

4.  Which pattern matches **all** file names that contain a "b"?
    a. `b*`
    b. `*b`
    c. `*b*`
    d. `[!b]*`

5.  Which pattern matches **only** file names that contain a number?
    a. `*#*`
    b. `*[[:digit:]]*`
    c. `*[digit]*`
    d. ``

6.  Which pattern matches **only** file names that begin with an uppercase letter?
    a. `^?*`
    b. `^*`
    c. `[upper]*`
    d. `[[:upper:]]*`
    e. `[[CAP]]*`

7.  Which pattern matches **only** file names with at least three characters?
    a. `???*`
    b. `???`
    c. `\3*`
    d. `+++*`
    e. `...*`

---

### Solutions and Explanations

The process of matching simple patterns to file and directory names is known as **globbing**, or **pattern matching**. The Bash shell uses **metacharacters** (also called **wildcards**) to achieve this, expanding the pattern into a list of matching pathnames *before* the command is executed. This means the command itself receives the expanded list of filenames, not the wildcard pattern. Shell wildcards generally **do not match a leading period (`.`)** in filenames (which denote hidden files) unless explicitly specified. Filenames in Linux are **case-sensitive**.

Here are the detailed explanations for each question:

1.  **Which pattern matches only file names that end with "b"?**
    *   **Correct Answer: b. `*b`**
    *   **Explanation:** The **asterisk (`*`)** is a metacharacter that matches **any string of zero or more characters**. When `*` is placed *before* a pattern (e.g., `*b`), it matches any filename that ends with that pattern. So, `*b` will match files like `ab`, `bb`, `testb`, or even just `b`.
    *   **Why other options are incorrect:**
        *   `a. b*`: This matches files that *begin* with "b".
        *   `c. *b*`: This matches files that *contain* "b" anywhere in their name, not just at the end.
        *   `d. [!b]*`: This matches files where the *first* character is *not* "b".

2.  **Which pattern matches only file names that begin with "b"?**
    *   **Correct Answer: a. `b*`**
    *   **Explanation:** As explained above, the **asterisk (`*`)** matches any string of zero or more characters. When `*` is placed *after* a pattern (e.g., `b*`), it matches any filename that begins with that pattern. For example, `b*` would match `b`, `box`, `banana`, `boot_file.txt`.
    *   **Why other options are incorrect:**
        *   `b. *b`: This matches files that *end* with "b".
        *   `c. *b*`: This matches files that *contain* "b" anywhere in their name.
        *   `d. [!b]*`: This matches files where the *first* character is *not* "b".

3.  **Which pattern matches only file names where the first character is not "b"?**
    *   **Correct Answer: d. `[!b]*`**
    *   **Explanation:** **Square brackets (`[]`)** are metacharacters that match **any one character in the enclosed set or range**. When an **exclamation mark (`!`)** or **caret (`^`)** is used immediately after the opening bracket (e.g., `[!b]` or `[^b]`), it **inverts the match**, meaning it matches any character *not* in the enclosed set. The `*` then matches any string of characters following the non-'b' first character.
    *   **Why other options are incorrect:** These options describe patterns that either begin, end, or contain 'b', or simply do not correctly use the negation syntax.

4.  **Which pattern matches all file names that contain a "b"?**
    *   **Correct Answer: c. `*b*`**
    *   **Explanation:** By placing an **asterisk (`*`)** before and after the character "b", you are specifying that the pattern can be preceded by any string of zero or more characters, followed by "b", and then followed by any other string of zero or more characters. This effectively matches any filename that has "b" located *anywhere* within its name.
    *   **Why other options are incorrect:**
        *   `a. b*`: Matches files starting with "b".
        *   `b. *b`: Matches files ending with "b".
        *   `d. [!b]*`: Matches files where the first character is not "b".

5.  **Which pattern matches only file names that contain a number?**
    *   **Correct Answer: b. `*[[:digit:]]*`**
    *   **Explanation:** **POSIX character classes** provide shorthand notations for common character sets, and they must be used **inside square brackets (`[]`)**. `[:digit:]` represents any single numeral from 0 to 9. The asterisks surrounding `[[:digit:]]` (`*` before and `*` after) ensure that the pattern matches any filename that *contains* at least one digit, regardless of its position.
    *   **Why other options are incorrect:**
        *   `a. *#*`: The hash sign `#` is not a standard wildcard for digits; it is often used for comments in shell scripts and configuration files.
        *   `c. *[digit]*`: `[digit]` is not a valid POSIX character class format.
        *   `d.`: This matches exactly *one* character that is a digit, and only if it's the *entire* filename or at a specific position if combined with other patterns (e.g., `doc` matches `doc1`, `doc2`, etc.). It does not match a filename that *contains* a number unless it's explicitly positioned.

6.  **Which pattern matches only file names that begin with an uppercase letter?**
    *   **Correct Answer: d. `[[:upper:]]*`**
    *   **Explanation:** Similar to `[:digit:]`, `[:upper:]` is a **POSIX character class** that matches **any single uppercase letter**. Enclosing it in square brackets (`[[:upper:]]`) and following it with an asterisk (`*`) ensures that the pattern matches filenames that begin with an uppercase letter and are followed by any string of zero or more characters.
    *   **Why other options are incorrect:**
        *   `a. ^?*` and `b. ^*`: The caret (`^`) is an anchor that signifies the *start of a line* in **regular expressions** (used by commands like `grep` or within `[[ ]]` in Bash), not typically in simple globbing patterns for filename matching. Also, `?` is for any single character, not specifically uppercase letters.
        *   `c. [upper]*` and `e. [[CAP]]*`: These are not valid POSIX character class formats.

7.  **Which pattern matches only file names with at least three characters?**
    *   **Correct Answer: a. `???*`**
    *   **Explanation:** The **question mark (`?`)** wildcard matches **exactly one single character**. By using three question marks (`???`), you are matching files that have at least three characters. The trailing asterisk (`*`) means "followed by any string of zero or more characters," ensuring that filenames with *more* than three characters also match. For example, `doc?` matches `doc1` and `docA`, but not `document` because `document` has too many characters for just one `?`. However, `doc?*` would match `document`.
    *   **Why other options are incorrect:**
        *   `b. ???`: This would match files that have *exactly* three characters.
        *   `c. \3*`, `d. +++*`, `e. ...*`: These are not standard or correct shell globbing patterns for matching a minimum number of characters. The backslash `\` is used for escaping special characters, and `+` is a regular expression quantifier (one or more) not a globbing wildcard.

---

This quiz and its explanations cover the essential concepts of shell globbing (filename expansion) in Bash, as detailed in your provided sources. Remember, practice is key to mastering these concepts.