import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    WEB3_PROVIDER = os.getenv("WEB3_PROVIDER", "http://127.0.0.1:8545")
    CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
    PRIVATE_KEY = os.getenv("PRIVATE_KEY")   # Hackathon only, don’t do this in prod

settings = Settings()
