from proto import admin_pb2_grpc

from app.gateway.service.admin_service import AdminServiceImpl

class AdminServicer(admin_pb2_grpc.AdminServicer):
    async def DeleteUser(self, request, context) -> admin_pb2_grpc.Empty:
        return await AdminServiceImpl().DeleteUser(request, context)
    
    async def DeletePost(self, request, context) -> admin_pb2_grpc.Empty:
        return await AdminServiceImpl().DeletePost(request, context)

    async def BanUser(self, request, context) -> admin_pb2_grpc.Empty:
        return await AdminServiceImpl().BanUser(request, context)
    