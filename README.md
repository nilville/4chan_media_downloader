# 4chan Media Downloader

A simple Python script that automates downloading media files from a specified 4chan thread using Selenium.

## Features

- Automatically scrapes and downloads images/videos from a 4chan thread
- Organizes downloads in a `4chan_downloads/` folder
- Uses Selenium WebDriver for dynamic content loading

## Requirements

- Python 3.6+
- Google Chrome installed
- ChromeDriver (matching your Chrome version)

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/nilville/4chan_media_downloader.git
cd 4chan_media_downloader
```

2. **Install Required Dependencies**

- Install the required Python packages using pip :
```bash
pip install selenium requests 
```

## Usage 

- Open the 4chan_media_downloader.py file 
- Replace the placeholder URL with the actual 4chan thread URL :
```bash
driver.get('https://boards.4chan.org/b/thread/123456789')  # Replace with actual thread URL
```
- Run the script : 
```bash
python 4chan_media_downloader.py
```