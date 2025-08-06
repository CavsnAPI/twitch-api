#!/usr/bin/env python3
"""
Basic usage examples for the Twitch API Client
"""

import os
import sys
from typing import Dict, Any

# Add parent directory to path to import the client
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from twitch_api_client import TwitchAPIClient, TwitchAPIError


def print_streamer_info(client: TwitchAPIClient, channel: str):
    """Print comprehensive streamer information"""
    print(f"\n{'='*50}")
    print(f"📺 CHANNEL: {channel.upper()}")
    print(f"{'='*50}")
    
    try:
        # Get basic streamer info
        info = client.get_streamer_info(channel)
        
        if info and 'user' in info:
            user = info['user']
            print(f"👤 Display Name: {user.get('displayName', 'N/A')}")
            print(f"📝 Description: {user.get('description', 'N/A')}")
            print(f"🔗 Profile URL: https://twitch.tv/{channel}")
            
            # Check stream status
            stream = user.get('stream')
            if stream:
                print(f"\n🔴 STATUS: LIVE")
                print(f"📺 Title: {stream.get('title', 'No title')}")
                
                game = stream.get('game')
                if game:
                    print(f"🎮 Game: {game.get('name', 'N/A')}")
                
                print(f"👥 Viewers: {stream.get('viewersCount', 0):,}")
                print(f"🏷️  Stream Type: {stream.get('type', 'N/A')}")
            else:
                print(f"\n⭕ STATUS: OFFLINE")
        
        # Get additional info
        print(f"\n📊 ADDITIONAL DATA:")
        
        # Get user ID
        user_data = client.get_user_id(channel)
        if user_data and 'user' in user_data:
            print(f"🆔 User ID: {user_data['user'].get('id', 'N/A')}")
        
        # Get viewer count (if live)
        try:
            viewers = client.get_stream_viewers(channel)
            if viewers:
                print(f"👁️  Current Viewers: {viewers}")
        except:
            print(f"👁️  Current Viewers: Not available")
        
        # Get stream tags
        try:
            tags = client.get_stream_tags(channel)
            if tags:
                print(f"🏷️  Stream Tags: Available")
        except:
            print(f"🏷️  Stream Tags: Not available")
            
    except TwitchAPIError as e:
        print(f"❌ API Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")


def demonstrate_all_endpoints(client: TwitchAPIClient, channel: str):
    """Demonstrate all available endpoints"""
    print(f"\n🔧 TESTING ALL ENDPOINTS FOR: {channel}")
    print(f"{'='*60}")
    
    endpoints = [
        ("Channel Panels", lambda: client.get_channel_panels(channel)),
        ("Streamer Info", lambda: client.get_streamer_info(channel)),
        ("Channel Videos", lambda: client.get_channel_videos(channel)),
        ("Stream Viewers", lambda: client.get_stream_viewers(channel)),
        ("User ID", lambda: client.get_user_id(channel)),
        ("Channel Points Context", lambda: client.get_channel_points_context(channel)),
        ("Chat Restrictions", lambda: client.get_chat_restrictions(channel)),
        ("Pinned Chat", lambda: client.get_pinned_chat(channel)),
        ("Channel Goals", lambda: client.get_channel_goals(channel)),
        ("Channel Leaderboards", lambda: client.get_channel_leaderboards(channel)),
        ("Stream Tags", lambda: client.get_stream_tags(channel)),
    ]
    
    for name, func in endpoints:
        try:
            result = func()
            status = "✅ Success" if result else "⚠️  Empty Response"
            print(f"{name:<25} | {status}")
        except Exception as e:
            print(f"{name:<25} | ❌ Error: {str(e)[:30]}...")
    
    # Test viewer card (needs username)
    try:
        # Use a common username for testing
        result = client.get_viewer_card(channel, "testuser")
        status = "✅ Success" if result else "⚠️  Empty Response"
        print(f"{'Viewer Card':<25} | {status}")
    except Exception as e:
        print(f"{'Viewer Card':<25} | ❌ Error: {str(e)[:30]}...")


def main():
    """Main function to run examples"""
    print("🎮 Twitch API Client - Example Usage")
    print("=" * 50)
    
    # Get API key from environment variable
    api_key = os.getenv("RAPIDAPI_KEY")
    
    if not api_key:
        print("❌ Error: Please set RAPIDAPI_KEY environment variable")
        print("Example: export RAPIDAPI_KEY='your_key_here'")
        return
    
    # Initialize client
    try:
        client = TwitchAPIClient(api_key)
        print("✅ Client initialized successfully!")
    except Exception as e:
        print(f"❌ Failed to initialize client: {e}")
        return
    
    # Test channels (mix of likely live and offline streamers)
    test_channels = ["xQc", "ninja", "pokimane", "shroud", "summit1g"]
    
    # Demonstrate detailed info for first channel
    print_streamer_info(client, test_channels[0])
    
    # Quick test of all endpoints
    demonstrate_all_endpoints(client, test_channels[0])
    
    # Show basic info for other channels
    print(f"\n📋 QUICK OVERVIEW OF OTHER CHANNELS:")
    print(f"{'='*60}")
    
    for channel in test_channels[1:3]:  # Test 2 more channels
        try:
            info = client.get_streamer_info(channel)
            if info and 'user' in info:
                user = info['user']
                stream = user.get('stream')
                status = "🔴 LIVE" if stream else "⭕ OFFLINE"
                viewers = f" ({stream.get('viewersCount', 0):,} viewers)" if stream else ""
                print(f"📺 {channel:<15} | {status}{viewers}")
            else:
                print(f"📺 {channel:<15} | ❓ No data")
        except Exception as e:
            print(f"📺 {channel:<15} | ❌ Error: {str(e)[:30]}...")
    
    print(f"\n✨ Demo completed! Check the README.md for more examples.")


if __name__ == "__main__":
    main() 