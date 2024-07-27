import os

class Config:
    DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')
    NATS_SERVER = os.getenv('NATS_SERVER', 'nats://localhost:4222')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')

    @classmethod
    def validate(cls):
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
