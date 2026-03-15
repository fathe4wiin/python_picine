from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol
import time
from collections import Counter

# 1. ProcessingStage Protocol (Duck Typing)
# Any class with a process() method automatically implements this.
class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...

# 2. Stage Implementations (Satisfy the Protocol)
class InputStage:
    def process(self, data: Any) -> Any:
        if data is None:
            raise ValueError("Invalid Input: Data is None")
        return data

class TransformStage:
    def process(self, data: Any) -> Any:
        # Simple transformation: cleaning and converting to string
        return str(data).strip().upper()

class OutputStage:
    def process(self, data: Any) -> str:
        return f"Final Nexus Output: {data}"

# 3. Pipeline Base Class (ABC)
class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.performance_stats = {"count": 0, "total_time": 0.0}

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def run_pipeline(self, data: Any) -> Any:
        start_time = time.perf_counter()
        current_val = data
        
        try:
            for stage in self.stages:
                current_val = stage.process(current_val)
            
            self.performance_stats["count"] += 1
            self.performance_stats["total_time"] += (time.perf_counter() - start_time)
            return current_val
            
        except Exception as e:
            # Error Recovery logic
            print(f"!!! Error in {self.pipeline_id}: {e}")
            print("Initiating recovery: Switching to backup formatting...")
            return f"RECOVERED_DATA: {str(data)}"

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

# 4. Data Adapters (Inheritance)
class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> str:
        # Simulate format-specific logic
        return self.run_pipeline(data)

class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> str:
        return self.run_pipeline(data)

class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> str:
        return self.run_pipeline(data)

# 5. Nexus Manager (Orchestrator)
class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []
        self.event_log = Counter()

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def orchestrate_all(self, data_samples: Dict[str, Any]) -> None:
        print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
        for pipe in self.pipelines:
            input_data = data_samples.get(pipe.pipeline_id)
            result = pipe.process(input_data)
            print(f"Result for {pipe.pipeline_id}: {result}")
            self.event_log["processed"] += 1

    def show_metrics(self) -> None:
        print("\n=== Performance Monitoring ===")
        # Dict comprehension for stats
        report = {p.pipeline_id: f"{p.performance_stats['total_time']:.4f}s" for p in self.pipelines}
        for pid, ptime in report.items():
            print(f"Pipeline {pid} Efficiency: {ptime}")

# 6. Main Execution & Pipeline Chaining
if __name__ == "__main__":
    manager = NexusManager()

    # Setup Pipelines
    json_pipe = JSONAdapter("JSON_PROC_01")
    csv_pipe = CSVAdapter("CSV_PROC_01")

    # Add Stages (Composition)
    for p in [json_pipe, csv_pipe]:
        p.add_stage(InputStage())
        p.add_stage(TransformStage())
        p.add_stage(OutputStage())

    manager.add_pipeline(json_pipe)
    manager.add_pipeline(csv_pipe)

    # 1. Normal Processing
    samples = {
        "JSON_PROC_01": {"sensor": "temp", "val": 25},
        "CSV_PROC_01": "user_id, login_time, ip_addr"
    }
    manager.orchestrate_all(samples)

    # 2. Pipeline Chaining Demo
    print("\n=== Pipeline Chaining Demo ===")
    raw_input = "Chain_Start"
    intermediate = json_pipe.process(raw_input)
    final_chain = csv_pipe.process(intermediate)
    print(f"Chain Result (Pipe A -> Pipe B): {final_chain}")

    # 3. Performance Stats
    manager.show_metrics()