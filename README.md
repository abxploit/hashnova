COMPANY: CODTECH IT SOLUTIONS

NAME: Abinesh M

INTERN ID: CT04DH572

DOMAIN: Cybersecurity & Ethical Hacking

DURATION: 4 Weeks

MENTOR: NEELA SANTOSH

---

# 🔐 HashNova - File Integrity Checker

**HashNova** is a simple and powerful Python-based tool that monitors file changes (added, deleted, modified) using SHA-256 hashing.

---

## 🚀 Features

- 🔎 Detects **added**, **deleted** and **modified** files
- 📄 Stores snapshot in **JSON** format
- 🎨 Colored terminal output using `colorama`
- ✅ Easy to use and lightweight

---

## 🛠️ Installation

Make sure Python 3 is installed.

Install required library:

```bash
pip install colorama
```

---

## 🔁 Clone This Repository

You can clone this repository using Git:

```bash
git clone https://github.com/abxploit/hashnova
cd hashnova
```

## 📂 Usage
```bash
python hashnova.py -d <target_directory> -s <snapshot_file>
```

---

## 🔹 Example
```bash
python hashnova.py -d "C:\Users\Abinesh\Documents" -s snapshot.json
```
First run creates a snapshot file

Later runs detect file changes and update the snapshot

---

## 📦 Output Example

[File Change Report - 06-07-2025  10:30:25]

[+] Added Files:
  C:\Users\abxploit\Documents\newfile.txt

[-] Deleted Files:
  C:\Users\abxploit\Documents\oldfile.txt

[*] Modified Files:
  C:\Users\abxploit\Documents\updated_file.py
  
 ---

## 📁 Snapshot File
The snapshot file stores the SHA-256 hash of every file in the target directory in JSON format. It's used for comparing file changes over time.

---

## 🧠 Author
Abinesh M

GitHub: @abxploit

## OUTPUT

<img width="871" height="181" alt="Image" src="https://github.com/user-attachments/assets/364e8453-8899-4724-a170-4a9e85e4a6be" />
<img width="897" height="356" alt="Image" src="https://github.com/user-attachments/assets/2716cfdc-3d83-4e5f-99ea-c99a687c040c" />

---
## ✅ Conclusion:
HashNova is a testament to simplicity, power, and practicality. It fills the gap between bloated GUI hashing tools and basic command-line utilities by offering a modern, well-structured, and extensible solution. Whether you are building a secure pipeline, conducting a forensic investigation, or simply verifying downloaded files, HashNova serves as a reliable companion in your cybersecurity toolkit
