# AirlinersNet Image Scraper

A Python library for downloading aircraft images from Airliners.net.

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install requests beautifulsoup4
```

## Usage

Basic usage example:

```python
from airliners import AirlinersNetScraper

# Create scraper instance with custom save path
scraper = AirlinersNetScraper(save_path="aircraft_images")

# Download images for specific aircraft
files = scraper.get_images("F/A-18")
print(f"Number of downloaded images: {len(files)}")
```

### Parameters

- `save_path`: Directory where images will be saved (default: "imgs")
- `aircraft_name`: Name of the aircraft to search for (supports various formats like "F/A-18", "Bf-109", etc.)

### Return Value

The `get_images()` method returns a list of paths to the downloaded image files.

## Features

- Automatic directory creation
- Safe filename handling (replaces invalid characters)
- Error handling for failed downloads
- Session management for efficient requests
- High-resolution image downloads
- Cross-platform compatibility

## Requirements

- Python 3.6+
- requests
- beautifulsoup4

## License

MIT License

## Note

Please be respectful of Airliners.net's terms of service and use this scraper responsibly. 
