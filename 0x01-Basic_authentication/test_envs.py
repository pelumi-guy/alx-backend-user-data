from os import getenv

host = getenv("API_HOST", "0.0.0.0")
port = getenv("API_PORT", "5000")

print(f'host: {host} | port: {port}')