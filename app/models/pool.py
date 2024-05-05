from pydantic import BaseModel

class Pool(BaseModel):
    name: str
    vm_size: str
    vm_count: int
    vm_publisher: str
    vm_offer: str
    vm_sku: str
    vm_version: str
    vm_node_agent: str
    container_image: str
    container_registry: str
    container_registry_username: str
    container_registry_password: str
    