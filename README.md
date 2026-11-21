# AlgoLabs: Linux terminal labs

You do every lab inside a **GitHub Codespace** of this repository. You don't need to install anything on your computer: a browser is enough.

**[Open AlgoLabs in a Codespace](https://codespaces.new/xDarkPhoneix/AlgoLabs?quickstart=1)** All labs are graded on the class **lab server**. You log in to the server from the Codespace terminal with the private SSH key from your personal access ZIP.

Your access ZIP comes from your instructor's email, for example `Lab_4_student07_Access.zip`. One ZIP works for **every** lab. Keep it private: the file `access/ssh_key` inside it is your private key, and anyone who has it can log in as you.

## Labs

| Lab    | Topic                                          | Instructions                                                                 |
| ------ | ---------------------------------------------- | ---------------------------------------------------------------------------- |
| `lab4` | File permissions, SSH and remote file transfer | [labs/lab4/Experiment_Book_4_Draft.md](labs/lab4/Experiment_Book_4_Draft.md) |
| `lab5` | Bash automation and terminal workflows         | [labs/lab5/Lab_Book.md](labs/lab5/Lab_Book.md)                               |
| `lab7` | Introduction to Git: commits, reset and revert | [labs/lab7/Lab_Book.md](labs/lab7/Lab_Book.md)                               |
| `lab8` | Shell scripting and automation                 | [labs/lab8/Lab_Book.md](labs/lab8/Lab_Book.md)                               |
| `test1` | Lab Test 1: shell scripting examination       | [labs/test1/Lab_Book.md](labs/test1/Lab_Book.md)                             |
| `mocktest1` | Mock Test 1: Linux basics, permissions, `cut` | [labs/mocktest1/Lab_Book.md](labs/mocktest1/Lab_Book.md)               |
| `mocktest2` | Mock Test 2: `sort`/`uniq`, `tar`, `chmod`, a script | [labs/mocktest2/Lab_Book.md](labs/mocktest2/Lab_Book.md)        |

---

## Lab 5: step by step

In every step below, replace `studentNN` with your own account, for example `student07`. Your account is in your ZIP's name and in the email.

> **Your private key is a file:** `access/ssh_key`. You give SSH the file's **location** with `-i`. Do **not** open the key and paste its text into the terminal: that fails and exposes your key.

**1. Open your Codespace.** Click this link and choose **Create new codespace** (if you already have one, choose **Resume this codespace**):

**[Open AlgoLabs in a Codespace](https://codespaces.new/xDarkPhoneix/AlgoLabs?quickstart=1)**

You can also open it from this repository's GitHub page: **Code → Codespaces**. Wait until the editor and a terminal appear at the bottom. If there is no terminal, open one with **Terminal → New Terminal** (or <kbd>Ctrl</kbd>+<kbd>`</kbd>).

**2. Upload your access ZIP.** In the Explorer on the left, right-click the `.uploads` folder, choose **Upload…** and pick the ZIP from your email. You can also drag the ZIP onto the `.uploads` folder. Keep it zipped.

**3. Unzip it into your home folder.** Run this in the terminal:

```bash
unzip -o .uploads/Lab_4_studentNN_Access.zip -d ~
cd ~/Lab_4_studentNN_Access
ls access
```

`ls access` must list `ssh_key`. Your home folder (`~`) is outside the repository, so the key can never be committed to Git by mistake.

**4. Protect your key.** SSH refuses a key that other users can read:

```bash
chmod 600 access/ssh_key
```

**5. Connect to the lab server.** Your ZIP's `README.md` has this exact command with your account already filled in:

```bash
ssh -i access/ssh_key studentNN@98.70.53.61
```

The first time, SSH asks `Are you sure you want to continue connecting?`. Type `yes` only if the fingerprint shown matches the one in your ZIP's `README.md`. You are connected when the prompt shows `studentNN@students-lab:~$`.

**6. Do the lab on the server:**

```bash
cd ~/lab-work/lab5          # your Lab 5 folder: sample data and README.md are here
check_lab lab5              # see your score at any time
```

Follow [labs/lab5/Lab_Book.md](labs/lab5/Lab_Book.md). You can keep it open in the Codespace editor next to the terminal. The same instructions are also in `README.md` in your server folder. Each part ends with a **✅ Check** box that tells you which evidence files to save. Type `exit` to disconnect. Your files stay on the server.

> Once you are connected, the prompt shows `studentNN@students-lab`, and every command you type runs **on the lab server**, not in the Codespace. Check the prompt if you are unsure where you are.

---

## Lab 7: Introduction to Git

Lab 7 uses the same Codespace, access ZIP and server account as Lab 5. Connect as in [Lab 5: step by step](#lab-5-step-by-step) (or [Coming back later](#coming-back-later)), then, on the server:

```bash
cd ~/lab-work/lab7          # README.md has the instructions
check_lab lab7              # 0/100 before you start; check your score any time
```

Follow [labs/lab7/Lab_Book.md](labs/lab7/Lab_Book.md) (or `README.md` in your server folder, which has your roll number filled in). Set your Git e-mail to `RollNo@algolab.local` **before your first commit**, and run every `git` command on the server, not in the Codespace: only `~/lab-work/lab7` on the server is graded.

---

## Lab 8: Shell scripting and automation

Lab 8 uses the same Codespace, access ZIP and server account as Lab 5. Connect as in [Lab 5: step by step](#lab-5-step-by-step) (or [Coming back later](#coming-back-later)), then, on the server:

```bash
cd ~/lab-work/lab8          # README.md has the tasks
check_lab lab8              # 0/100 before you start; check your score any time
```

Follow [labs/lab8/Lab_Book.md](labs/lab8/Lab_Book.md) (or `README.md` in your server folder). Work in `~/lab-work/lab8`, do the tasks in order, and run every test case exactly as shown, saving its output in `outputs/`: the grader reads those files, it does not run your scripts.

---

## Mock Test 1 (mocktest1): Linux basics

Mock Test 1 is worth 30 marks. You connect from the **Terminal** app on your Mac (not a Codespace), with the same access ZIP and server account:

```bash
cd ~/Downloads
unzip -o Lab_4_studentNN_Access.zip
cd Lab_4_studentNN_Access
chmod 600 access/ssh_key
ssh -i access/ssh_key studentNN@98.70.53.61    # type yes if asked
```

Then, on the server:

```bash
cd ~/lab-work/mocktest1/RollNo_Exam    # already created for you
check_lab mocktest1                    # 2/30 before you start; check your score any time
```

The questions are in [labs/mocktest1/Lab_Book.md](labs/mocktest1/Lab_Book.md). Your folder `RollNo_Exam` (named after your roll number) and every answer file are already created, empty, on the server: write your answers into them and keep the exact file names. There is nothing to upload: your files on the server are graded.

---

## Mock Test 2 (mocktest2): text processing, tar, permissions, scripting

Mock Test 2 is worth 40 marks. Connect from the **Terminal** app on your Mac exactly as for [Mock Test 1](#mock-test-1-mocktest1-linux-basics), then, on the server:

```bash
cd ~/lab-work/mocktest2/RollNo_Exam    # already created for you
check_lab mocktest2                    # 0/40 before you start; check your score any time
```

The questions are in [labs/mocktest2/Lab_Book.md](labs/mocktest2/Lab_Book.md). Your folder `RollNo_Exam` and most answer files are already created, empty, on the server: write your answers into them, keep the exact file names and do the questions in order.

---

## Lab Test 1 (test1): shell scripting examination

Lab Test 1 is a 90-minute exam worth 70 marks. Connect from the **Terminal** app on your Mac exactly as for [Mock Test 1](#mock-test-1-mocktest1-linux-basics), then, on the server:

```bash
cd ~/lab-work/test1/RollNo_Exam        # already created for you
check_lab test1                        # 0/70 before you start; check your score any time
```

The questions are in [labs/test1/Lab_Book.md](labs/test1/Lab_Book.md). Your folder `RollNo_Exam` and every answer file are already created, empty, on the server: write your answers into them, keep the exact file names and do the questions in order. There is nothing to upload: your files on the server are graded.

---

## Check your score

```bash
check_lab lab5      # on the server: name the lab
check_lab lab7      # Lab 7: Git
check_lab lab8      # Lab 8: shell scripting
check_lab test1     # Lab Test 1
check_lab mocktest1 # Mock Test 1
check_lab mocktest2 # Mock Test 2
```

- Grading runs on the server, and the tests are hidden.
- You can check as often as you like. Every attempt is recorded for your instructor.
- Checking never changes your files.
- Read the **FAIL** lines: each one names the ✅ Check it belongs to.

---

## Coming back later

Your lab work is saved on the server, not in the Codespace.

- **Same Codespace:** open the [Codespace link](https://codespaces.new/xDarkPhoneix/AlgoLabs?quickstart=1) and choose **Resume this codespace**, then run:

  ```bash
  cd ~/Lab_4_studentNN_Access
  ssh -i access/ssh_key studentNN@98.70.53.61
  ```

- **New or rebuilt Codespace**, or `cd` says `No such file or directory`: repeat steps 2 to 5. Your work on the server is still there.

---

## If something goes wrong

| Problem                                                                                                                  | What to do                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| `unzip: cannot find or open .uploads/…`                                                                                  | Run `cd /workspaces/*` first. Check that the ZIP is in `.uploads` and that its name matches exactly (`ls .uploads`).               |
| `UNPROTECTED PRIVATE KEY FILE` or `bad permissions`                                                                      | Run `chmod 600 access/ssh_key` (step 4), then connect again.                                                                       |
| `Identity file access/ssh_key not accessible`                                                                            | You are not in the unzipped folder. Run `cd ~/Lab_4_studentNN_Access` and connect again.                                           |
| `Identity file b3BlbnNzaC1rZXkt… not accessible` (or `-----BEGIN…`), or bash says `command not found` for lines of letters | You pasted the key's **text**. Use the file path `access/ssh_key` instead, and tell your instructor so they can give you a new key. |
| `REMOTE HOST IDENTIFICATION HAS CHANGED`                                                                                 | Stop. Do not type `yes` or delete anything. Send the exact message to your instructor.                                             |
| Connection lost, frozen terminal, or the Codespace stopped                                                               | Open a new terminal and connect again (see [Coming back later](#coming-back-later)). Saved files are kept.                         |
| `Host key verification failed` or `Permission denied (publickey)`                                                        | Do not change any SSH settings. Send the exact error to your instructor (**never** send your key or ZIP).                          |
| A file already exists, or a check says "extra line"                                                                      | Look at the file first (`cat FILE`). Appending (`>>`) twice adds lines twice. Recreate the file, then try again.                   |

---

## Rules

- Use only **your own** ZIP, account and roll number.
- Never commit, share or post your ZIP or key. The `.uploads` folder is kept out of Git, and your unzipped key lives outside the repository.
- Work only on your own lab files. Do not use `sudo`.
