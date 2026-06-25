import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "tasks.json"

def load_tasks():
    """从 JSON 文件读取任务"""
    if not DATA_FILE.exists():
        return []
    
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []
    
def save_tasks(tasks):
    """把任务保存到 JSON 文件。"""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            tasks,
            file,
            ensure_ascii=False,
            indent=2
        )