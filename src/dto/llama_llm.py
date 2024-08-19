from datetime import datetime

from pydantic import BaseModel

import src.enums as enums


class LlamaResponse(BaseModel):
    model: enums.LlamaModels
    created_at: datetime
    response: str
    done: bool
    done_reason: str
    context: list[int]
    total_duration: int
    load_duration: int
    prompt_eval_count: int
    prompt_eval_duration: int
    eval_count: int
    eval_duration: int
