#!/usr/bin/env python3
"""
Environment Validation Script

This script validates that your development environment is properly configured.
It tests both package installation and API key configuration.

TESTING PHILOSOPHY:
This is an "environment validator" not a traditional unit test. It dynamically
reads from your actual config files (requirements.txt, config.py) to
ensure your environment matches your current setup. This approach:

✅ Tests what you actually have configured
✅ Automatically adapts when you add new packages/keys  
✅ Catches real deployment issues (Docker build failures, etc.)
✅ Provides a "health check" for your working environment

The trade-off is that it's more of a "status check" than a pure test, but
that's exactly what we need for environment validation.
"""

import sys
import os

# Add src root to path (we're in /src inside the container)
sys.path.append('/src')


def get_packages_from_requirements():
    """Get package list from requirements.txt with validation"""
    # Core packages that should always be present (meta-validation)
    CORE_PACKAGES = ['langchain', 'langchain-core', 'langchain-openai', 'openai', 'pandas']
    
    try:
        # requirements.txt is copied to container root during build
        req_path = '/requirements.txt'
        with open(req_path, 'r') as f:
            packages = []
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    # Extract package name (before == or >= etc)
                    pkg_name = line.split('==')[0].split('>=')[0].split('<=')[0].split('~=')[0].strip()
                    # Skip some packages that are hard to test or not main ones
                    if pkg_name not in ['pip', 'setuptools', 'wheel']:
                        packages.append(pkg_name)
            
            # Meta-validation: Check that core packages are in requirements.txt
            missing_core = [pkg for pkg in CORE_PACKAGES if pkg not in packages]
            if missing_core:
                print(f"⚠️  requirements.txt missing expected core packages: {missing_core}")
                print("   This might indicate requirements.txt is incomplete or corrupted")
                # Still add them for testing
                packages.extend(missing_core)
            
            return packages[:12]  # Test first 12 packages to keep output manageable
            
    except FileNotFoundError:
        print("⚠️  requirements.txt not found, testing core packages only")
        return CORE_PACKAGES


def test_packages():
    """Test that key packages are installed"""
    import importlib.metadata
    
    print("🐍 Python Environment Check")
    print(f"✅ Python: {sys.version.split()[0]}")
    
    packages = get_packages_from_requirements()
    
    print(f"\n📦 Package Versions (from requirements.txt):")
    missing = []
    for pkg in packages:
        try:
            # Use importlib.metadata to check by actual pip package name
            version = importlib.metadata.version(pkg)
            print(f"  ✅ {pkg}: {version}")
        except importlib.metadata.PackageNotFoundError:
            print(f"  ❌ {pkg}: Missing")
            missing.append(pkg)
    
    if missing:
        print(f"\n⚠️  Missing packages: {', '.join(missing)}")
    else:
        print("\n🎉 All tested packages installed!")


def get_api_keys_from_config():
    """Extract API key names from config.py with validation"""
    # Core API keys we expect to see (meta-validation)
    EXPECTED_KEYS = ['OPENAI_API_KEY', 'ANTHROPIC_API_KEY', 'GOOGLE_API_KEY']
    
    try:
        # config.py is now in src/ directory
        config_path = '/src/config.py'
        with open(config_path, 'r') as f:
            keys = []
            for line in f:
                line = line.strip()
                if 'os.environ[' in line and ('API_KEY' in line or 'API_TOKEN' in line):
                    # Extract key name between quotes
                    start = line.find("'") + 1
                    end = line.find("'", start)
                    if start > 0 and end > start:
                        key_name = line[start:end]
                        if (key_name.endswith('_API_KEY') or 
                            key_name.endswith('_API_TOKEN') or 
                            key_name.endswith('_TRACING_V2') or
                            key_name.endswith('_PROJECT')):
                            keys.append(key_name)
            
            # Meta-validation: Check that expected keys are in config
            missing_expected = [key for key in EXPECTED_KEYS if key not in keys]
            if missing_expected:
                print(f"⚠️  config.py missing expected keys: {missing_expected}")
                print("   This might indicate config.py is incomplete")
                # Still add them for testing
                keys.extend(missing_expected)
            
            return keys[:10]  # Keep to reasonable number for cleaner output
            
    except FileNotFoundError:
        print("⚠️  config.py not found, testing common keys only")
        return EXPECTED_KEYS


def test_config():
    """Test config.py setup"""
    print("\n🔑 Configuration Check")
    print("=" * 50)
    
    try:
        # Clear any existing environment variables to start fresh
        api_keys_to_clear = [
            'OPENAI_API_KEY', 'ANTHROPIC_API_KEY', 'GOOGLE_API_KEY', 
            'LANGSMITH_API_KEY', 'LANGCHAIN_API_KEY', 'HUGGINGFACE_API_TOKEN',
            'PINECONE_API_KEY', 'WEAVIATE_API_KEY', 'AZURE_OPENAI_API_KEY',
            'COHERE_API_KEY', 'SERPAPI_API_KEY'
        ]
        for key in api_keys_to_clear:
            if key in os.environ:
                del os.environ[key]
        
        from config import set_environment
        print("✅ config.py found")
        
        # Set environment variables (no more print statement to suppress)
        set_environment()
        
        # Get API keys from config
        keys = get_api_keys_from_config()
        configured = 0
        
        for key in keys:
            value = os.environ.get(key, '')
            if value and not value.startswith('your-'):
                configured += 1
                print(f"  ✅ {key}: configured")
            else:
                print(f"  💤 {key}: not configured")
        
        print(f"\n📊 {configured}/{len(keys)} API keys ready")
        if configured == 0:
            print("🎯 Clean start! Add API keys when you need them.")
        
    except ImportError:
        print("❌ config.py not found")
        print("💡 Run: cp config_template.py config.py")


def main():
    """Run all tests"""
    print("🚀 Gen AI Experiments - System Test")
    print("=" * 60)
    
    test_packages()
    test_config()
    
    print("\n" + "=" * 60)
    print("📋 Next Steps:")
    print("1. If packages missing → check Docker build")
    print("2. Create config.py from template")
    print("3. Add API keys as you progress")


if __name__ == "__main__":
    main()
