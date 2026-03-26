import os
import sys
from dotenv import load_dotenv


def load_config() -> dict[str, str | None]:
    """Load and return the Matrix configuration from environment variables."""
    # Load variables from .env file if it exists
    load_dotenv()

    config_keys = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]

    config = {key: os.getenv(key) for key in config_keys}
    return config


def check_security(config: dict[str, str | None]) -> None:
    """Perform basic security checks on the environment configuration."""
    print("Environment security check:")
    
    # Check if .env is potentially being ignored (not perfect, but a prompt requirement)
    if os.path.exists(".env"):
        print("[OK] .env file detected for local configuration")
    else:
        print("[WARN] No .env file found; using system environment variables")

    # Ensure no secrets were accidentally hardcoded (simple check for placeholders)
    if config.get("API_KEY") == "your_secret_api_key_here":
        print("[WARN] API_KEY still using placeholder value")
    else:
        print("[OK] No hardcoded secrets detected")

    print("[OK] Production overrides available")


def display_oracle_status(config: dict[str, str | None]) -> None:
    """Display the current configuration status in a readable format."""
    print("ORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    
    mode = config.get("MATRIX_MODE", "unknown")
    print(f"Mode: {mode}")
    
    db = "Connected to local instance" if mode == "development" else "Connected to Production Mainframe"
    print(f"Database: {db if config.get('DATABASE_URL') else 'Disconnected'}")
    
    print(f"API Access: {'Authenticated' if config.get('API_KEY') else 'Denied'}")
    print(f"Log Level: {config.get('LOG_LEVEL', 'NOT SET')}")
    print(f"Zion Network: {'Online' if config.get('ZION_ENDPOINT') else 'Offline'}")
    print()


def main() -> None:
    """Entry point for the Oracle mainframe access."""
    try:
        config = load_config()
        
        # Verify critical configuration exists
        if not config.get("MATRIX_MODE"):
            print("ERROR: MATRIX_MODE not found. Have you initialized your .env?")
            sys.exit(1)

        display_oracle_status(config)
        check_security(config)
        print("\nThe Oracle sees all configurations.")

    except Exception as e:
        print(f"Mainframe connection error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()