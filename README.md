# Stream Assistant

## Overview

StreamAssistant is a Python script for Windows that automatically mutes your music when it detects audio of someone talking in one of your Chrome browser tabs. The script uses the PyAudio library to capture audio data from your microphone, and the win32api library to simulate a key press that mutes the volume.

## Installation

To use StreamAssistant, you'll need to install Python 3 and a few Python packages. Here's how to get started:

1. Install Python 3 from the [official website](https://www.python.org/downloads/).

2. Install the following Python packages using pip:
   ```
   pip install win32gui win32api win32con pyaudio numpy psutil
   ```

   This command installs the `win32gui`, `win32api`, `win32con`, `pyaudio`, `numpy`, and `psutil` libraries.

3. Download the `streamassistant.py` script and save it to your computer.

## Usage

To use StreamAssistant, follow these steps:

1. Open a terminal window and navigate to the directory where you saved the `streamassistant.py` script.

2. Run the script by typing `python streamassistant.py` and pressing Enter.

3. Start playing music on your computer.

4. Open a Chrome browser tab and start playing a video with audio.

5. The script will automatically detect the audio and mute your music.

To stop the script, press `Ctrl + C` in the terminal window.

You'll also need to set `THRESHOLD` to a value that works well for your system. This value determines the audio level at which the music is muted.

When you run this script, it will continuously check for audio playing in Chrome tabs and mute your music if it detects audio. Note that this script assumes that you have at least one Chrome tab with audio playing. If you don't, it will continue running and checking for audio. You can stop the script by pressing Ctrl+C in the terminal.

If you want to automatically launch Chrome when the script starts, you can add the following code to the beginning of the script:

```python
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"  # path to Chrome executable
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab('https://www.google.com')
``` 

Replace `C:/Program Files (x86)/Google/Chrome/Application/chrome.exe` with the path to your Chrome executable. This code will open a new Chrome tab when the script starts.

## Configuration

You can configure the script by modifying the following variables at the beginning of the `streamassistant.py` file:

- `CHUNK`: The number of audio samples per buffer.
- `FORMAT`: The format of the audio samples.
- `CHANNELS`: The number of audio channels.
- `RATE`: The sampling rate of the audio.
- `THRESHOLD`: The audio threshold at which the music is muted.
- `VK_VOLUME_MUTE`: The virtual key code for the mute key.

## Contributing

If you'd like to contribute to Chrome Audio Mute, feel free to fork the repository and submit a pull request. Please follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide and include tests for any new functionality.

## License

Chrome Audio Mute is released under the [GNU 3.0](https://opensource.org/license/gpl-3-0/). See `LICENSE` for more information.
