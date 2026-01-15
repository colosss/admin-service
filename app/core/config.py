import os 

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    kafka_url: str= os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")

settings = Settings()