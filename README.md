<div align="center">

# 👻✨ GhostPanel ✨👻

<p>
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" />
  <img src="https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows" />
  <img src="https://img.shields.io/badge/Discord%20Bot-Online-brightgreen?logo=discord" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen" />
</p>

---

## 🚨 **WARNING** 🚨

> **This project is for educational and authorized testing purposes only. Unauthorized use of keyloggers or remote administration tools is illegal and unethical.**

---

## 🧭 Overview

**GhostPanel** is a multi-functional Discord bot for Windows, designed for remote administration and control. It provides a range of features accessible via Discord commands and interactive UI buttons, including privilege escalation, keylogging, screen and webcam capture, mouse manipulation, and more.

---

## 🗂️ Feature Table

| Feature                | Description                                                                 | Libraries/APIs                |
|------------------------|-----------------------------------------------------------------------------|-------------------------------|
| 🛡️ Privilege Escalation | Run as admin using Windows Task Scheduler                                   | `ctypes`, `subprocess`, `os`  |
| 🤖 Discord Bot         | Full Discord bot with UI buttons and commands                               | `discord.py`                  |
| ⌨️ Keylogger           | System-wide keylogging, logs sent to Discord                                | `keyboard`, `discord_webhook` |
| 🖥️ Screen Capture      | Take and send desktop screenshots                                           | `pyautogui`, `discord.File`   |
| 📷 Webcam Capture      | Take and send webcam photos                                                  | `opencv-python`, `discord.File`|
| 🖱️ Mouse Manipulation  | Move mouse randomly to disrupt user                                         | `pyautogui`                   |
| 🔒 Screen Blocking     | Fullscreen overlay to block user input                                       | `tkinter`                     |
| 📌 Persistence         | Copy to Startup for auto-run on login                                       | `os`, `shutil`                |
| 🔔 Notifications       | Send status and alerts to Discord                                            | `discord`                     |
| 🌍 Location Retrieval  | Get geolocation via IP                                                       | `requests`                    |

---

## 🚀 Quickstart Checklist

1. **Install Python 3.8+** ([Download](https://www.python.org/downloads/windows/))
   - ✅ Add Python to PATH during install
2. **Clone or Download** this project
3. **Install Dependencies**
   ```bash
   pip install discord.py discord-webhook keyboard opencv-python imageio pyautogui requests
   ```
4. **Configure the Bot**
   - Edit `GhostPanel.py`:
     - Replace `add_token` with your Discord bot token
     - Set `NOTIFICATIONS_CHANNEL_ID` to your Discord channel ID
5. **Run the Bot**
   ```bash
   python GhostPanel.py
   ```
6. **Control via Discord**
   - Use the provided UI buttons or commands in your Discord server

---

## 🛠️ Detailed Features

<details>
<summary>🛡️ <b>Privilege Escalation</b></summary>

- Checks for admin rights; if not, relaunches with highest privileges using Task Scheduler.
- Required for actions like BSOD or system file changes.

</details>

<details>
<summary>⌨️ <b>Keylogger</b></summary>

- Hooks into system-wide keyboard events, logs all keystrokes.
- Sends logs to Discord via webhook, on demand or at intervals.
- Can be toggled remotely.

</details>

<details>
<summary>🖥️ <b>Screen Capture</b></summary>

- Takes a screenshot of the desktop and sends it to Discord.
- Triggered by a Discord button.

</details>

<details>
<summary>📷 <b>Webcam Capture</b></summary>

- Captures a photo from the webcam and sends to Discord.
- Handles errors if webcam is unavailable.

</details>

<details>
<summary>🖱️ <b>Mouse Manipulation</b></summary>

- Moves the mouse cursor randomly at intervals.
- Can be toggled on/off from Discord.

</details>

<details>
<summary>🔒 <b>Screen Blocking</b></summary>

- Creates a fullscreen overlay with a blocking message.
- Prevents user interaction until removed.

</details>

<details>
<summary>📌 <b>Persistence</b></summary>

- Copies itself to the Windows Startup folder for auto-run.
- Checks for duplicates before copying.

</details>

<details>
<summary>🌍 <b>Location Retrieval</b></summary>

- Uses `ip-api.com` to get geolocation info (IP, country, city, ISP, etc.).
- Sends info to Discord.

</details>

---

## 💻 Setup (Windows Only)

1. **Download or Copy the Project Folder**
2. **Edit `GhostPanel.py`**
   - Add your Discord bot token and channel ID
3. **Open Command Prompt in the folder**
4. **Run:**
   ```bash
   python GhostPanel.py
   ```

---

## 🕹️ Usage

- Interact with the bot via Discord using UI buttons or commands.
- All actions are performed on the Windows machine where the bot is running.
- Features can be toggled or triggered remotely.

---

## 📝 FAQ & Tips

**Q: The bot won't start!**
- Make sure Python 3.8+ is installed and added to PATH.
- Check that all dependencies are installed (`pip install ...`).

**Q: How do I get my Discord channel ID?**
- Enable Developer Mode in Discord settings, right-click your channel, and select "Copy ID".

**Q: Can I run this on Linux or Mac?**
- No, GhostPanel is designed for Windows only.

**Q: Is this legal?**
- Only use on systems you own or have explicit permission to test. Unauthorized use is illegal.

**Q: How do I stop the bot?**
- Close the Command Prompt window or stop the Python process.

**Tip:**
- For best results, use a dedicated Discord server for testing.
- Keep your bot token secret!

---

## ⚖️ Legal & Ethical Notice

> This software is intended for educational purposes and authorized environments only. **Do NOT use it on systems without explicit permission.** Unauthorized use may violate laws and result in severe penalties.

---

## 🏷️ Discord Controls & Commands

- 🔒 **Block Screen:** Activates the screen-blocking overlay.
- 💀 **Trigger BSOD:** Attempts to force a Blue Screen of Death (requires admin).
- 🖱️ **Mess with Mouse:** Starts/stops mouse disruption.
- 🦠 **Run EXE:** Decodes and runs embedded executable (if present).
- 🖥️ **Screenshot:** Captures and sends a screenshot.
- 📷 **Webcam Photo:** Captures and sends a webcam photo.
- ⌨️ **Keylogger:** Starts/stops keylogger, sends logs to Discord.

> The bot may also support text commands. See the code for details or extend as needed.

---

<div align="center">

✨ **Happy Hacking (Ethically)!** ✨

<img src="https://img.shields.io/badge/Discord%20Remote%20Admin-GhostPanel-8e44ad?style=for-the-badge" />

</div>

</div>
