from pydantic import BaseModel


class Task(BaseModel):
    name: str
    job_id: str
    command: str
    pool_id: str
    
