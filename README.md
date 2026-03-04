# Random Quote Generator

A desktop Python app built with Tkinter that fetches inspirational quotes from the ZenQuotes API and can read them aloud using macOS text-to-speech.

## Features

- Fetches a random quote from the internet
- Displays quote text and author in a simple GUI
- Keeps the UI responsive using background threads
- Speaks the current quote aloud with macOS `say`
- Handles network/API errors gracefully

## Tech Stack

- Python 3.10+
- Tkinter (built-in GUI library)
- `urllib` + `json` (built-in HTTP/JSON handling)
- `threading` (non-blocking UI)
- macOS `say` command (text-to-speech)

## Requirements

- macOS (for voice output via `say`)
- Python 3.10 or newer
- Tk support for Python (`tkinter`, usually included)
- Internet connection (to fetch quotes)

> Note: No third-party pip packages are required for this project.

## Installation

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. (Optional but recommended) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies (there are none beyond stdlib, but this keeps workflow consistent):

   ```bash
   pip install -r requirements.txt
   ```

## Run the App

```bash
python3 quote_generator.py
```

## How to Use

1. Click **Get Random Quote**.
2. Wait for the quote to load.
3. Click **Speak Quote** to hear it read aloud.

## Project Structure

```text
.
├── quote_generator.py
├── requirements.txt
├── code_explanation.md
└── README.md
```

## Troubleshooting

- **Quote fetch fails:** Check internet connection and try again.
- **No voice output:** Ensure you are on macOS and `say` is available.
- **Tkinter errors:** Reinstall Python with Tk support (python.org installer usually includes it).

## License

Add a license section here if/when you choose one (e.g., MIT).
