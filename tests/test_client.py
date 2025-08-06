"""
Unit tests for the Twitch API Client
"""

import unittest
from unittest.mock import Mock, patch
import json

from twitch_api_client import TwitchAPIClient, TwitchAPIError


class TestTwitchAPIClient(unittest.TestCase):
    """Test cases for TwitchAPIClient"""
    
    def setUp(self):
        """Set up test client"""
        self.api_key = "test_api_key"
        self.client = TwitchAPIClient(self.api_key)
    
    def test_init_with_valid_key(self):
        """Test client initialization with valid API key"""
        client = TwitchAPIClient("valid_key")
        self.assertEqual(client.rapidapi_key, "valid_key")
        self.assertEqual(client.headers["X-RapidAPI-Key"], "valid_key")
        self.assertEqual(client.headers["X-RapidAPI-Host"], "twitch-api8.p.rapidapi.com")
    
    def test_init_with_empty_key(self):
        """Test client initialization with empty API key"""
        with self.assertRaises(ValueError):
            TwitchAPIClient("")
    
    def test_init_with_none_key(self):
        """Test client initialization with None API key"""
        with self.assertRaises(ValueError):
            TwitchAPIClient(None)
    
    @patch('twitch_api_client.client.requests.Session.get')
    def test_make_request_success(self, mock_get):
        """Test successful API request"""
        # Mock successful response
        mock_response = Mock()
        mock_response.json.return_value = {"success": True, "data": "test"}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        result = self.client._make_request("test_endpoint", {"param": "value"})
        
        self.assertEqual(result, {"success": True, "data": "test"})
        mock_get.assert_called_once()
    
    @patch('twitch_api_client.client.requests.Session.get')
    def test_make_request_http_error(self, mock_get):
        """Test API request with HTTP error"""
        # Mock HTTP error
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = Exception("HTTP Error")
        mock_get.return_value = mock_response
        
        with self.assertRaises(TwitchAPIError):
            self.client._make_request("test_endpoint", {"param": "value"})
    
    @patch('twitch_api_client.client.requests.Session.get')
    def test_make_request_json_decode_error(self, mock_get):
        """Test API request with JSON decode error"""
        # Mock JSON decode error
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.side_effect = json.JSONDecodeError("Invalid JSON", "", 0)
        mock_get.return_value = mock_response
        
        with self.assertRaises(TwitchAPIError):
            self.client._make_request("test_endpoint", {"param": "value"})
    
    @patch('twitch_api_client.client.TwitchAPIClient._make_request')
    def test_get_channel_panels(self, mock_request):
        """Test get_channel_panels method"""
        mock_request.return_value = {"panels": []}
        
        result = self.client.get_channel_panels("test_channel")
        
        mock_request.assert_called_once_with("get_channel_panels", {"channel": "test_channel"})
        self.assertEqual(result, {"panels": []})
    
    @patch('twitch_api_client.client.TwitchAPIClient._make_request')
    def test_get_viewer_card(self, mock_request):
        """Test get_viewer_card method"""
        mock_request.return_value = {"viewer": {}}
        
        result = self.client.get_viewer_card("test_channel", "test_user")
        
        mock_request.assert_called_once_with("get_viewer_card", {
            "channel": "test_channel",
            "username": "test_user"
        })
        self.assertEqual(result, {"viewer": {}})
    
    @patch('twitch_api_client.client.TwitchAPIClient._make_request')
    def test_get_streamer_info(self, mock_request):
        """Test get_streamer_info method"""
        mock_request.return_value = {"user": {"displayName": "TestStreamer"}}
        
        result = self.client.get_streamer_info("test_channel")
        
        mock_request.assert_called_once_with("get_streamer_info", {"channel": "test_channel"})
        self.assertEqual(result, {"user": {"displayName": "TestStreamer"}})
    
    @patch('twitch_api_client.client.TwitchAPIClient._make_request')
    def test_get_channel_videos(self, mock_request):
        """Test get_channel_videos method"""
        mock_request.return_value = {"videos": []}
        
        result = self.client.get_channel_videos("test_channel")
        
        mock_request.assert_called_once_with("get_channel_videos", {"channel": "test_channel"})
        self.assertEqual(result, {"videos": []})
    
    @patch('twitch_api_client.client.TwitchAPIClient._make_request')
    def test_get_stream_viewers(self, mock_request):
        """Test get_stream_viewers method"""
        mock_request.return_value = {"viewerCount": 1234}
        
        result = self.client.get_stream_viewers("test_channel")
        
        mock_request.assert_called_once_with("get_stream_viewers", {"channel": "test_channel"})
        self.assertEqual(result, {"viewerCount": 1234})
    
    @patch('twitch_api_client.client.TwitchAPIClient._make_request')
    def test_get_user_id(self, mock_request):
        """Test get_user_id method"""
        mock_request.return_value = {"user": {"id": "123456"}}
        
        result = self.client.get_user_id("test_channel")
        
        mock_request.assert_called_once_with("get_user_id", {"channel": "test_channel"})
        self.assertEqual(result, {"user": {"id": "123456"}})


class TestTwitchAPIError(unittest.TestCase):
    """Test cases for TwitchAPIError"""
    
    def test_twitch_api_error_creation(self):
        """Test TwitchAPIError can be created and raised"""
        with self.assertRaises(TwitchAPIError) as context:
            raise TwitchAPIError("Test error message")
        
        self.assertEqual(str(context.exception), "Test error message")
    
    def test_twitch_api_error_inheritance(self):
        """Test TwitchAPIError inherits from Exception"""
        error = TwitchAPIError("Test")
        self.assertIsInstance(error, Exception)


if __name__ == "__main__":
    unittest.main() 