from __future__ import annotations
from pathlib import Path
import json
from typing import List

from stages import Lead

class LeadRepository:
    def __init__(self, base_dir: Path | None = None) -> None:
        root = Path(__file__).resolve().parent
        self.data_dir = (base_dir or (root / "data"))
        self.data_dir.mkdir(exist_ok=True)
        self.db_path = self.data_dir / "leads.json"

    def _load_raw(self) -> list[dict]:
        if not self.db_path.exists():
            return []
        try:
            return json.loads(self.db_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []

    def _save_raw(self, rows: list[dict]) -> None:
        self.db_path.write_text(
            json.dumps(rows, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

    def add_lead(self, lead: Lead) -> None:
        rows = self._load_raw()
        rows.append(lead.to_dict())
        self._save_raw(rows)

    def list_leads(self) -> List[Lead]:
        rows = self._load_raw()
        return [Lead.from_dict(r) for r in rows]

