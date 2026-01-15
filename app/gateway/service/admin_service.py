from proto import admin_pb2
from app.kafka.repositories.kafka_repositories import KafkaRepository
from app.gateway.service.iadmin_service import IAdminService


class AdminServiceImpl(IAdminService):
    def __init__(self):
        self.kf = KafkaRepository()

    async def DeleteUser(self, request, context) -> admin_pb2.Empty:
        await self.kf.send_message(topic="admin_delete_user", message={"id": request.id})
        return admin_pb2.Empty()
    
    async def DeletePost(self, request, context) -> admin_pb2.Empty:
        await self.kf.send_message(topic="admin_delete_post", message={"id": request.id})
        return admin_pb2.Empty()
    
    async def BanUser(self, request, context) -> admin_pb2.Empty:
        await self.kf.send_message(topic="admin_ban_user", message={"id": request.id})
        return admin_pb2.Empty()
    
