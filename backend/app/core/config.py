import os
import json
from dotenv import load_dotenv

load_dotenv()

# Absolute path to the ABI file
ABI_PATH = r"D:\AntiCorruptionDapp\blockchain\artifacts\contracts\FundRelease.sol\FundRelease.json"

if not os.path.exists(ABI_PATH):
    raise FileNotFoundError(f"ABI file not found at {ABI_PATH}")

class Settings:
    WEB3_PROVIDER = os.getenv("WEB3_PROVIDER", "http://127.0.0.1:8545")
    CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
    PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Only for testing; don't use in production

    # Load ABI from the JSON file
    with open(ABI_PATH, "r") as f:
        CONTRACT_ABI = json.load(f)["abi"]

settings = Settings()
