from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional, List

@dataclass
class ConllConfig:
    delimiter: str = '\t' or '\n'
    skip_blank_lines: bool = True
    column_names: Optional[List[str]] = None


class Conll:
    BUILDER_CLASS_CONFIG = ConllConfig
    
    def _split_generators(filepath): 
        with open(filepath, "r") as f:

            lines = f.readlines()
            for line in lines:

                ## Two Types of inputs
                # Docstart, and Tags

                if line.strip() == '': 

                    pass 
                