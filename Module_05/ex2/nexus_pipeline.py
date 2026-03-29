import time
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Protocol, Union
from collections import Counter


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Any:
        if data is None:
            raise ValueError("Invalid Input: Data is None")
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        return str(data).strip().upper()


class OutputStage:
    def process(self, data: Any) -> str:
        return f"Final Nexus Output: {data}"


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.performance_stats: Dict[str, Union[int, float]] = {
            "count": 0,
            "total_time": 0.0
        }

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def run_pipeline(self, data: Any) -> Any:
        start_time = time.perf_counter()
        current_val = data

        try:
            for stage in self.stages:
                current_val = stage.process(current_val)

            self.performance_stats["count"] = int(
                self.performance_stats["count"]) + 1
            self.performance_stats["total_time"] = float(
                self.performance_stats["total_time"]) + (
                    time.perf_counter() - start_time
                )
            return current_val

        except Exception as e:
            print(f"Error detected in pipeline {self.pipeline_id}: {e}")
            print("Recovery initiated: Switching to backup processor")
            return f"RECOVERED_DATA: {str(data)}"

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> str:
        return str(self.run_pipeline(data))


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> str:
        return str(self.run_pipeline(data))


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> str:
        return str(self.run_pipeline(data))


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []
        self.event_log: Counter = Counter()

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
        for p in self.pipelines:
            pid = p.pipeline_id
            ptime = p.performance_stats["total_time"]
            print(f"Pipeline {pid} Efficiency: {ptime:.4f}s")


if __name__ == "__main__":
    manager = NexusManager()

    json_pipe = JSONAdapter("JSON_PROC_01")
    csv_pipe = CSVAdapter("CSV_PROC_01")

    for p in [json_pipe, csv_pipe]:
        p.add_stage(InputStage())
        p.add_stage(TransformStage())
        p.add_stage(OutputStage())

    manager.add_pipeline(json_pipe)
    manager.add_pipeline(csv_pipe)

    samples = {
        "JSON_PROC_01": {"sensor": "temp", "val": 25},
        "CSV_PROC_01": "user_id, login_time, ip_addr"
    }
    manager.orchestrate_all(samples)

    print("\n=== Pipeline Chaining Demo ===")
    raw_input = "Chain_Start"
    intermediate = json_pipe.process(raw_input)
    final_chain = csv_pipe.process(intermediate)
    print(f"Chain Result (Pipe A -> Pipe B): {final_chain}")

    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    error_result = json_pipe.process(None)
    print(f"Recovery successful: {error_result}")

    manager.show_metrics()
    print("\nNexus Integration complete. All systems operational.")
