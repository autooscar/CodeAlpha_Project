# fixed_sample.py
import subprocess
import json
import re

def safe_ping(host):
    if not re.fullmatch(r"[A-Za-z0-9\.\-]+", host):
        raise ValueError("Invalid host")
    subprocess.run(["ping", "-c", "1", host], check=False)

def load_config_json(filename):
    with open(filename, "r") as f:
        text = f.read()
    try:
        return json.loads(text)
    except:
        return {}

def main():
    try:
        host = input("Enter hostname or IP: ").strip()
        safe_ping(host)
    except Exception:
        print("Invalid input or error occurred.")

    conf = load_config_json("config.json")
    print("Config keys:", list(conf.keys()))

if __name__ == "__main__":
    main()
