#!/usr/bin/env python3
"""
Diagnostic script for Railway deployment
Checks if the application is running correctly
"""

import requests
import sys
import time

def check_endpoint(base_url, endpoint, expected_status=200):
    """Check if an endpoint is responding"""
    try:
        url = f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        print(f"Testing: {url}")
        
        response = requests.get(url, timeout=10)
        print(f"Status: {response.status_code}")
        
        if response.status_code == expected_status:
            print(f"✅ {endpoint} - OK")
            if response.headers.get('content-type', '').startswith('application/json'):
                try:
                    data = response.json()
                    print(f"Response: {data}")
                except:
                    print(f"Response: {response.text[:200]}...")
            else:
                print(f"Response: {response.text[:200]}...")
        else:
            print(f"❌ {endpoint} - Expected {expected_status}, got {response.status_code}")
            print(f"Response: {response.text}")
        
        return response.status_code == expected_status
    except requests.exceptions.RequestException as e:
        print(f"❌ {endpoint} - Error: {e}")
        return False

def main():
    """Main diagnostic function"""
    if len(sys.argv) < 2:
        print("Usage: python diagnose_railway.py <railway_url>")
        print("Example: python diagnose_railway.py https://your-app.railway.app")
        sys.exit(1)
    
    base_url = sys.argv[1]
    print(f"🔍 Diagnosing Railway deployment at: {base_url}")
    print("=" * 50)
    
    # Test endpoints
    endpoints = [
        ("", "Root endpoint"),
        ("health", "Health check"),
        ("test", "Test endpoint"),
        ("docs", "API documentation"),
        ("api/chat/stream", "Chat endpoint (should return 405 for GET)"),
    ]
    
    results = []
    for endpoint, description in endpoints:
        print(f"\n📋 Testing {description}...")
        expected_status = 405 if endpoint == "api/chat/stream" else 200
        success = check_endpoint(base_url, endpoint, expected_status)
        results.append((endpoint, success))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 DIAGNOSTIC SUMMARY")
    print("=" * 50)
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for endpoint, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {endpoint}")
    
    print(f"\nOverall: {passed}/{total} endpoints working")
    
    if passed == total:
        print("🎉 All endpoints are working correctly!")
    elif passed > 0:
        print("⚠️  Some endpoints are working, but there are issues")
    else:
        print("🚨 No endpoints are responding - check Railway deployment")

if __name__ == "__main__":
    main()
