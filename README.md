# Twitch API Client 🎮

A powerful Python client library for accessing Twitch data through RapidAPI. Get comprehensive information about Twitch streamers, channels, chat, and much more with just a few lines of code!

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Features

- **Easy to Use**: Simple and intuitive API interface
- **Comprehensive**: Access to 12+ different Twitch data endpoints
- **Well Documented**: Full documentation with examples
- **Type Hints**: Complete type annotations for better development experience
- **Error Handling**: Robust error handling with custom exceptions
- **Production Ready**: Built for reliability and performance

## 📋 Available Endpoints

| Method | Description | Parameters |
|--------|-------------|------------|
| `get_channel_panels()` | Get channel panels information | `channel` |
| `get_viewer_card()` | Get viewer card for specific user | `channel`, `username` |
| `get_streamer_info()` | Get comprehensive streamer info | `channel` |
| `get_channel_videos()` | Get recent channel videos | `channel` |
| `get_stream_viewers()` | Get current viewer count | `channel` |
| `get_user_id()` | Get user ID information | `channel` |
| `get_channel_points_context()` | Get channel points info | `channel` |
| `get_chat_restrictions()` | Get chat restrictions | `channel` |
| `get_pinned_chat()` | Get pinned chat messages | `channel` |
| `get_channel_goals()` | Get active channel goals | `channel` |
| `get_channel_leaderboards()` | Get channel leaderboards | `channel` |
| `get_stream_tags()` | Get current stream tags | `channel` |

## 🔧 Installation

Install the package using pip:

```bash
pip install twitch-api-client
```

## 🔑 Getting Started

### 1. Get Your RapidAPI Key

First, you need to subscribe to the Twitch API on RapidAPI:

1. Visit the [Twitch API on RapidAPI](https://rapidapi.com/cavsn/api/twitch-api8)
2. Subscribe to the API
3. Copy your RapidAPI key from the dashboard

### 2. Basic Usage

```python
from twitch_api_client import TwitchAPIClient

# Initialize the client with your RapidAPI key
client = TwitchAPIClient(rapidapi_key="your_rapidapi_key_here")

# Get channel panels
panels = client.get_channel_panels("xQc")
print(panels)

# Get streamer information
streamer_info = client.get_streamer_info("ninja")
print(f"Is live: {streamer_info}")

# Get current viewers
viewers = client.get_stream_viewers("shroud")
print(f"Current viewers: {viewers}")
```

## 📖 Detailed Examples

### Getting Channel Information

```python
from twitch_api_client import TwitchAPIClient

client = TwitchAPIClient("your_rapidapi_key")

# Get comprehensive streamer info
channel = "pokimane"
info = client.get_streamer_info(channel)

if info and 'user' in info:
    user = info['user']
    print(f"Channel: {user.get('displayName', 'N/A')}")
    print(f"Description: {user.get('description', 'N/A')}")
    
    # Check if stream is live
    stream = info.get('user', {}).get('stream')
    if stream:
        print(f"🔴 LIVE - {stream.get('title', 'No title')}")
        print(f"Game: {stream.get('game', {}).get('name', 'N/A')}")
        print(f"Viewers: {stream.get('viewersCount', 0)}")
    else:
        print("⭕ Offline")
```

### Working with Viewer Cards

```python
# Get viewer card information
channel = "xQc"
username = "viewer123"

try:
    card = client.get_viewer_card(channel, username)
    print(f"Viewer card for {username} in {channel}:")
    print(card)
except Exception as e:
    print(f"Error getting viewer card: {e}")
```

### Channel Analytics

```python
# Get multiple channel metrics
channel = "summit1g"

# Get viewer count
viewers = client.get_stream_viewers(channel)

# Get channel goals
goals = client.get_channel_goals(channel)

# Get leaderboards
leaderboards = client.get_channel_leaderboards(channel)

# Get stream tags
tags = client.get_stream_tags(channel)

print(f"Analytics for {channel}:")
print(f"Current viewers: {viewers}")
print(f"Goals: {goals}")
print(f"Leaderboards: {leaderboards}")
print(f"Tags: {tags}")
```

### Error Handling

```python
from twitch_api_client import TwitchAPIClient, TwitchAPIError

client = TwitchAPIClient("your_rapidapi_key")

try:
    # This might fail if channel doesn't exist
    info = client.get_streamer_info("nonexistentchannel12345")
    print(info)
except TwitchAPIError as e:
    print(f"API Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## 🔐 Environment Variables

For security, it's recommended to store your API key in environment variables:

```python
import os
from twitch_api_client import TwitchAPIClient

# Set your API key as an environment variable
# export RAPIDAPI_KEY="your_rapidapi_key_here"

api_key = os.getenv("RAPIDAPI_KEY")
if not api_key:
    raise ValueError("Please set RAPIDAPI_KEY environment variable")

client = TwitchAPIClient(api_key)
```

## 📊 Response Format

All methods return dictionaries containing the API response data. The exact structure depends on the endpoint, but here's a general example:

```python
{
    "user": {
        "id": "123456789",
        "login": "streamername",
        "displayName": "StreamerName",
        "description": "Streamer description...",
        "profileImageURL": "https://...",
        "stream": {
            "id": "987654321",
            "title": "Stream Title",
            "game": {
                "name": "Game Name"
            },
            "viewersCount": 1234
        }
    }
}
```

## ⚡ Rate Limits

Be aware of RapidAPI rate limits for your subscription tier. The client doesn't implement rate limiting, so make sure to handle this in your application if needed.

## 🛠️ Development

### Setting up for development:

```bash
git clone https://github.com/cavsn/twitch-api-client.git
cd twitch-api-client
pip install -e ".[dev]"
```

### Running tests:

```bash
pytest tests/
```

## 📝 Requirements

- Python 3.7+
- requests>=2.25.0
- A valid RapidAPI subscription to the Twitch API

## 🔗 Links

- **RapidAPI Twitch API**: [Subscribe Here](https://rapidapi.com/cavsn/api/twitch-api8)
- **Documentation**: [Full API Documentation](https://rapidapi.com/cavsn/api/twitch-api8)
- **GitHub Repository**: [Source Code](https://github.com/cavsn/twitch-api-client)
- **Issues**: [Report Issues](https://github.com/cavsn/twitch-api-client/issues)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 💬 Support

If you encounter any issues or have questions:

1. Check the [documentation](https://rapidapi.com/cavsn/api/twitch-api8)
2. Search existing [issues](https://github.com/cavsn/twitch-api-client/issues)
3. Create a new issue if needed

## 🙏 Acknowledgments

- Thanks to RapidAPI for providing the platform
- Twitch for the amazing streaming platform
- All contributors to this project

---

Made with ❤️ for the Twitch community 