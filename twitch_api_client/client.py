"""
Twitch API Client for RapidAPI
A Python client library for the Twitch API available on RapidAPI
"""

import requests
from typing import Dict, Optional, Any
import json


class TwitchAPIError(Exception):
    """Custom exception for Twitch API errors"""
    pass


class TwitchAPIClient:
    """
    A Python client for the Twitch API available on RapidAPI.
    
    This client provides easy access to various Twitch data including:
    - Channel information
    - Stream data
    - Chat information
    - Channel points and goals
    - And much more!
    """
    
    BASE_URL = "https://twitch-api8.p.rapidapi.com"
    
    def __init__(self, rapidapi_key: str):
        """
        Initialize the Twitch API Client
        
        Args:
            rapidapi_key (str): Your RapidAPI key for the Twitch API
        """
        if not rapidapi_key:
            raise ValueError("RapidAPI key is required")
            
        self.rapidapi_key = rapidapi_key
        self.headers = {
            "X-RapidAPI-Key": self.rapidapi_key,
            "X-RapidAPI-Host": "twitch-api8.p.rapidapi.com"
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def _make_request(self, endpoint: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Make a request to the API
        
        Args:
            endpoint (str): API endpoint
            params (Dict[str, Any]): Request parameters
            
        Returns:
            Dict[str, Any]: API response data
            
        Raises:
            TwitchAPIError: If the API request fails
        """
        url = f"{self.BASE_URL}/{endpoint}"
        
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise TwitchAPIError(f"API request failed: {str(e)}")
        except json.JSONDecodeError:
            raise TwitchAPIError("Failed to decode API response")
    
    def get_channel_panels(self, channel: str) -> Dict[str, Any]:
        """
        Get channel panels information
        
        Args:
            channel (str): Twitch channel name (e.g., 'xQc')
            
        Returns:
            Dict[str, Any]: Channel panels data
        """
        return self._make_request("get_channel_panels", {"channel": channel})
    
    def get_viewer_card(self, channel: str, username: str) -> Dict[str, Any]:
        """
        Get viewer card information for a specific user in a channel
        
        Args:
            channel (str): Twitch channel name
            username (str): Username to get viewer card for
            
        Returns:
            Dict[str, Any]: Viewer card data
        """
        return self._make_request("get_viewer_card", {
            "channel": channel,
            "username": username
        })
    
    def get_streamer_info(self, channel: str) -> Dict[str, Any]:
        """
        Get comprehensive streamer information including live status
        
        Args:
            channel (str): Twitch channel name
            
        Returns:
            Dict[str, Any]: Streamer information and live status
        """
        return self._make_request("get_streamer_info", {"channel": channel})
    
    def get_channel_videos(self, channel: str) -> Dict[str, Any]:
        """
        Get recent videos from a channel
        
        Args:
            channel (str): Twitch channel name
            
        Returns:
            Dict[str, Any]: Channel videos data
        """
        return self._make_request("get_channel_videos", {"channel": channel})
    
    def get_stream_viewers(self, channel: str) -> Dict[str, Any]:
        """
        Get current stream viewer count
        
        Args:
            channel (str): Twitch channel name
            
        Returns:
            Dict[str, Any]: Stream viewer data
        """
        return self._make_request("get_stream_viewers", {"channel": channel})
    
    def get_user_id(self, channel: str) -> Dict[str, Any]:
        """
        Get user ID information for a channel
        
        Args:
            channel (str): Twitch channel name
            
        Returns:
            Dict[str, Any]: User ID data
        """
        return self._make_request("get_user_id", {"channel": channel})
    
    def get_channel_points_context(self, channel: str) -> Dict[str, Any]:
        """
        Get channel points context and information
        
        Args:
            channel (str): Twitch channel name
            
        Returns:
            Dict[str, Any]: Channel points context data
        """
        return self._make_request("get_channel_points_context", {"channel": channel})
    
    def get_chat_restrictions(self, channel: str) -> Dict[str, Any]:
        """
        Get chat restrictions for a channel
        
        Args:
            channel (str): Twitch channel name
            
        Returns:
            Dict[str, Any]: Chat restrictions data
        """
        return self._make_request("get_chat_restrictions", {"channel": channel})
    
    def get_pinned_chat(self, channel: str) -> Dict[str, Any]:
        """
        Get pinned chat messages for a channel
        
        Args:
            channel (str): Twitch channel name
            
        Returns:
            Dict[str, Any]: Pinned chat data
        """
        return self._make_request("get_pinned_chat", {"channel": channel})
    
    def get_channel_goals(self, channel: str) -> Dict[str, Any]:
        """
        Get active channel goals
        
        Args:
            channel (str): Twitch channel name
            
        Returns:
            Dict[str, Any]: Channel goals data
        """
        return self._make_request("get_channel_goals", {"channel": channel})
    
    def get_channel_leaderboards(self, channel: str) -> Dict[str, Any]:
        """
        Get channel leaderboards information
        
        Args:
            channel (str): Twitch channel name
            
        Returns:
            Dict[str, Any]: Channel leaderboards data
        """
        return self._make_request("get_channel_leaderboards", {"channel": channel})
    
    def get_stream_tags(self, channel: str) -> Dict[str, Any]:
        """
        Get current stream tags
        
        Args:
            channel (str): Twitch channel name
            
        Returns:
            Dict[str, Any]: Stream tags data
        """
        return self._make_request("get_stream_tags", {"channel": channel}) 