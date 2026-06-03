#this is used to load config.json

import json
import os

config_path = os.path.join(os.path.dirname(__file__), "config.json")

def load_config ():
    with open(config_path, "r") as file:
        config = json.load(file)
    
    redaction_modes = ["mask", "hash", "redact"]
    if config["mode"] not in redaction_modes:
        print(f"[ERROR]: invalid mode '{config['mode']}' returning to default mask mode")
        config["mode"] = "mask"
        
    return config