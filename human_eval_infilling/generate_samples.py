from human_eval_infilling.data import read_problems, write_jsonl


def generate_one_completion(prompt, suffix):
    return "    return "


def generate_samples(benchmark_name: str, num_samples_per_task: int):
    problems = read_problems(benchmark_name=benchmark_name)
    num_samples_per_task = 1
    samples = [
        dict(
            task_id=task_id,
            completion=generate_one_completion(
                problems[task_id]["prompt"], problems[task_id]["suffix"]
            ),
        )
        for task_id in problems
        for _ in range(num_samples_per_task)
    ]
    write_jsonl("./data/samples.jsonl", samples)
    return samples


if __name__ == "__main__":
    generate_samples("test", 1)
