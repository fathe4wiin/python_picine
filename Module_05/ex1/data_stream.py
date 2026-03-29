from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.corrupted_items = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None) -> List[Any]:
        return [item for item in data_batch if item is not None]

    @abstractmethod
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "corrupted_items": self.corrupted_items
        }


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        readings = [float(d)
                    for d in data_batch if isinstance(d, (int, float))]
        avg = sum(readings) / len(readings) if readings else 0.0
        return f"""Sensor analysis: {
            len(readings)} readings processed, avg temp: {avg}°C"""

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None) -> List[Any]:
        numeric_only = [d for d in data_batch if isinstance(d, (int, float))]
        if criteria == "high_priority":
            return [d for d in numeric_only if d > 30]
        return numeric_only

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Environmental Data"
        return stats


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        net_flow = 0.0
        ops = 0
        for item in data_batch:
            if isinstance(item, str) and ":" in item:
                try:
                    parts = item.split(":")
                    action, val = parts[0].strip().lower(), float(parts[1])
                    net_flow += val if action == "buy" else -val
                    ops += 1
                except ValueError:
                    self.corrupted_items += 1
            else:
                self.corrupted_items += 1

        flow_prefix = "+" if net_flow > 0 else ""
        return f"""Transaction analysis: {
            ops} operations, net flow: {flow_prefix}{net_flow} units"""

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Financial Data"
        return stats


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        errors = 0
        for item in data_batch:
            if isinstance(item, str) and item.lower() == "error":
                errors += 1
        return f"""Event analysis: {
            len(data_batch)} events, {errors} error detected"""

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "System Events"
        return stats


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def run_all(self, batch_map: Dict[str, List[Any]]) -> None:
        print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
        for stream in self.streams:
            print(f"Initializing {stream.__class__.__name__}...")
            stats = stream.get_stats()
            print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")

            raw_data = batch_map.get(stream.stream_id, [])
            print(f"Processing batch: {raw_data}")

            result = stream.process_batch(raw_data)
            print(f"{result}")
            print("-" * 30)

    def process_mixed_interface(
            self, batch_map: Dict[str, List[Any]],
            criteria: Optional[str] = None
            ) -> None:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        if criteria:
            print(f"Stream filtering active: {criteria}")

        for stream in self.streams:
            raw_data = batch_map.get(stream.stream_id, [])
            filtered = stream.filter_data(raw_data, criteria)
            result = stream.process_batch(filtered)
            print(f"- {result}")

        print("All streams processed successfully.\nNexus throughput optimal.")


if __name__ == "__main__":
    processor = StreamProcessor()

    s_stream = SensorStream("SENSOR_001")
    t_stream = TransactionStream("TRANS_001")
    e_stream = EventStream("EVENT_001")

    processor.add_stream(s_stream)
    processor.add_stream(t_stream)
    processor.add_stream(e_stream)

    data_payload = {
        "SENSOR_001": [22.5, 35.0, 21.2],
        "TRANS_001": ["buy:100", "sell:150", "buy:75"],
        "EVENT_001": ["login", "error", "logout"]
    }

    processor.run_all(data_payload)
    processor.process_mixed_interface(data_payload, criteria="high_priority")
