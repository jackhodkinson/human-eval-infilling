from human_eval_infilling.data import write_jsonl, read_problems

problems = read_problems(benchmark_name="test")


def generate_one_completion(prompt, suffix):
    return "    return "


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
