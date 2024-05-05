# This file contains the AzureBatchService class which is used to interact with Azure Batch Service
from azure.batch import BatchServiceClient


from app.core.config import SetupService
from app.models.azure import batch_config
class AzureBatchService:
    def __init__(self, setup: SetupService):
        
        self.batch_client = BatchServiceClient(
            credentials=setup.sp_credentials,
            batch_url=batch_config.BATCH_ACCOUNT_URL
        )
        
    