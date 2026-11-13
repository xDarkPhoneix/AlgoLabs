# Lab 8: Shell Scripting & Automation

**Environment:** the class lab server, reached from the **Terminal** app on your Mac. Your account is `studentNN`: replace `studentNN` with your own account (in your ZIP's name), e.g. `student07`.

---

## Setup: connect to the lab server from your Mac

Your access ZIP (for example `Lab_4_studentNN_Access.zip`) is the one from your instructor's email; the same ZIP works for every lab.

1. Download the ZIP from the email. It lands in your **Downloads** folder. Leave it there.
2. Open **Terminal**: press `⌘ Space`, type `Terminal` and press Return.
3. Go to your Downloads folder and unzip the ZIP:

   ```bash
   cd ~/Downloads
   unzip -o Lab_4_studentNN_Access.zip
   ```

   Safari often unzips downloads by itself. If `ls` already shows a folder named `Lab_4_studentNN_Access`, you can skip the `unzip` line.

4. Go into the unzipped folder, protect the key and connect:

   ```bash
   cd ~/Downloads/Lab_4_studentNN_Access
   ls access                                     # you must see ssh_key
   chmod 600 access/ssh_key                      # SSH refuses a key others can read
   ssh -i access/ssh_key studentNN@98.70.53.61
   ```

   The first time, SSH asks `Are you sure you want to continue connecting (yes/no/[fingerprint])?`. Type `yes` and press Return.

   `-i` takes the **path** of the key file. Never open the key and paste its text into the terminal.

5. You are connected when the prompt shows `studentNN@students-lab`. Everything in this lab is typed **on the server**, not on your Mac. Go to your lab folder and check that grading works:

   ```bash
   cd ~/lab-work/lab8
   check_lab lab8                                # 0/100 before you start; run it any time
   ```

If the connection drops, open Terminal and run steps 4 and 5 again. Your files stay on the server. Do not share your key or ZIP with anyone.

**Common problems**

| Message                                       | Fix                                                                                                                   |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `No such file or directory` after `cd`        | The folder or ZIP name is different. Run `ls ~/Downloads` and use the exact name you see.                             |
| `WARNING: UNPROTECTED PRIVATE KEY FILE!`      | Run `chmod 600 access/ssh_key` again, then connect.                                                                   |
| `Permission denied (publickey)`               | Check that you are in the `Lab_4_studentNN_Access` folder and that `studentNN` matches the number in your ZIP's name. |
| `Identity file access/ssh_key not accessible` | You are in the wrong folder. Run step 4 from the `cd` line.                                                           |

---

## Overview

This lab contains **5 shell-scripting tasks** arranged in progressive difficulty.

You will practise:

- Script arguments and file validation
- Counting lines using `wc`
- Comparing files using `diff`
- Searching logs using `grep`
- Arrays and `for` loops
- Exit statuses and output redirection

Complete the tasks in order. Later tasks reuse scripts and files created earlier.

## Lab Contents

| Task | Topic                                   |
| ---- | --------------------------------------- |
| Q1   | File Validation and Line Counter        |
| Q2   | File Comparison using `diff`            |
| Q3   | Log Searching using `grep`              |
| Q4   | Folder Checklist using Arrays and Loops |
| Q5   | Event Summary Report                    |

---

## General Instructions

1. Your main lab directory is **`~/lab-work/lab8`** on the server. Work only there; it is what gets graded.
2. Create the following three folders inside it:
   - `commands/` — input and test data files.
   - `scripts/` — shell scripts.
   - `outputs/` — generated output, error logs and saved test results.
3. Use the exact file and folder names specified in each task.
4. Every script must:
   - Start with `#!/usr/bin/env bash` (the very first line).
   - Be executable using `chmod +x`.
   - Send normal output to **stdout** and error messages to **stderr** (`echo "..." >&2`).
5. Always quote variables containing file or directory paths (`"$1"`, `"$file"`).
6. Run every command from the main lab directory `~/lab-work/lab8`, unless specified otherwise. All paths below are relative to it.
7. Create the data files with the commands given in each **Setup** (copy them exactly). Write scripts with `nano` or a here-document (`cat > scripts/x.sh << 'EOF' ... EOF`).
8. `sudo` is not needed for any task.

## How your work is graded: save every test run

The grader **does not run your scripts**. It reads the files in `outputs/`. So each test case must be run with its results saved, using this pattern:

```bash
./scripts/NAME.sh ARGS > outputs/qN_testM.out 2> outputs/qN_testM.err; echo $? > outputs/qN_testM.status
```

| File                      | Holds                                       |
| ------------------------- | ------------------------------------------- |
| `outputs/qN_testM.out`    | everything the script printed on **stdout** |
| `outputs/qN_testM.err`    | everything the script printed on **stderr** |
| `outputs/qN_testM.status` | the script's **exit status** (`$?`)         |

The exact command for every test is given under **Test Cases** in each task. If you fix a script later, **run its tests again** so the saved files are up to date (they are overwritten, not appended). Run `check_lab lab8` any time to see your score; each `FAIL` line names the task it belongs to.

## Initial Setup

Create the lab workspace:

```bash
cd ~/lab-work/lab8
mkdir -p commands scripts outputs
```

Your directory structure should look like this:

```text
~/lab-work/lab8/
├── README.md
├── commands/
├── scripts/
└── outputs/
```

## Useful Commands

`mkdir`, `cd`, `ls`, `cat`, `printf`, `echo`, `nano`, `chmod`, `wc`, `diff`, `grep`, `rm`, `export`, `command`

Reminders:

- `$#` is the number of arguments, `$1` the first one. `[ -z "$1" ]` is true when it is empty.
- `[ -f "$file" ]` tests for a regular file, `[ -d "$dir" ]` for a folder.
- `wc -l < "$file"` prints only the number; `wc -l "$file"` also prints the name.
- `diff` and `grep` set an exit status you can test with `if`: `diff` gives `0` when the files are identical, `grep` gives `0` when something matched.

---

# Lab Tasks

## Q1. File Validation and Line Counter

### Objective

Create a script that accepts one filename, checks whether it exists, and counts its lines.

### Setup

Create a sample file:

```bash
printf "apple\nbanana\ncherry\norange\n" > commands/fruits.txt
```

### Task

Create `scripts/check_file.sh`.

**Usage:**

```bash
./scripts/check_file.sh <filename>
```

The script must:

1. Check whether a filename is provided.
2. If no filename is provided, display `Error: No file provided` to stderr and exit with status `1`.
3. Check whether the specified file exists.
4. If the file does not exist, display `Error: File not found` to stderr and exit with status `1`.
5. If the file exists, display its filename (exactly as given in the argument) and total number of lines, and exit with status `0`.

Use `wc -l` to count the lines.

### Expected Output

```text
File: commands/fruits.txt
Lines: 4
```

### Test Cases

```bash
chmod +x scripts/check_file.sh

# Test 1: Valid file
./scripts/check_file.sh commands/fruits.txt > outputs/q1_test1.out 2> outputs/q1_test1.err; echo $? > outputs/q1_test1.status

# Test 2: File does not exist
./scripts/check_file.sh commands/missing.txt > outputs/q1_test2.out 2> outputs/q1_test2.err; echo $? > outputs/q1_test2.status

# Test 3: No argument
./scripts/check_file.sh > outputs/q1_test3.out 2> outputs/q1_test3.err; echo $? > outputs/q1_test3.status
```

Check your results with `cat outputs/q1_test1.out` and so on. Test 1's `.err` file must be empty; Tests 2 and 3 must have an empty `.out` file.

---

## Q2. Comparing Files using `diff`

### Objective

Create a script that accepts one filename and compares it with a predefined reference file.

### Setup

Create the following files:

```bash
printf "PORT=8080\nTIMEOUT=30\n" > commands/reference.txt

printf "PORT=8080\nTIMEOUT=30\n" > commands/config.txt

printf "PORT=9090\nTIMEOUT=60\n" > commands/config_wrong.txt
```

### Task

Create `scripts/compare_config.sh`.

**Usage:**

```bash
./scripts/compare_config.sh <filename>
```

The script must:

1. Check whether a filename is provided. If not, display `Error: No file provided` to stderr and exit with status `1`.
2. Check whether the specified file exists. If not, display `Error: File not found` to stderr and exit with status `1`.
3. Compare `commands/reference.txt` (first) with the given file (second) using `diff`:

```bash
diff commands/reference.txt "$file"
```

4. If both files are identical, display:

```text
Configuration is correct
```

5. If the files are different:
   - Display `Configuration is different`.
   - Save the differences (the output of `diff`) in `outputs/diff_output.txt`.
   - Exit with status `2`.

Use exit status `0` for identical files and `1` for invalid input or missing files.

### Test Cases

```bash
chmod +x scripts/compare_config.sh

# Test 1: Identical configuration
./scripts/compare_config.sh commands/config.txt > outputs/q2_test1.out 2> outputs/q2_test1.err; echo $? > outputs/q2_test1.status

# Test 2: Different configuration
./scripts/compare_config.sh commands/config_wrong.txt > outputs/q2_test2.out 2> outputs/q2_test2.err; echo $? > outputs/q2_test2.status

# Test 3: Missing file
./scripts/compare_config.sh commands/missing.txt > outputs/q2_test3.out 2> outputs/q2_test3.err; echo $? > outputs/q2_test3.status

# Test 4: No argument
./scripts/compare_config.sh > outputs/q2_test4.out 2> outputs/q2_test4.err; echo $? > outputs/q2_test4.status
```

After Test 2, `outputs/diff_output.txt` must hold the differences between the two files. Tests 3 and 4 must not change it.

---

## Q3. Searching Logs using `grep`

### Objective

Create a script that accepts one keyword and searches for it in a predefined log file.

### Setup

Create the sample log:

```bash
cat > commands/server.log << 'EOF'
INFO System initialized
ERROR Database connection timed out
INFO User logged in
WARNING Disk space low
ERROR Failed to write to storage
INFO Backup completed successfully
EOF
```

### Task

Create `scripts/search_log.sh`.

**Usage:**

```bash
./scripts/search_log.sh <keyword>
```

The script must:

1. Check whether a keyword is provided. If not, display `Error: No keyword provided` to stderr and exit with status `1`.
2. Search for the keyword in `commands/server.log` using `grep`.
3. Save all matching lines in `outputs/matches.txt` (overwrite it on every run).
4. Count the number of matching lines.
5. If matches are found, display the number of matching lines in the form `Found N matching lines` and exit with status `0`.
6. If no matches are found, display an appropriate error message to stderr (for example `Error: No matches found for FATAL`) and exit with status `2`.

### Expected Output

For the keyword `ERROR`:

```text
Found 2 matching lines
```

### Expected Content of `outputs/matches.txt`

```text
ERROR Database connection timed out
ERROR Failed to write to storage
```

### Test Cases

Each run overwrites `outputs/matches.txt`, so after Tests 1 and 2 keep a copy of it as shown:

```bash
chmod +x scripts/search_log.sh

# Test 1: Search for ERROR
./scripts/search_log.sh ERROR > outputs/q3_test1.out 2> outputs/q3_test1.err; echo $? > outputs/q3_test1.status
cp outputs/matches.txt outputs/q3_test1_matches.txt

# Test 2: Search for INFO
./scripts/search_log.sh INFO > outputs/q3_test2.out 2> outputs/q3_test2.err; echo $? > outputs/q3_test2.status
cp outputs/matches.txt outputs/q3_test2_matches.txt

# Test 3: Search for a keyword that does not exist
./scripts/search_log.sh FATAL > outputs/q3_test3.out 2> outputs/q3_test3.err; echo $? > outputs/q3_test3.status

# Test 4: No argument
./scripts/search_log.sh > outputs/q3_test4.out 2> outputs/q3_test4.err; echo $? > outputs/q3_test4.status
```

---

## Q4. Folder Checklist using Arrays and Loops

### Objective

Create a script that checks whether an event folder contains three required files.

### Setup

Create the event folders:

```bash
mkdir -p commands/events/tech-conference
mkdir -p commands/events/sports-meet
```

Create the sample files:

```bash
# tech-conference contains all three required files
printf "Event notes\nVenue details\n" > commands/events/tech-conference/notes.txt

printf "Food: 400\nDecor: 200\n" > commands/events/tech-conference/budget.txt

printf "Student1\nStudent2\nStudent3\n" > commands/events/tech-conference/registrations.txt

# sports-meet is missing registrations.txt
printf "Sports event\n" > commands/events/sports-meet/notes.txt

printf "Trophies: 300\n" > commands/events/sports-meet/budget.txt
```

Do **not** create `commands/events/cultural-fest`: it must stay missing.

### Task

Create `scripts/check_event.sh`.

**Usage:**

```bash
./scripts/check_event.sh <event_folder>
```

The script must:

1. Check whether the event folder exists. If no folder is given or it does not exist, display `Error: Event folder not found` to stderr and exit with status `1`.
2. Create an array containing the following filenames:

```bash
required_files=("notes.txt" "budget.txt" "registrations.txt")
```

3. Use a `for` loop to check whether all three files exist inside the given folder.
4. If any file is missing, display `Missing file: <filename>` (for the first missing file) to stderr and exit with status `1`. Nothing is printed to stdout in this case.
5. If all files exist, display the event folder name and the line count of each file (format below), and exit with status `0`.

### Expected Output

For `commands/events/tech-conference` (stdout):

```text
Event: commands/events/tech-conference

notes.txt: 2
budget.txt: 2
registrations.txt: 3
```

For `commands/events/sports-meet` (stderr):

```text
Missing file: registrations.txt
```

For `commands/events/cultural-fest` (stderr):

```text
Error: Event folder not found
```

### Test Cases

```bash
chmod +x scripts/check_event.sh

# Test 1: Complete event folder
./scripts/check_event.sh commands/events/tech-conference > outputs/q4_test1.out 2> outputs/q4_test1.err; echo $? > outputs/q4_test1.status

# Test 2: Incomplete event folder
./scripts/check_event.sh commands/events/sports-meet > outputs/q4_test2.out 2> outputs/q4_test2.err; echo $? > outputs/q4_test2.status

# Test 3: Non-existent folder
./scripts/check_event.sh commands/events/cultural-fest > outputs/q4_test3.out 2> outputs/q4_test3.err; echo $? > outputs/q4_test3.status
```

---

## Q5. Event Summary Report

### Objective

Create a master script that checks multiple event folders using the previously created `check_event.sh` script and generates a summary report.

### Task

Create `scripts/event_summary.sh`.

Run the script from the main lab directory:

```bash
./scripts/event_summary.sh
```

The script must:

1. Add the `scripts/` directory to the `PATH` environment variable:

```bash
export PATH="$PWD/scripts:$PATH"
```

2. Verify that `check_event.sh` is available using:

```bash
command -v check_event.sh > /dev/null
```

If it is not found, display `Error: check_event.sh not found` to stderr and exit with status `1`.

3. Store the following event folder names in an array:

```bash
events=("tech-conference" "sports-meet" "cultural-fest")
```

4. Use a `for` loop to check each event folder by calling `check_event.sh` **by name** (not `./scripts/check_event.sh`):

```bash
check_event.sh "commands/events/$event"
```

5. If the event check succeeds (exit status `0`), mark it as `COMPLETE`.

6. If the event check fails, mark it as `INCOMPLETE`.

7. Discard the normal output of `check_event.sh` using `> /dev/null`.

8. Append error messages from `check_event.sh` to `outputs/errors.log` (use `2>>`).

9. Generate the summary report in `outputs/event_summary.txt` using a grouped command block and a single output redirection.

**Important:** Generate the complete report using one grouped command block:

```bash
{
    # Report generation commands
} > outputs/event_summary.txt
```

10. Display the following message on stdout:

```text
Summary report created
```

Exit with status `0`.

### Expected Report

`outputs/event_summary.txt`:

```text
EVENT SUMMARY REPORT

====================

tech-conference: COMPLETE
sports-meet: INCOMPLETE
cultural-fest: INCOMPLETE
```

### Expected Error Log

`outputs/errors.log`:

```text
Missing file: registrations.txt
Error: Event folder not found
```

### Expected Terminal Output

```text
Summary report created
```

### Test Case

Remove any previous error log and run the script, saving its results:

```bash
chmod +x scripts/event_summary.sh

rm -f outputs/errors.log

# Test 1: Generate the report
./scripts/event_summary.sh > outputs/q5_test1.out 2> outputs/q5_test1.err; echo $? > outputs/q5_test1.status
```

Then check `cat outputs/event_summary.txt outputs/errors.log outputs/q5_test1.out`. If you run the script again, run `rm -f outputs/errors.log` first, so the log holds only one run.

---

When you are done, run `check_lab lab8` one last time. There is nothing to upload: your files on the server are graded.

---

**End of Lab 8**
