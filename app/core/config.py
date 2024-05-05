from app.models.azure import azure_config, batch_config
from azure.common.credentials import ServicePrincipalCredentials
import os
class SetupService:
   
    def __init__(self):
        self.sp_credentials = ServicePrincipalCredentials(
            client_id= azure_config.AZURE_CLIENT_ID,
            secret= azure_config.AZURE_CLIENT_SECRET,
            tenant_id= azure_config.AZURE_TENANT_ID,
            resource = batch_config.BATCH_RESOURCE_URI
        )

     