import os

class AzureConfig:
    AZURE_CLIENT_ID = os.getenv('AZURE_CLIENT_ID')
    AZURE_CLIENT_SECRET = os.getenv('AZURE_CLIENT_SECRET')
    AZURE_TENANT_ID = os.getenv('AZURE_TENANT_ID')
    AZURE_SUBSCRIPTION_ID = os.getenv('AZURE_SUBSCRIPTION_ID')

class BatchConfig:
    BATCH_RESOURCE_URI = os.getenv('BATCH_RESOURCE_URI')
    BATCH_ACCOUNT_NAME = os.getenv('BATCH_ACCOUNT_NAME')
    BATCH_ACCOUNT_KEY = os.getenv('BATCH_ACCOUNT_KEY')
    BATCH_ACCOUNT_URL = os.getenv('BATCH_ACCOUNT_URL')
    BATCH_VNET_NAME = os.getenv('BATCH_VNET_NAME')
    BATCH_SUBNET_NAME = os.getenv('BATCH_SUBNET_NAME')
    BATCH_VNET_RESOURCE_GROUP = os.getenv('BATCH_VNET_RESOURCE_GROUP')
    BATCH_SUBSCRIPTION_ID = os.getenv('BATCH_SUBSCRIPTION_ID')
    
    
    
azure_config = AzureConfig()
batch_config = BatchConfig()