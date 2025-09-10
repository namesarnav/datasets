from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional, List

@dataclass
class ConllConfig:
    delimiter: str = '\t' or '\n'
    skip_blank_lines: bool = True
    column_names: Optional[List[str]] = None

