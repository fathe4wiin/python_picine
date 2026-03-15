from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union

class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.corrupted_items = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Abstract: Subclasses must define specific summary string output."""
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        """Default: Returns non-None items. Subclasses override for specific domain logic."""
        return [item for item in data_batch if item is not None]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Default: Returns core stream metadata to be augmented by subclasses."""
        return {
            "stream_id": self.stream_id,
            "corrupted_items": self.corrupted_items
        }

class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        readings = [float(d) for d in data_batch if isinstance(d, (int, float))]
        avg = sum(readings) / len(readings) if readings else 0
        return f"Sensor analysis: {len(readings)} readings processed, avg temp: {avg}°C"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        numeric_only = [d for d in data_batch if isinstance(d, (int, float))]
        if criteria == "high_priority":
            return [d for d in numeric_only if d > 30]
        return numeric_only

class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        net_flow = 0
        ops = 0
        for item in data_batch:
            try:
                parts = str(item).split(":")
                type, val = parts[0], float(parts[1])
                net_flow += val if type == "buy" else -val
                ops += 1
            except (ValueError, IndexError):
                self.corrupted_items += 1
        
        flow_str = f"+{net_flow}" if net_flow > 0 else str(net_flow)
        return f"Transaction analysis: {ops} operations, net flow: {flow_str} units"

class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        errors = [e for e in data_batch if str(e).lower() == "error"]
        return f"Event analysis: {len(data_batch)} events, {len(errors)} error(s) detected"

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
        print("=== Polymorphic Stream Processing ===")
        for stream in self.streams:
            try:
                raw_data = batch_map.get(stream.stream_id, [])
                
                filtered = stream.filter_data(raw_data)
                result = stream.process_batch(filtered)
                stats = stream.get_stats()
                
                print(f"[{stats.get('type', 'Data')}] {result}")
            except Exception as e:
                print(f"Failure in stream {stream.stream_id}: {e}")

if __name__ == "__main__":
    manager = StreamProcessor()
    
    s_stream = SensorStream("SENSOR_001")
    t_stream = TransactionStream("TRANS_001")
    e_stream = EventStream("EVENT_001")
    
    manager.add_stream(s_stream)
    manager.add_stream(t_stream)
    manager.add_stream(e_stream)
    
    data_payload = {
        "SENSOR_001": [22.5, 35.0, 21.2],
        "TRANS_001": ["buy:100", "sell:50", "buy:25"],
        "EVENT_001": ["login", "error", "logout"]
    }
    
    manager.run_all(data_payload)

