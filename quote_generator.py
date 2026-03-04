#!/usr/bin/env python3
import urllib.request
import json
import subprocess
import threading
import tkinter as tk
from tkinter import messagebox

def get_random_quote():
    """Fetches a random quote from the ZenQuotes API."""
    url = "https://zenquotes.io/api/random"
    try:
        # Send a browser-like User-Agent to avoid some basic API blocks.
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                return data[0].get('q'), data[0].get('a')
    except Exception as e:
        print(f"Error fetching quote: {e}")
    return None, None

def speak_quote(text):
    """Speaks the given text using the macOS 'say' command."""
    try:
        # Uses the native macOS text-to-speech CLI.
        subprocess.run(["say", text])
    except Exception as e:
        print(f"Text-to-Speech Error: {e}")

def _fetch_and_update():
    """Runs in a background thread: fetches quote and schedules UI update."""
    quote, author = get_random_quote()
    # Tkinter widgets must be updated on the main thread.
    root.after(0, _apply_quote, quote, author)

def _apply_quote(quote, author):
    """Called on the main thread to update the UI after fetching."""
    global current_quote_text
    if quote and author:
        current_quote_text = f"{quote}... by {author}"
        quote_label.config(text=f'"{quote}"', fg="#333333")
        author_label.config(text=f"— {author}")
        speak_btn.config(state=tk.NORMAL)
    else:
        messagebox.showerror("Error", "Failed to fetch a quote. Check your internet connection.")
        quote_label.config(text="Failed to fetch a quote.", fg="red")
        speak_btn.config(state=tk.DISABLED)
    fetch_btn.config(state=tk.NORMAL)

def update_quote():
    """Fetches a new quote and updates the UI."""
    quote_label.config(text="Fetching...", fg="#888888")
    author_label.config(text="")
    # Prevent repeated clicks while a request is in progress.
    fetch_btn.config(state=tk.DISABLED)
    # Keep UI responsive while waiting for network I/O.
    threading.Thread(target=_fetch_and_update, daemon=True).start()

def on_speak_clicked():
    """Handler for the Speak button."""
    if current_quote_text:
        # Run speech in a worker thread so the UI does not freeze.
        threading.Thread(target=speak_quote, args=(current_quote_text,), daemon=True).start()

# --- Main Application Setup ---
current_quote_text = ""

# Create the main window
root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("600x400")
root.configure(bg="#f4f4f9")

# Title Label
title_label = tk.Label(root, text="Inspirational Quotes", font=("Helvetica", 24, "bold"), bg="#f4f4f9", fg="#333333")
title_label.pack(pady=20)

# Quote Formatting Frame
quote_frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.GROOVE)
quote_frame.pack(padx=30, pady=10, fill=tk.BOTH, expand=True)

# Quote Text Label
quote_label = tk.Label(quote_frame, text="Click the button to fetch a quote!", font=("Helvetica", 16, "italic"), bg="#ffffff", fg="#555555", wraplength=500, justify="center")
quote_label.pack(expand=True, pady=(20, 5), padx=20)

# Author Text Label
author_label = tk.Label(quote_frame, text="", font=("Helvetica", 14, "bold"), bg="#ffffff", fg="#222222")
author_label.pack(pady=(0, 20))

# Button Frame
button_frame = tk.Frame(root, bg="#f4f4f9")
button_frame.pack(pady=20)

# Fetch Button
fetch_btn = tk.Button(button_frame, text="Get Random Quote", font=("Helvetica", 14), command=update_quote)
fetch_btn.pack(side=tk.LEFT, padx=10)

# Speak Button (Initially disabled)
speak_btn = tk.Button(button_frame, text="Speak Quote", font=("Helvetica", 14), command=on_speak_clicked, state=tk.DISABLED)
speak_btn.pack(side=tk.LEFT, padx=10)

# Start the application loop
root.mainloop()
