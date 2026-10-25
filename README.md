# ASCII Banner Generator

A lightweight Python CLI tool that converts text into customizable ASCII art banners with colored terminal output.

## Features

- Convert text into ASCII art banners
- Choose from 7 terminal colors
- Interactive command-line interface
- Supports multiple banners in one session
- Simple and beginner-friendly
- Lightweight with minimal dependencies

## Requirements

- Python 3.8 or newer
- `pyfiglet`
- `colorama`

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/ascii-banner-generator.git
cd ascii-banner-generator
```

Replace `YOUR-USERNAME` with your GitHub username.

**2. Install dependencies**

```bash
python -m pip install pyfiglet colorama
```

**3. Run the program**

```bash
python ascii_banner.py
```

## Usage

1. Launch the program.
2. Enter the text you want to convert.
3. Choose a color.
4. Your ASCII banner will appear in the terminal.

Type `exit` to quit the program.

## Available Colors

- Red
- Green
- Blue
- Cyan
- Magenta
- Yellow
- White

## Example

```text
========================================
       ASCII BANNER GENERATOR
========================================

Enter text (or 'exit' to quit): HELLO

Available colors: red, green, blue, cyan, magenta, yellow, white
Choose a color: cyan

 _   _ _____ _     _     ___
| | | | ____| |   | |   / _ \
| |_| |  _| | |   | |  | | | |
|  _  | |___| |___| |__| |_| |
|_| |_|_____|_____|_____\___/
```

*The output style depends on the selected font and text.*

## Technologies

- Python
- Pyfiglet
- Colorama

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
