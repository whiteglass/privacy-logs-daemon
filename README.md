# privacy-logs-daemon

privacy-logs-daemon is a Linux daemon that is responsible for monitoring log files for sensitive information and automatically redacts data using 3 configurable redaction methods.

---

## What does it do?

This daemon watches logs (or any file path that is set) in real time and detects sensitive data such as emails and passwords (patterns can be configured inside of 'detect.py'). If and when sensitive data is found, the daemon rewrites the data in the file and replaces the data with one of the three redaction methods that the user has chosen in 'config.json'. 

The original data is gone from the file. However, the user will be able to see some characters when using the mask configuration, be able to verify whether something matches the hashed data when using the hash configuration by applying the same hash function used in the daemon against an input, and the redact configuration provides no way of seeing what the original data was.

---

## How does it work?

The daemon tails each file specified in 'config.json' starting from the end of it, so they only process new written lines in the file(s). 

Flow of the daemon:

daemon reads log file --> daemon may detect sensitive data --> daemon rewrites the data in one of the three redaction modes

---

## What sensitive data is detected?

- Email addresses
- Passwords with these formats: (`password=`, `pwd=`, `passwd=`, `secret=`, `pass=`, `passphrase=`)

You can set patterns that get detected in 'detect.py'; you will have to add some lines of code.
I currently have not implemented an easier method to change patterns, but future releases will have this feature.

---

## What are the redaction modes?

There are three modes available which are configused inside of 'config.json'.

| Mode | Input | Output |
|------|-------|--------|
| `mask` | `test@gmail.com` | `tes**********` |
| `hash` | `test@gmail.com` | `[HASH:87924606b4131a8aceeeae8868531fbb9712aaa07a5d3a756b26ce0f5d6ca674]` |
| `redact` | `test@gmail.com` | `[REDACTED]` |

**mask** - replaces all characters except the first 3 with asterisks and the length of the original value is kept the same.

**hash** - replaces all characters with a SHA-256 hash. If you know the original value, you can hash the original value and compare to what hashed value appears in the file to compare if needed.

**redact** - replaces the whole value to '[REDACTED]'. No trace of the original value is left.

Default mode that is set in 'config.json' is the hash mode.

---

## Installation

```bash
git clone https://github.com/glass-skyy/privacy-logs-daemon.git
cd privacy-logs-daemon
```

---

## Configuration

Please edit 'config.json' before running to ensure that file path is correct and that the redaction mode you want is selected.

```json
{
    "mode": "redact",
    "log_files": [
        "/path/to/your/logfile.log",
        "/path/to/your/secondlogfile.log"
    ]
}
```
**mode** — choose `mask`, `hash`, or `redact`

**log_files** - this is the list of files that will be watched, you may set this to any file path you would like the daemon to watch and redact. You can have multiple log files or just one. To add a second/multiple log files, add the path in the same format as the code above.

## Usage

### Option 1 — Run manually in terminal

```bash
python3 main.py
```
The script will run in terminal. It will stop if the terminal is closed.

### Option 2 — Run as a systemd service

This runs the daemon permanently in the background, this will survive terminal closes and will start automatically on boot.

**1. Open `privacy-logs-daemon.service` and replace the path:**

```ini
ExecStart=/bin/bash /home/YOUR_USERNAME/privacy-logs-daemon/run.sh
```

Replace `YOUR_USERNAME` with your actual username. Run `pwd` inside the project folder if you are unsure of the path.

**2. Make the 'run.sh' script executable:**

```bash
chmod +x run.sh
```

**3. Install and enable the service:**

```bash
sudo cp privacy-logs-daemon.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start privacy-logs-daemon
sudo systemctl enable privacy-logs-daemon
```

**4. Check it is running:**

```bash
sudo systemctl status privacy-logs-daemon
```

**To stop the daemon:**

```bash
sudo systemctl stop privacy-logs-daemon
```

**To disable from starting on boot:**

```bash
sudo systemctl disable privacy-logs-daemon
```
## Examples and Screenshots

### Script running in terminal:

###  Mask

<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td valign="top">

<img width="429" alt="image" src="https://github.com/user-attachments/assets/8174315b-0710-483c-9784-7f71c7371750" />

<br><br>

<img width="460" alt="image" src="https://github.com/user-attachments/assets/3620f1fe-6d75-466d-a83b-395110b73eb5" />

</td>
<td valign="top">

<img width="416" alt="image" src="https://github.com/user-attachments/assets/ec7e63fb-6115-4bfb-8d35-87d549165a80" />

<br><br>

<img width="468" alt="image" src="https://github.com/user-attachments/assets/014a23ae-af47-4981-ab06-43c6966683b6" />

</td>
</tr>
</table>

---

###  Hash

<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td valign="top">

<img width="415" alt="image" src="https://github.com/user-attachments/assets/255b1b2f-5dcd-4ec3-a697-a3b06283ceb6" />

<br><br>

<img width="460" alt="image" src="https://github.com/user-attachments/assets/60ded4a6-9b55-4cc5-864a-7a38520d8b10" />

</td>
<td valign="top">

<img width="421" alt="image" src="https://github.com/user-attachments/assets/024328ca-9419-4104-9f3a-e413a68c154a" />

<br><br>

<img width="632" alt="image" src="https://github.com/user-attachments/assets/19f802fa-c210-4e69-ac14-17ec4db8c94a" />

</td>
</tr>
</table>



---

###  Redact

<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td valign="top">

<img width="421" alt="image" src="https://github.com/user-attachments/assets/583cd211-404f-45d9-9bfe-e6ac1e6424b4" />

<br><br>

<img width="460" alt="image" src="https://github.com/user-attachments/assets/77405021-d612-4683-80c2-58f5913ebf20" />

</td>
<td valign="top">

<img width="416" alt="image" src="https://github.com/user-attachments/assets/e477632c-fbc4-4ff6-b071-392b6f357f94" />

<br><br>

<img width="408" alt="image" src="https://github.com/user-attachments/assets/ef77c616-739a-48b3-b71d-f866853b9f6a" />

</td>
</tr>
</table>


---

## Planned features

- A discord bot/Slack notification when sensitive data is detected.
- Extended patterns to detect. e.g. API keys, phone numbers etc.
- An easier method to change and add detection patterns rather than needing to directly edit 'detect.py'.

---

## Caution

This daemon edits and writes to files directly and original data is unrecoverable once redacted. Only use this daemon on files you understand and know is safe to edit. Be careful about using this on system files unless you are sure that it is safe to do. 

I am not responsible for any data loss or system instability caused by misconfiguration of this daemon.  
