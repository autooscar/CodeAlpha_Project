
---

# ➤ b) insecure_sample.py (paste into `secure_review/insecure_sample.py`)

```python
# insecure_sample.py
import os
import json

def run_command(user_input):
    cmd = "ping -c 1 " + user_input
    os.system(cmd)

def load_and_eval(filename):
    with open(filename, "r") as f:
        data = f.read()
    return eval(data)

def main():
    name = input("Enter hostname or IP to ping: ")
    run_command(name)

    conf = load_and_eval("config.txt")
    print("Loaded config:", conf)

if __name__ == "__main__":
    main()
