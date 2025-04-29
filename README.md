# WindowsCrashHandaler

**WindowsCrashHandaler** is a Python-based Discord bot designed for controlled environments such as Capture The Flag (CTF) challenges or authorized remote administration tests. **Use this tool only on systems for which you have explicit permission.**

> **⚠ Disclaimer:**  
> This tool is intended solely for educational and authorized testing purposes. Unauthorized use of these techniques is illegal and unethical.
A new version with embedded EXE, UAC bypass, webcam, and screenshot features is coming soon!
---

## 📌 Overview

**WindowsCrashHandaler** provides a suite of remote administration functionalities, including:
- 🔒 **Screen Blocking** – Opens a full-screen, always-on-top window to block the user’s screen.
- 💀 **BSOD Triggering** – Attempts to force a Blue Screen of Death (BSOD) via Windows APIs.
- 🖱 **Mouse Manipulation** – Randomly moves the mouse pointer to simulate erratic behavior.
- 🌍 **System & Location Information** – Collects and displays system details (user, computer name, OS info, IP address) along with geolocation data (using an external API) in an RGB-colored embed message.
- 🚀 **Startup Persistence** – Clones itself to the Windows Startup folder (`WindowsCrashHandaler.exe`) so that it runs automatically when the system boots.

---

## ⚙ How It Works

### 1️⃣ Discord Bot Setup
- Uses [discord.py](https://discordpy.readthedocs.io/) to connect to Discord.
- Sends an embed message to a specified Discord channel with system & location info on startup.

### 2️⃣ System Functions

#### 🔒 **Screen Blocking & Animation**
- Uses Tkinter to create a **full-screen blocking window** with the message `"🔒 SCREEN BLOCKED 🔒"`.
- An animated **spiral effect** is drawn on the screen.

#### 💀 **BSOD Triggering**
- Uses Windows API (`ctypes`) to adjust privileges and force a **Blue Screen of Death**.
- **⚠ Warning:** Extremely disruptive! Recommended only in VMs or test environments.

#### 🖱 **Mouse Manipulation**
- Uses [pyautogui](https://pyautogui.readthedocs.io/) to move the mouse randomly.
- Can be toggled **on/off** via an interactive Discord button.

### 3️⃣ 🌍 **Location & System Information**
- **Location Data:** Fetches geolocation details using [ip-api.com](http://ip-api.com).
- **System Data:** Gathers **username, computer name, OS details, and IP address**.
- **RGB Embed:** Generates a **random RGB color** for each embed.

### 4️⃣ 🎛 **Action Buttons (Discord UI)**
The bot sends an **embed message** with interactive buttons:
- 🔒 **Block Screen**
- 💀 **Trigger BSOD**
- 🖱 **Mess with Mouse**

Each button requires **Administrator permissions**.

### 5️⃣ 🚀 **Startup Persistence**
- The script **clones itself** to the Windows Startup folder as `WindowsCrashHandaler.exe` to persist after reboots.

---

## 🛠 Code Walkthrough

### **a. Startup Cloning**
- The `clone_to_startup()` function copies the script to Startup.

### **b. Screen Blocking & Animation**
- `screenblock()`: Opens a **fullscreen blocking window**.
- `animate()`: Draws a **spiral effect** on the screen.

### **c. Mouse Manipulation**
- `StartMouseMess()`: Moves the mouse randomly when **enabled**.

### **d. Location Information**
- `get_location()`: Fetches geolocation details via **ip-api.com**.

### **e. Action Buttons**
- `ActionButtons`: Defines **interactive buttons** (Block Screen, BSOD, Mouse Mess).

### **f. Notification Embed**
- `send_notification()`: Collects **system + location info**, sends **RGB embed** to Discord.

### **g. Main Event Loop**
- `on_ready()`:  
  - Clones script to **Startup**.  
  - Sends system info & action buttons to Discord.

---

## 📦 Dependencies

Install required libraries:
```bash
pip install discord.py psutil pyautogui requests
