The "Custom Guided Exercise: Read Manual Pages" you are asking about is a practical activity found on **page 104** of the `rh124-9.0-student-guide.pdf`. This exercise, along with the "Lab: Get Help in Red Hat Enterprise Linux" on **page 108** of the same guide, is designed to enhance your proficiency in utilising Red Hat Enterprise Linux (RHEL)'s local help systems, particularly its system manual pages.

### Lab: Get Help in Red Hat Enterprise Linux

This lab is part of **Chapter 4: Get Help in Red Hat Enterprise Linux**.

**Outcomes / Objectives of the Lab:**
Upon successfully completing this guided exercise, you are expected to be able to:
*   **Locate relevant information for commands by searching manual pages**.
*   **Learn new options for the most common documentation commands**.
*   **Use appropriate tools to view and print documentation and other non-text formatted files**.

**Prerequisites and Setup:**
To begin this exercise, you must be logged in as the **`student` user on the `workstation` machine**. The necessary lab environment is prepared by executing the command **`lab start help-review`**.

**Instructions (Implied Tasks):**
While the provided source does not list explicit step-by-step instructions for the "Lab: Get Help in Red Hat Enterprise Linux" within the excerpt, the preceding "Guided Exercise: Read Manual Pages" (on page 104) and the general context of "Get Help in Red Hat Enterprise Linux" chapter outline the types of tasks expected. These tasks typically involve using the `man` command to view manual pages, exploring options within them, and searching for information using keywords.

Specifically, the "Read Manual Pages" section discusses:
*   Using the `man` command to view system manual pages.
*   The location of these pages in subdirectories of `/usr/share/man`.
*   The `man` program itself being used to see these pages from the command line.

Other relevant commands and tools for getting help on RHEL systems, as covered in the broader "Getting Help" context, include:
*   The **`apropos` command** (or `man -k` option) to search for keywords in man page names and short descriptions.
*   The **`whatis` command** to expose a short, one-line description for a specified command or file from the man page database.
*   The **`info` and `pinfo` commands** which offer more detailed documentation than typical man pages.
*   Documentation located in the **`/usr/share/doc` directory**.
*   The **`--help` option** for commands, which displays a usage message or screen.

**Completion:**
After completing the practical tasks, you are instructed to run **`lab grade help-review`** to check your progress and **`lab finish help-review`** to conclude the exercise, ensuring resources from previous exercises do not impact upcoming ones.

### Understanding Manual Pages (Man Pages)

Manual pages are a **fundamental and commonly used source of documentation in RHEL**. They are critical for RHEL administration skills and are considered the **main information resource in the system**.

**Structure and Sections:**
Man pages organise information under various standard headings, such as `NAME`, `SYNOPSIS`, `DESCRIPTION`, `OPTIONS`, `EXAMPLES`, `FILES`, and `SEE ALSO` (though not all headings appear on every page). They are structured as quick references rather than in-depth tutorials [General knowledge, not explicitly stated in sources, but common understanding].

Man pages are organised into **nine numbered sections** based on the type of information they contain:
*   **Section 1:** User commands and shell programs (e.g., `passwd(1)`).
*   **Section 5:** File formats for various system configuration files (e.g., `passwd(5)` for `/etc/passwd`).
*   **Section 8:** System administration and privileged commands.
If a topic exists in multiple sections (e.g., `passwd` as both a command and a file format), the `man` command typically displays the lowest-numbered section by default. To view a specific section, you must include the section number, for example, **`man 5 passwd`**.

**Navigation within Man Pages:**
When a man page is displayed (usually using a pager like `less`), you can navigate its content. For example, you can search for text strings using `/string` (forward) or `?string` (backward) and jump to the next or previous occurrence using `n` or `N`, respectively. Pressing `q` will quit the man page [from common Linux knowledge; specific navigation keystrokes are not detailed in the provided excerpts but are implied by the instruction to "browse various headings"].

### Importance for RHCSA Certification

Local documentation, including man pages, is a **critical resource for the Red Hat Certified System Administrator (RHCSA) exam**. During the RHCSA exam, candidates typically **do not have access to the Internet**, but they do have access to the local system's documentation, including man and info pages, and files in `/usr/share/doc` directories. This necessitates strong familiarity with these local help systems to successfully complete tasks in the hands-on exam environment.