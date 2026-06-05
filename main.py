# runs the daemon
import time
import os
from detect import detection_sensitive
from config import load_config
from redact import apply_redact

def tailing_file(path, config):
    if not os.path.exists(path):
        print(f"[ERROR]: {path} not found...")
        return 

    print(f"[daemon] is watching: {path}")
    with open(path, "r") as file:
        file.seek(0, 2)
        
        while True:
            line = file.readline()
            if line:
                process_line(line.strip(), config)
            else:
                time.sleep(1)

def process_line(line, config):
    matches = detection_sensitive(line)
    if not matches:
        return

    redacted_data = line
    for label, value in matches:
        cleanse = apply_redact(value, config["mode"])
        redacted_data = redacted_data.replace(value, cleanse)

    print(f"[DETECTED]: found {[label for label, value in matches]}")


def run():
    config = load_config()
    print(f"[daemon] starting with: {config['mode']}")
    for log_file in config["log_files"]:
        tailing_file(log_file, config)

if __name__ == "__main__":
    run()