import os
import hashlib
import argparse
import json
from datetime import datetime
from colorama import Fore, Style, init
init(autoreset=True)  # Automatically reset colors after each print


def hash_file(filepath):
    h = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk:=f.read(8192):
                h.update(chunk)
        return h.hexdigest()
    except Exception as e:
        return f"Error: {str(e)}"

def get_file_hashes(tar_dir):
    file_hashes = {}
    for root, dirs, files in os.walk(tar_dir):
        for file in files:
            abs_path = os.path.join(root, file)
            file_hashes[abs_path] = hash_file(abs_path)
    return file_hashes

def save_hashes(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_hashes(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, 'r') as f:
        return json.load(f)
    
def compare_hashes(old, new):
    added, deleted, modified = [], [], []
    for path in old:
        if path not in new:
            deleted.append(path)
        elif old[path] != new[path]:
            modified.append(path)
    for path in new:
        if path not in old:
            added.append(path)
    return added, deleted, modified

def log_report(added, deleted, modified):
    now = datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
    print(f"{Style.BRIGHT}\n[File Change Report - {now}]{Style.RESET_ALL}")
    if not (added or deleted or modified):
        print(f"{Fore.MAGENTA}[✓] No Changes Detected!{Style.RESET_ALL}")
        return
    if added:
        print(f"{Fore.CYAN}\n[+] Added Files:{Style.RESET_ALL}")
        for files in added:
            print(f"{Fore.CYAN} {files}{Style.RESET_ALL}")
    if deleted:
        print(f"{Fore.RED}\n[-] Deleted Files:{Style.RESET_ALL}")
        for files in deleted:
            print(f"{Fore.RED} {files}{Style.RESET_ALL}")
    if modified:
        print(f"{Fore.YELLOW}\n[*] Modified Files:{Style.RESET_ALL}")
        for files in modified:
            print(f"{Fore.YELLOW} {files}{Style.RESET_ALL}")
    
def main():
    parser = argparse.ArgumentParser(description="File Integrity Checker using SHA 256.")
    parser.add_argument("-d", "--directory", required=True, help="Target directory to monitor")
    parser.add_argument("-s", "--snapshot", default="snapshot.json", help="Snapshot file to save hashes")
    args = parser.parse_args()

    tar_dir = os.path.abspath(args.directory)
    snapshot_file = os.path.abspath(args.snapshot)

    print(f"{Fore.GREEN}\n📂 Scanning: {tar_dir}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}\n📄 Snapshot: {snapshot_file}{Style.RESET_ALL}")

    if not os.path.exists(snapshot_file):
        hash = get_file_hashes(tar_dir)
        save_hash = save_hashes(hash, snapshot_file)
        print(f"{Fore.GREEN}\nInitial snapshot created and saved to {snapshot_file}{Style.RESET_ALL}")
        return
    old_snapshot = load_hashes(snapshot_file)
    new_snapshot = get_file_hashes(tar_dir)

    added, deleted, modified = compare_hashes(old_snapshot, new_snapshot)

    log_report(added, deleted, modified)

    save_hashes(new_snapshot, snapshot_file)

if __name__ == "__main__":
    main()
