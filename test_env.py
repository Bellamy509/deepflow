#!/usr/bin/env python3
"""
Test script for environment variables configuration
"""

import os
import requests
import json

def test_openai_key():
    """Test OpenAI API key"""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        return False, "OPENAI_API_KEY not set"
    
    if not api_key.startswith('sk-'):
        return False, "OPENAI_API_KEY format invalid (should start with 'sk-')"
    
    # Test simple avec OpenAI API
    try:
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'model': 'gpt-3.5-turbo',
            'messages': [{'role': 'user', 'content': 'Hello'}],
            'max_tokens': 10
        }
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers=headers,
            json=data,
            timeout=10
        )
        
        if response.status_code == 200:
            return True, "OPENAI_API_KEY is valid"
        elif response.status_code == 401:
            return False, "OPENAI_API_KEY is invalid"
        else:
            return False, f"OpenAI API error: {response.status_code}"
            
    except Exception as e:
        return False, f"OpenAI API test failed: {str(e)}"

def test_tavily_key():
    """Test Tavily API key"""
    api_key = os.getenv('TAVILY_API_KEY')
    if not api_key:
        return False, "TAVILY_API_KEY not set"
    
    if not api_key.startswith('tvly-'):
        return False, "TAVILY_API_KEY format invalid (should start with 'tvly-')"
    
    # Test simple avec Tavily API
    try:
        headers = {
            'X-API-Key': api_key,
            'Content-Type': 'application/json'
        }
        data = {
            'query': 'test',
            'search_depth': 'basic',
            'max_results': 1
        }
        response = requests.post(
            'https://api.tavily.com/search',
            headers=headers,
            json=data,
            timeout=10
        )
        
        if response.status_code == 200:
            return True, "TAVILY_API_KEY is valid"
        elif response.status_code == 401:
            return False, "TAVILY_API_KEY is invalid"
        else:
            return False, f"Tavily API error: {response.status_code}"
            
    except Exception as e:
        return False, f"Tavily API test failed: {str(e)}"

def test_railway_app(railway_url):
    """Test Railway app endpoints"""
    if not railway_url:
        return False, "Railway URL not provided"
    
    try:
        # Test health endpoint
        response = requests.get(f"{railway_url}/health", timeout=10)
        if response.status_code == 200:
            return True, f"Railway app is healthy: {response.json()}"
        else:
            return False, f"Railway app health check failed: {response.status_code}"
            
    except Exception as e:
        return False, f"Railway app test failed: {str(e)}"

def main():
    """Main test function"""
    print("🔍 Testing Environment Configuration")
    print("=" * 50)
    
    # Test local environment variables
    print("\n📋 Local Environment Variables:")
    for key in ['OPENAI_API_KEY', 'TAVILY_API_KEY', 'ALLOWED_ORIGINS', 'SEARCH_API']:
        value = os.getenv(key, 'NOT SET')
        if key.endswith('_KEY') and value != 'NOT SET':
            value = f"{value[:8]}..." if len(value) > 8 else "***"
        print(f"  {key}: {value}")
    
    # Test OpenAI API key
    print("\n🤖 Testing OpenAI API Key:")
    success, message = test_openai_key()
    status = "✅" if success else "❌"
    print(f"  {status} {message}")
    
    # Test Tavily API key
    print("\n🔍 Testing Tavily API Key:")
    success, message = test_tavily_key()
    status = "✅" if success else "❌"
    print(f"  {status} {message}")
    
    # Test Railway app if URL provided
    railway_url = input("\n🚂 Enter your Railway app URL (or press Enter to skip): ").strip()
    if railway_url:
        print(f"\n🌐 Testing Railway App at {railway_url}:")
        success, message = test_railway_app(railway_url)
        status = "✅" if success else "❌"
        print(f"  {status} {message}")
    
    print("\n" + "=" * 50)
    print("📊 Configuration Test Complete")
    print("=" * 50)

if __name__ == "__main__":
    main()
