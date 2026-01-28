import grpc
from proto import admin_pb2_grpc

from app.gateway.gRPC.admin_server import AdminServicer

async def serve():
    server = grpc.aio.server()
    admin_pb2_grpc.add_AdminServicer_to_server(AdminServicer(), server)
    server.add_insecure_port('[::]:50056')
    print ("gRPC сервер запущен на порту 50056...")
    await server.start()
    await server.wait_for_termination()