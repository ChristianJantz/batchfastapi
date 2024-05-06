from app.models.pool import SubmitPoolSchema
from app.core.azure_batch import AzureBatchService
from app.models.azure import batch_config, azure_config
from azure.batch.models import PoolAddParameter, VirtualMachineConfiguration, ImageReference, NetworkConfiguration, ContainerConfiguration, ContainerRegistry
class PoolService:
    def __init__(self):
        self.azure_batch_service = AzureBatchService()

    def create_pool(self, pool: SubmitPoolSchema):
        
        container_registry = ContainerRegistry(
            registry_server=pool.container_registry,
            user_name=pool.container_registry_username,
            password=pool.container_registry_password
        )
        
        new_pool = PoolAddParameter(
            id = pool.id,
            vm_size=pool.vm_size,
            virtual_machine_configuration= VirtualMachineConfiguration(
                image_reference= ImageReference(
                    publisher=pool.vm_publisher,
                    offer=pool.vm_offer,
                    sku=pool.vm_sku,
                    version=pool.vm_version
                ),
                node_agent_sku_id=pool.vm_node_agent,
                container_configuration= ContainerConfiguration(
                    type=pool.container_type,
                    container_image_names=[pool.container_image],
                    container_registries=[container_registry]
                ) if pool.vm_publisher == "microsoft-azure-batch" else None
            ),
            enable_auto_scale= True,
            auto_scale_formula= f'$TargetDedicated={pool.vm_count}',
            network_configuration= NetworkConfiguration(
                subnet_id=f"/subscriptions/{batch_config.BATCH_SUBSCRIPTION_ID}/resourceGroups/{batch_config.BATCH_VNET_RESOURCE_GROUP}/providers/Microsoft.Network/virtualNetworks/{batch_config.BATCH_VNET_NAME}/subnets/{batch_config.BATCH_SUBNET_NAME}"
            )
        )
        self.azure_batch_service.batch_client.pool.add(new_pool)
        

    def delete_pool(self, pool_id: str):
        self.azure_batch_service.batch_client.pool.delete(pool_id)
        return pool_id



   
