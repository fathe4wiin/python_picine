from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union


class DataProcessor(ABC):
    """Base abstract class defining the common processing interface."""

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Marked as abstract to ensure subclass implementation."""
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        """Marked as abstract to ensure subclass implementation."""
        pass

    def format_output(self, result: str) -> str:
        """Default implementation that can be overridden."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        """Checks if data is a list of numeric values."""
        if not isinstance(data, list):
            return False
        return all(isinstance(x, (int, float)) for x in data)

    def process(self, data: List[Union[int, float]]) -> str:
        """Calculates sum and average for a batch of numbers."""
        count = len(data)
        total = sum(data)
        avg = total / count if count > 0 else 0.0
        return f"Processed {count} numeric values, sum={total}, avg={avg}"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        """Checks if data is a string."""
        return isinstance(data, str)

    def process(self, data: str) -> str:
        """Extracts character and word counts from text."""
        char_count = len(data)
        word_count = len(data.split())
        return f"Processed text: {char_count} characters, {word_count} words"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        """Validates if the string is a recognized log entry."""
        return (isinstance(data, str) and
                any(lvl in data for lvl in ["ERROR", "INFO"]))

    def process(self, data: str) -> str:
        """Identifies log levels and extracts the message."""
        parts = data.split(":", 1)
        level = parts[0].strip()
        msg = parts[1].strip() if len(parts) > 1 else ""

        tag = "[ALERT]" if level == "ERROR" else "[INFO]"
        return f"{tag} {level} level detected: {msg}"


def run_pipeline() -> None:
    """Diagnostic program to verify polymorphic constructs."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    test_data: List[Dict[str, Any]] = [
        {"data": [1, 2, 3, 4, 5], "name": "Numeric Processor"},
        {"data": "Hello Nexus World", "name": "Text Processor"},
        {"data": "ERROR: Connection timeout", "name": "Log Processor"}
    ]

    for item in test_data:
        data = item["data"]
        name = item["name"]
        print(f"Initializing {name}...")

        for proc in processors:
            if proc.validate(data):
                print(f"Processing data: {data}")
                print(f"Validation: {name.split()[0]} data verified")
                result = proc.process(data)
                print(proc.format_output(result))

    print("=== Polymorphic Processing Demo ===")
    demo_batch: List[Any] = [[1, 2, 3], "Hello Nexus", "INFO: System ready"]

    for i, data in enumerate(demo_batch, 1):
        for proc in processors:
            if proc.validate(data):
                res = proc.process(data)
                print(f"Result {i}: {res}")

    print("Foundation systems online.")
    print("Nexus ready for advanced streams.")


if __name__ == "__main__":
    run_pipeline()
