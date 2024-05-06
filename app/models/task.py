from pydantic import BaseModel


class SubmitTaskSchema(BaseModel):
    name: str
    job_id: str
    command: str
    pool_id: str
    
