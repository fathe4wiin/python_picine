from abc import ABC, abstractmethod
from typing import Any, List, Union

class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Must be implemented by subclasses to check data type."""
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        """Must be implemented by subclasses to process data."""
        pass

    def format_output(self, result: str) -> str:
        """Default implementation that can be overridden or used via super()."""
        return f"Processed Result: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, (int, float))

    def process(self, data: Union[int, float]) -> str:
        return str(data ** 2)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: str) -> str:
        return data.upper()

    def format_output(self, result: str) -> str:
        standard = super().format_output(result)
        return f"[TEXT] {standard}"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and "ERROR" in data

    def process(self, data: str) -> str:
        return data.split(":", 1)[-1].strip()


def run_pipeline():
    processors: List[DataProcessor] = [NumericProcessor(), TextProcessor(), LogProcessor()]
    test_data = [25, "hello world", "ERROR: System Failure", 3.14, "Invalid Data"]

    for data in test_data:
        for proc in processors:
            try:
                if proc.validate(data):
                    result = proc.process(data)
                    print(proc.format_output(result))
            except Exception as e:
                print(f"Error processing {data}: {e}")

if __name__ == "__main__":
    run_pipeline()