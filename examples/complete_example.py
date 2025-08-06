#!/usr/bin/env python3
"""
Complete example demonstrating all Twitch API Client features
"""

import os
import sys
from typing import Dict, Any

# Add parent directory to path to import the client
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from twitch_api_client import TwitchAPIClient, TwitchAPIError


class TwitchAnalytics:
    """Complete Twitch analytics tool using the API client"""
    
    def __init__(self, api_key: str):
        self.client = TwitchAPIClient(api_key)
    
    def get_complete_channel_analysis(self, channel: str) -> Dict[str, Any]:
        """Get comprehensive analysis of a Twitch channel"""
        print(f"📊 Analyzing channel: {channel}")
        print("=" * 50)
        
        analysis = {
            "channel": channel,
            "streamer_info": None,
            "is_live": False,
            "viewer_count": 0,
            "user_id": None,
            "videos": None,
            "panels": None,
            "goals": None,
            "leaderboards": None,
            "chat_info": {},
            "error": None
        }
        
        try:
            # 1. Get basic streamer information
            print("🔍 Getting streamer info...")
            streamer_info = self.client.get_streamer_info(channel)
            analysis["streamer_info"] = streamer_info
            
            if streamer_info and "user" in streamer_info:
                user = streamer_info["user"]
                print(f"✅ Found user: {user.get('displayName', channel)}")
                
                # Check if live
                stream = user.get("stream")
                if stream:
                    analysis["is_live"] = True
                    analysis["viewer_count"] = stream.get("viewersCount", 0)
                    print(f"🔴 LIVE with {analysis['viewer_count']:,} viewers")
                    print(f"📺 Stream title: {stream.get('title', 'N/A')}")
                    
                    game = stream.get("game")
                    if game:
                        print(f"🎮 Playing: {game.get('name', 'N/A')}")
                else:
                    print("⭕ Currently offline")
            
            # 2. Get user ID
            print("\n🆔 Getting user ID...")
            user_id_data = self.client.get_user_id(channel)
            if user_id_data and "user" in user_id_data:
                analysis["user_id"] = user_id_data["user"].get("id")
                print(f"✅ User ID: {analysis['user_id']}")
            
            # 3. Get channel videos
            print("\n📹 Getting recent videos...")
            videos = self.client.get_channel_videos(channel)
            analysis["videos"] = videos
            if videos:
                print("✅ Video data retrieved")
            
            # 4. Get channel panels
            print("\n📋 Getting channel panels...")
            panels = self.client.get_channel_panels(channel)
            analysis["panels"] = panels
            if panels:
                print("✅ Panel data retrieved")
            
            # 5. Get channel goals
            print("\n🎯 Getting channel goals...")
            goals = self.client.get_channel_goals(channel)
            analysis["goals"] = goals
            if goals:
                print("✅ Goals data retrieved")
            
            # 6. Get leaderboards
            print("\n🏆 Getting leaderboards...")
            leaderboards = self.client.get_channel_leaderboards(channel)
            analysis["leaderboards"] = leaderboards
            if leaderboards:
                print("✅ Leaderboard data retrieved")
            
            # 7. Get chat information
            print("\n💬 Getting chat info...")
            
            try:
                chat_restrictions = self.client.get_chat_restrictions(channel)
                analysis["chat_info"]["restrictions"] = chat_restrictions
                print("✅ Chat restrictions retrieved")
            except Exception as e:
                print(f"⚠️  Chat restrictions: {str(e)[:50]}...")
            
            try:
                pinned_chat = self.client.get_pinned_chat(channel)
                analysis["chat_info"]["pinned"] = pinned_chat
                print("✅ Pinned chat retrieved")
            except Exception as e:
                print(f"⚠️  Pinned chat: {str(e)[:50]}...")
            
            # 8. Get channel points and stream tags
            print("\n🎁 Getting additional data...")
            
            try:
                points_context = self.client.get_channel_points_context(channel)
                analysis["chat_info"]["points_context"] = points_context
                print("✅ Channel points context retrieved")
            except Exception as e:
                print(f"⚠️  Channel points: {str(e)[:50]}...")
            
            try:
                stream_tags = self.client.get_stream_tags(channel)
                analysis["chat_info"]["stream_tags"] = stream_tags
                print("✅ Stream tags retrieved")
            except Exception as e:
                print(f"⚠️  Stream tags: {str(e)[:50]}...")
        
        except TwitchAPIError as e:
            analysis["error"] = f"API Error: {str(e)}"
            print(f"❌ API Error: {e}")
        except Exception as e:
            analysis["error"] = f"Unexpected Error: {str(e)}"
            print(f"❌ Unexpected Error: {e}")
        
        return analysis
    
    def compare_channels(self, channels: list) -> Dict[str, Any]:
        """Compare multiple channels"""
        print(f"\n🔍 COMPARING {len(channels)} CHANNELS")
        print("=" * 60)
        
        comparison = {}
        
        for channel in channels:
            try:
                info = self.client.get_streamer_info(channel)
                if info and "user" in info:
                    user = info["user"]
                    stream = user.get("stream")
                    
                    comparison[channel] = {
                        "display_name": user.get("displayName", channel),
                        "is_live": bool(stream),
                        "viewers": stream.get("viewersCount", 0) if stream else 0,
                        "game": stream.get("game", {}).get("name") if stream else "Offline",
                        "title": stream.get("title", "No stream") if stream else "Offline"
                    }
                else:
                    comparison[channel] = {
                        "display_name": channel,
                        "is_live": False,
                        "viewers": 0,
                        "game": "Data unavailable",
                        "title": "Data unavailable"
                    }
            except Exception as e:
                comparison[channel] = {
                    "display_name": channel,
                    "error": str(e)[:50]
                }
        
        # Print comparison table
        print(f"{'Channel':<15} | {'Status':<8} | {'Viewers':<10} | {'Game':<20}")
        print("-" * 60)
        
        for channel, data in comparison.items():
            if "error" in data:
                print(f"{channel:<15} | {'ERROR':<8} | {'-':<10} | {data['error']:<20}")
            else:
                status = "🔴 LIVE" if data["is_live"] else "⭕ OFF"
                viewers = f"{data['viewers']:,}" if data["is_live"] else "-"
                game = data["game"][:18] if len(data["game"]) > 18 else data["game"]
                print(f"{channel:<15} | {status:<8} | {viewers:<10} | {game:<20}")
        
        return comparison
    
    def test_viewer_card(self, channel: str, username: str):
        """Test viewer card functionality"""
        print(f"\n👤 TESTING VIEWER CARD: {username} in {channel}")
        print("=" * 50)
        
        try:
            card = self.client.get_viewer_card(channel, username)
            if card:
                print("✅ Viewer card data retrieved successfully")
                return card
            else:
                print("⚠️  No viewer card data available")
                return None
        except Exception as e:
            print(f"❌ Error getting viewer card: {e}")
            return None


def main():
    """Main function"""
    print("🎮 TWITCH API CLIENT - COMPLETE EXAMPLE")
    print("=" * 60)
    
    # Get API key from environment
    api_key = os.getenv("RAPIDAPI_KEY")
    
    if not api_key:
        print("❌ Error: Please set RAPIDAPI_KEY environment variable")
        print("Example: export RAPIDAPI_KEY='your_actual_api_key_here'")
        print("\n🔗 Get your API key from: https://rapidapi.com/hub")
        return
    
    # Initialize analytics tool
    try:
        analytics = TwitchAnalytics(api_key)
        print("✅ Twitch Analytics tool initialized!")
    except Exception as e:
        print(f"❌ Failed to initialize: {e}")
        return
    
    # Test channels
    test_channels = ["xQc", "ninja", "pokimane"]
    
    # 1. Complete analysis of first channel
    print(f"\n{'🔍 COMPLETE ANALYSIS':^60}")
    analysis = analytics.get_complete_channel_analysis(test_channels[0])
    
    # 2. Compare multiple channels
    print(f"\n{'📊 CHANNEL COMPARISON':^60}")
    comparison = analytics.compare_channels(test_channels)
    
    # 3. Test viewer card
    print(f"\n{'👤 VIEWER CARD TEST':^60}")
    analytics.test_viewer_card(test_channels[0], "testuser")
    
    print(f"\n✨ Complete example finished!")
    print(f"💡 Check the returned data structures for integration into your apps")


if __name__ == "__main__":
    main() 