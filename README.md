# Nmap Network Scanner

Python-based network scanner that uses Nmap to discover devices on a local network.

## Features

- Discover active devices on a local network
- Uses the Nmap scanning engine
- Simple command-line interface
- Fast host discovery

## Technologies

- Python
- Nmap
- python-nmap

## Installation

First install the required dependency:

```bash
pip install python-nmap
```

Make sure Nmap is installed on your system as well.

## Usage

Run the scanner:

```bash
python scanner.py
```

Then enter a network range such as:

```
192.168.1.0/24
```

The program will scan the network and list active devices.

## Future Improvements

- Port scanning
- OS detection
- Export results to CSV
- Web dashboard
