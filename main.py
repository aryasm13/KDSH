import os
import json
from dotenv import load_dotenv

load_dotenv()
from src.KdshRag.KdshRag import KdshRag
from src.KdshRag.utils.config_utils import BaseConfig
from src.KdshRag.utils.misc_utils import get_gold_answers
import csv

csv_path="./test.csv"


def write_results_csv(queries, solutions, output_csv):
    import csv, os

    os.makedirs(os.path.dirname(output_csv), exist_ok=True)

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "label", "reason"])
        writer.writeheader()

        for q, sol in zip(queries, solutions):
            writer.writerow({
                "id": q["id"],
                "label": sol["label"],
                "reason": sol["reason"]
            })

def build_queries_from_csv(csv_path):
    """
    Reads CSV with fields:
    id, book_name, char, caption, content, label

    Returns:
    - List[dict] with keys: id, character, content
    """
    queries = []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            queries.append({
    "id": row["id"].strip(),
    "book_name": row["book_name"].strip(),
    "character": row["char"].strip(),
    "content": row["content"].strip()
})

    return queries



def process_dataset(config):
    print("processing all the queries prcoeding for the result plese wait: ")
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

    csv_path = os.path.join(PROJECT_ROOT, "test.csv")
    output_csv = os.path.join(PROJECT_ROOT, "results.csv")

    all_queries = build_queries_from_csv(csv_path)

    kdshRag = KdshRag(global_config=config)
    solutions = kdshRag.try_answer(all_queries)

    write_results_csv(all_queries, solutions, output_csv)

  
def main():
    print("program execution started please wait, preapring the environemnt")
    base_path = './dataset/KDSH'
    dataset_dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
    
    dataset_dirs.sort()
    dataset_paths = [os.path.join(base_path, d) for d in dataset_dirs]
    

    config = BaseConfig(
        llm_base_url=os.environ["llm_base_url"],
        llm_name='gpt-4o-mini',
        llm_api_key=os.environ["OPENAI_API_KEY"],
        dataset='monte_cristo',
        embedding_model_name='BAAI/bge-base-en-v1.5',
        embedding_batch_size=32,
        need_cluster=True,
        output_dir='result/KDSH',
        save_dir="outputs/KDSH",
        max_meta_loop_max_iterations=5,
        is_mc=False,
        max_tokens_ver=2000,
        max_tokens_sem=2000,
        max_tokens_epi=2000
    )

    import copy

  
    tempconfig = copy.deepcopy(config)
        
    process_dataset(tempconfig)

if __name__ == "__main__":
    main()
