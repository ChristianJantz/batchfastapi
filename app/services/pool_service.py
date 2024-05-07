from app.models.pool import SubmitPoolSchema
from app.core.azure_batch import AzureBatchService
from app.models.azure import batch_config, azure_config
from azure.batch.models import PoolAddParameter, VirtualMachineConfiguration, ImageReference, NetworkConfiguration, ContainerConfiguration, ContainerRegistry
class PoolService:
    def __init__(self):
        self.azure_batch_service = AzureBatchService()

    def create_pool(self, pool_options: SubmitPoolSchema):
        
        container_registry = ContainerRegistry(
            registry_server=pool_options.container_registry,
            user_name=pool_options.container_registry_username,
            password=pool_options.container_registry_password
        )
        
        new_pool = PoolAddParameter(
            id = pool_options.id,
            vm_size=pool_options.vm_size,
            virtual_machine_configuration= VirtualMachineConfiguration(
                image_reference= ImageReference(
                    publisher=pool_options.vm_publisher,
                    offer=pool_options.vm_offer,
                    sku=pool_options.vm_sku,
                    version=pool_options.vm_version
                ),
                node_agent_sku_id=pool_options.vm_node_agent,
                container_configuration= ContainerConfiguration(
                    type=pool_options.container_type,
                    container_image_names=[pool_options.container_image],
                    container_registries=[container_registry]
                ) if pool_options.vm_publisher == "microsoft-azure-batch" else None
            ),
            enable_auto_scale= True,
            auto_scale_formula= f'$TargetDedicated={pool_options.vm_count}',
            network_configuration= NetworkConfiguration(
                subnet_id=f"/subscriptions/{batch_config.BATCH_SUBSCRIPTION_ID}/resourceGroups/{batch_config.BATCH_VNET_RESOURCE_GROUP}/providers/Microsoft.Network/virtualNetworks/{batch_config.BATCH_VNET_NAME}/subnets/{batch_config.BATCH_SUBNET_NAME}"
            )
        )
        self.azure_batch_service.batch_client.pool_options.add(new_pool)
        

    def delete_pool(self, pool_id: str):
        self.azure_batch_service.batch_client.pool_options.delete(pool_id)
        return pool_id



   
