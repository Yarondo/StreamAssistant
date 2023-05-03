import win32gui
import win32api
import win32con
import time
import pyaudio
import struct
import numpy as np
import webbrowser
import psutil

# Set up PyAudio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
THRESHOLD = 0.1

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

# Set up browser detection
chrome_processes = [process for process in psutil.process_iter() if process.name() == "chrome.exe"]

# Set up mute key
VK_VOLUME_MUTE = 0xAD  # VK_VOLUME_MUTE virtual key code

# Function to check if a Chrome tab is playing audio
def check_audio():
    for process in chrome_processes:
        try:
            # Get the window handle of the Chrome process
            hwnd = win32gui.FindWindowEx(None, None, None, None)
            win32gui.EnumWindows(EnumWindowsProc, process.pid)
            
            # Get the process ID of the tab with focus
            focused_pid = win32process.GetWindowThreadProcessId(hwnd)[1]
            
            # Get the audio data from the PyAudio stream
            data = stream.read(CHUNK)
            data_int = np.array(struct.unpack(f"{CHUNK}h", data)) / 32768.0
            if np.max(data_int) > THRESHOLD:
                # Mute the volume if audio is detected
                win32api.keybd_event(VK_VOLUME_MUTE, 0, 0, 0)
                return True
        except:
            pass
    return False

# Main loop
while True:
    audio_playing = check_audio()
    if audio_playing:
        print("Audio detected, muting music.")
    else:
        print("No audio detected.")
    time.sleep(1)
