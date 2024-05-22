import os

# Remove (unset) the environment variable
if 'openai.api_key' in os.environ:
    del os.environ['openai.api_key']

# Check if the environment variable has been removed
print(f"After deletion: openai.api_key = {os.environ.get('openai.api_key')}")