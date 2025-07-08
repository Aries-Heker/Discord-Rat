# 👻 GhostPanel

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows)
![Discord Bot](https://img.shields.io/badge/Discord%20Bot-Online-brightgreen?logo=discord)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 🚨 WARNING

**This project is for educational and authorized testing purposes only. Unauthorized use of keyloggers or remote administration tools is illegal and unethical.**

---

## 🗂️ Features

| Feature                | Description                                      | Libraries/APIs                |
|------------------------|--------------------------------------------------|-------------------------------|
| 🛡️ Privilege Escalation | Run as admin using Windows Task Scheduler        | `ctypes`, `subprocess`, `os`  |
| 🤖 Discord Bot         | Full Discord bot with UI buttons and commands    | `discord.py`                  |
| ⌨️ Keylogger           | System-wide keylogging, logs sent to Discord     | `keyboard`, `discord_webhook` |
| 🖥️ Screen Capture      | Take and send desktop screenshots                | `pyautogui`, `discord.File`   |
| 📷 Webcam Capture      | Take and send webcam photos                      | `opencv-python`, `discord.File`|
| 🖱️ Mouse Manipulation  | Move mouse randomly to disrupt user              | `pyautogui`                   |
| 🔒 Screen Blocking     | Fullscreen overlay to block user input           | `tkinter`                     |
| 📌 Persistence         | Copy to Startup for auto-run on login            | `os`, `shutil`                |
| 🔔 Notifications       | Send status and alerts to Discord                | `discord`                     |
| 🌍 Location Retrieval  | Get geolocation via IP                           | `requests`                    |

---

## 🧭 Overview

GhostPanel is a powerful Discord bot for Windows that lets you control a PC remotely via Discord commands and buttons. It supports privilege escalation, keylogging, screenshots, webcam capture, mouse disruption, screen blocking, persistence, notifications, and more.

---

## 🚀 Quickstart

1. **Install Python 3.8+** ([Download here](https://www.python.org/downloads/windows/))
   - Make sure to check "Add Python to PATH" during install.
2. **Clone or Download** this project.
3. **Install dependencies:**
   ```bash
   pip install discord.py discord-webhook keyboard opencv-python imageio pyautogui requests
   ```
4. **Configure the bot:**
   - Open `GhostPanel.py` in a text editor.
   - Replace `add_token` with your Discord bot token.
   - Set `NOTIFICATIONS_CHANNEL_ID` to your Discord channel ID.
5. **Run the bot:**
   ```bash
   python GhostPanel.py
   ```
6. **Control via Discord:**
   - Use the provided UI buttons or commands in your Discord server.

---

## 🛠️ Setup (Windows Only)

- Download or copy all files to the same folder on your Windows machine.
- Edit `GhostPanel.py` to add your bot token and channel ID.
- Open Command Prompt in the folder and run:
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

**Tips:**
- Use a dedicated Discord server for testing.
- Keep your bot token secret!

---

## ⚖️ Legal & Ethical Notice

This software is intended for educational purposes and authorized environments only. **Do NOT use it on systems without explicit permission.** Unauthorized use may violate laws and result in severe penalties.

---

## 🏷️ Discord Controls & Commands

- 🔒 Block Screen: Activates the screen-blocking overlay.
- 💀 Trigger BSOD: Attempts to force a Blue Screen of Death (requires admin).
- 🖱️ Mess with Mouse: Starts/stops mouse disruption.
- 🦠 Run EXE: Decodes and runs embedded executable (if present).
- 🖥️ Screenshot: Captures and sends a screenshot.
- 📷 Webcam Photo: Captures and sends a webcam photo.
- ⌨️ Keylogger: Starts/stops keylogger, sends logs to Discord.

> The bot may also support text commands. See the code for details or extend as needed.

---

**Happy Hacking (Ethically)!**
