"""
Error handling utilities for Gen AI experiments
"""

class ConfigurationError(Exception):
    """Raised when there's an issue with API key configuration"""
    pass

class ModelError(Exception):
    """Raised when there's an issue with AI model interaction"""
    pass

class ValidationError(Exception):
    """Raised when input validation fails"""
    pass

def handle_api_error(func):
    """Decorator to handle common API errors gracefully"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"❌ API Error in {func.__name__}: {str(e)}")
            raise
    return wrapper

def validate_api_key(key_name):
    """Check if an API key is properly configured"""
    import os
    key_value = os.environ.get(key_name, '')
    if not key_value or key_value.startswith('your-'):
        raise ConfigurationError(f"API key {key_name} not configured")
    return True
