import dotenv

def load_env():
    """
    Load environment variables from a .env file.
    """
    dotenv.load_dotenv()
    print("Environment variables loaded from .env file.")


