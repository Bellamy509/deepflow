#!/usr/bin/env python3
"""
Robust server startup script for Railway deployment
Handles missing environment variables gracefully
"""

import os
import sys
import logging
from pathlib import Path

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def check_environment():
    """Check if required environment variables are set"""
    required_vars = [
        'OPENAI_API_KEY',
        'TAVILY_API_KEY'
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        logger.warning(f"Missing environment variables: {missing_vars}")
        logger.warning("Application will start but some features may not work")
        return False
    return True

def main():
    """Main startup function"""
    try:
        logger.info("Starting DeerFlow server...")
        
        # Check environment
        env_ok = check_environment()
        
        # Set default environment variables if not present
        if not os.getenv('ALLOWED_ORIGINS'):
            os.environ['ALLOWED_ORIGINS'] = 'http://localhost:3000,https://your-frontend-domain.com'
            logger.info("Set default ALLOWED_ORIGINS")
        
        if not os.getenv('SEARCH_API'):
            os.environ['SEARCH_API'] = 'tavily'
            logger.info("Set default SEARCH_API")
        
        # Import and start the server
        from src.server.app import app
        import uvicorn
        
        port = int(os.getenv('PORT', 8000))
        host = os.getenv('HOST', '0.0.0.0')
        
        logger.info(f"Starting server on {host}:{port}")
        logger.info(f"Environment check: {'OK' if env_ok else 'WARNING'}")
        
        uvicorn.run(
            app,
            host=host,
            port=port,
            log_level="info"
        )
        
    except Exception as e:
        logger.error(f"Failed to start server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
