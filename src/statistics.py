import json
from pathlib import Path


dataset_path = Path('/Users/elena/Documents/summarization/summarization-dataset/dataset')

domain2info = dict()

for domain_dir in dataset_path.iterdir():
    if not domain_dir.is_dir():
        continue

    n_tables = 0
    n_figures = 0
    n_tokens = 0
    n_chars = 0
    n_tokens_abstract = 0
    n_chars_abstract = 0
    n_unique_tokens = 0

    for text_dir in domain_dir.iterdir():
        if not text_dir.is_dir():
            continue
        with open(text_dir / 'abstract.txt', 'r') as f:
            abstract_file = f.read()
            n_chars_abstract += len(abstract_file)
            tokens = abstract_file.split(' ')
            n_tokens_abstract += len(tokens)
        with open(text_dir / 'text.txt', 'r') as f:
            text_file = f.read()
            n_chars += len(text_file)
            tokens = text_file.split(' ')
            n_tokens += len(tokens)
            n_unique_tokens += len(set(tokens))
        figures_path = text_dir / 'figures.json'
        if figures_path.exists():
            with open(figures_path, 'r') as f:
                data = json.load(f)
                n_figures += len(data)
        tables_path = text_dir / 'tables.json'
        if tables_path.exists():
            with open(tables_path, 'r') as f:
                data = json.load(f)
                n_tables += len(data)

    res = {
        'n_tables': n_tables,
        'n_figures': n_figures,
        'n_tokens': n_tokens,
        'n_chars': n_chars,
        'n_unique_tokens': n_unique_tokens,
        'n_tokens_abstract': n_tokens_abstract,
        'n_chars_abstract': n_chars_abstract
    }

    domain2info[domain_dir.name] = res

for domain, data in domain2info.items():
    print(f'[{domain}]')
    for feat, val in data.items():
        print(f'{feat}: {val}')
    print('=' * 100)
