# Windows Discord Remote Control Bot

## Overview

`GhostPanel.py` is a multi-functional Discord bot for Windows, designed for remote administration and control. It provides a range of features accessible via Discord commands and interactive UI buttons, including privilege escalation, keylogging, screen and webcam capture, mouse manipulation, and more.

> **Warning:** This project is for educational and authorized testing purposes only. Unauthorized use of keyloggers or remote administration tools is illegal and unethical.

---

## Features (Detailed)

- 🛡️ **Privilege Escalation:**
  - **How it works:** The bot checks if it is running with administrator rights using the Windows API via `ctypes.windll.shell32.IsUserAnAdmin()`. If not, it uses the Windows Task Scheduler (`schtasks`) to create a scheduled task that relaunches the script with the highest privileges. This allows the bot to access protected system features that require admin rights, such as triggering a BSOD or modifying system files.
  - **Libraries/APIs:** `ctypes`, `subprocess`, `sys`, `os`, `datetime`

- 🤖 **Discord Bot Integration:**
  - **How it works:** The bot uses the `discord.py` library to connect to Discord as a bot user. It listens for events, commands, and button presses in a specified channel. The bot can send messages, files, and rich embeds, and provides interactive UI elements (buttons) for remote control. All actions are performed on the host Windows machine.
  - **Libraries/APIs:** `discord`, `discord.ext.commands`, `discord.ui.View`

- ⌨️ **Keylogger:**
  - **How it works:** The bot uses the `keyboard` library to hook into system-wide keyboard events. It records all keystrokes, including special keys (e.g., Enter, Backspace, Shift), and stores them in a log. The logs can be sent to a Discord channel via webhook, either on demand or at regular intervals (default: every 15 seconds). The keylogger can be toggled on or off remotely.
  - **Libraries/APIs:** `keyboard`, `discord_webhook`, `threading`, `Timer`

- 🖥️ **Screen Capture:**
  - **How it works:** The bot uses the `pyautogui` library to take a screenshot of the user's desktop. The screenshot is saved as an image file and sent to Discord as an attachment, often embedded in a message for easy viewing. This feature can be triggered remotely via a Discord button.
  - **Libraries/APIs:** `pyautogui`, `discord.File`

- 📷 **Webcam Capture:**
  - **How it works:** The bot uses the `opencv-python` (`cv2`) library to access the system's webcam. It captures a single frame (photo) and saves it as an image file, which is then sent to Discord. This can be triggered remotely via a Discord button. If the webcam is unavailable or access is denied, the bot will report an error.
  - **Libraries/APIs:** `cv2`, `discord.File`

- 🖱️ **Mouse Manipulation ("Mess with Mouse"):**
  - **How it works:** The bot uses the `pyautogui` library to move the mouse cursor to random positions on the screen at regular intervals, making the computer difficult to use. This feature runs in a background thread and can be toggled on or off from Discord.
  - **Libraries/APIs:** `pyautogui`, `threading`, `random`, `time`

- 🔒 **Screen Blocking:**
  - **How it works:** The bot creates a fullscreen, always-on-top window using `tkinter` that covers the entire display and prevents user interaction. The window displays a "SCREEN BLOCKED" message and can optionally show an animated spiral pattern. The window cannot be closed by normal means, effectively locking the user out until the bot removes it.
  - **Libraries/APIs:** `tkinter`, custom animation logic

- 📌 **Persistence (Startup Cloning):**
  - **How it works:** The bot copies its own executable/script to the Windows Startup folder so it runs automatically every time the user logs in. It renames itself to `WindowsCrashHandaler.exe` (note the typo: "Handaler") and places the file at `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\WindowsCrashHandaler.exe`. The bot checks if the file already exists before copying, to avoid duplicates.
  - **Libraries/APIs:** `os`, `sys`, `shutil`

- 🔔 **Notifications:**
  - **How it works:** The bot can send custom notifications, status updates, or alerts to a specified Discord channel. This is useful for confirming actions, reporting errors, or providing updates on the bot's status.
  - **Libraries/APIs:** `discord`, custom notification logic

- 🌍 **Location Retrieval:**
  - **How it works:** The bot attempts to determine the user's geographic location by making an HTTP request to the `ip-api.com` geolocation service. It parses the returned JSON to extract IP address, country, city, latitude/longitude, ISP, and more, then sends this information to Discord.
  - **Libraries/APIs:** `requests`, `json`

---

## Python & Dependency Installation Guide

### 1. Install Python (Windows)
- Download Python from the official website: https://www.python.org/downloads/windows/
- Run the installer and **make sure to check the box that says "Add Python to PATH"** before clicking Install.
- Complete the installation process.
- To verify installation, open Command Prompt and run:
  ```
  python --version
  ```
  You should see the installed Python version number.

### 2. Install Required Python Packages
- Open Command Prompt (cmd) or PowerShell in your project folder.
- Run the following command to install all dependencies:
  ```
  pip install discord.py discord-webhook keyboard opencv-python imageio pyautogui requests
  ```

If you encounter any errors, ensure Python and pip are correctly installed and available in your system PATH.

---

## Setup (Windows Only)

1. **Download or Copy the Project Folder**
   - Make sure all files are in the same folder on your Windows machine.

2. **Configure the Bot**
   - Open `GhostPanel.py` in a text editor.
   - Replace `add_token` with your Discord bot token.
   - Set `NOTIFICATIONS_CHANNEL_ID` to your Discord channel ID.

3. **Run the Bot**
   - In Command Prompt or PowerShell, run:
     ```
     python GhostPanel.py
     ```

---

## Usage

- Interact with the bot via Discord using the provided UI buttons or commands.
- Features can be toggled or triggered remotely from Discord.
- All actions are performed on the Windows machine where the bot is running.

---

## Legal & Ethical Notice

This software is intended for educational purposes and authorized environments only. Do **not** use it on systems without explicit permission. Unauthorized use may violate laws and result in severe penalties.

## Discord Controls & Commands

The bot provides interactive controls in Discord, typically as buttons on embeds. Each button triggers a specific action on the target machine:

- 🔒 **Block Screen:** Activates the screen-blocking overlay.
- 💀 **Trigger BSOD:** Attempts to force a Blue Screen of Death (BSOD) on the target (requires admin). Uses Windows API calls to trigger a system crash.
- 🖱️ **Mess with Mouse:** Starts or stops the mouse disruption feature, moving the cursor randomly.
- 🦠 **Run EXE:** Decodes and runs the embedded executable (if present in the project files).
- 🖥️ **Screenshot:** Captures and sends a screenshot of the desktop.
- 📷 **Webcam Photo:** Captures and sends a webcam photo.
- ⌨️ **Keylogger:** Starts or stops the keylogger, and can send logs to Discord.

> The bot may also support text commands, depending on your configuration. See the code for details or extend as needed. 
