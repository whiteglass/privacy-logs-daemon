# runs the daemon
import time
import os
from detect import detection_sensitive
from config import load_config


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
                print(line.strip(), config)
            else:
                time.sleep(1)

def run():
    config = load_config()
    print(f"[daemon] starting with: {config['mode']}")
    for log_file in config["log_files"]:
        tailing_file(log_file, config)

if __name__ == "__main__":
    run()