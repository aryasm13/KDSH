import os
import json
import copy
from src.KdshRag.KdshRag import KdshRag
from src.KdshRag.utils.config_utils import BaseConfig


def build_index(dataset_path, config):
    corpus_path = os.path.join(dataset_path, "corpus.jsonl")

    with open(corpus_path, 'r', encoding='utf-8') as f:
        corpus = [json.loads(line) for line in f if line.strip()]

    docs = [doc['contents'] for doc in corpus]
    config.corpus_len = len(docs)

    print(f"[INDEXING] {os.path.basename(dataset_path)} | docs = {len(docs)}")

    KdshRag = KdshRag(global_config=config)
    KdshRag.index(docs)

    print(f"[DONE] Index built at: {config.save_dir}")


def main():
    os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")

    base_path = "./dataset/cinderella"
    dataset_dirs = sorted(
        d for d in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, d))
    )

    base_config = BaseConfig(
        llm_base_url="https://api.openai.com/v1",
        llm_name="gpt-4o-mini",
        llm_api_key=os.environ["OPENAI_API_KEY"],
        dataset="cinderella",
        embedding_model_name="BAAI/bge-base-en-v1.5",
        embedding_batch_size=32,
        need_cluster=True,
        save_dir="outputs/cinderella",
        max_meta_loop_max_iterations=5,
        is_mc=False,
        max_tokens_ver=2000,
        max_tokens_sem=2000,
        max_tokens_epi=2000
    )

    for d in dataset_dirs:
        dataset_path = os.path.join(base_path, d)
        config = copy.deepcopy(base_config)
        config.save_dir = os.path.join(base_config.save_dir, d)
        


if __name__ == "__main__":
    main()
