import logging
import os
import time

import grpc

from protos.file_pb2 import FileDownloadReq,ListReq,FileUploadReq
from protos.file_pb2_grpc import FileStub

logger = logging.getLogger(__name__)

class FileClient:
  def __init__(self, ip_address, port, cert_file,root_dir):
    self.__ip_address = ip_address
    self.__port = port
    self.__cert_file = cert_file
    self.__files_directory=root_dir

    with open(self.__cert_file, "rb") as fh:
      trusted_cert = fh.read()
      
    # credentials = grpc.ssl_channel_credentials(root_certificates=trusted_cert)
    # channel = grpc.secure_channel("{}:{}"
    #   .format(self.__ip_address, self.__port), credentials)
    # self.stub = FileStub(channel)
      # Crear un canal gRPC inseguro
    channel = grpc.insecure_channel("{}:{}".format(self.__ip_address, self.__port))
    self.stub = FileStub(channel)

    logger.info("created instance " + str(self))

  def list(self):
    logger.info("downloading files list from server")
    response_stream = self.stub.list(ListReq())
    self.__list_files(response_stream)

  def download(self, file_name,chunk_name):
    logger.info("downloading chunk {chunk} from file:{file_name}".format(file_name=file_name,chunk=chunk_name))
    req= FileDownloadReq(filename=file_name,chunkname=chunk_name)
   
    try:
      #Remote Call procedure download
      response_bytes = self.stub.download(req)
      self.__saving_chunk(response_bytes, chunk_name, file_name)
    except grpc.RpcError as e:
        logger.error("gRPC error: {}".format(e.details()))
        print("An error occurred while downloading the chunk: {}".format(e.details()))
    

  def __saving_chunk(self, response_bytes, out_file_name, out_file_dir):
    try:
      #Si directorio no existe, lo crea para guardar las particiones del archivo.
      directory=os.path.join(self.__files_directory, out_file_dir)
      if not os.path.exists(directory):
        os.mkdir(directory)
      with open(directory+"/"+out_file_name, "wb") as fh:
        fh.write(response_bytes.buffer)
    except Exception as e:
        print("An error occurred while saving the chunk: {}".format(e))
        logger.error("Error while saving chunk: {}".format(e))
      
  def upload(self,file_name,out_file_dir):
    file_path= get_file_path(file_name= file_name)
    logger.info(file_path)
    try:
      with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            upload_request = FileUploadReq(name=file_name, buffer=chunk)
            response = self.stub.upload(upload_request)
            print(response)
    except:
      print('An exception occurred')
    

  def __list_files(self, response_stream):
    for response in response_stream:
      print("file name: {}, size: {} bytes".format(response.name, response.size))

  def __str__(self):
    return "ip:{ip_address}, port:{port}, cert_file:{cert_file}"\
      .format(
        ip_address=self.__ip_address,
        port=self.__port,
        cert_file=self.__cert_file)
def get_file_path(file_name):
    # Obtener la ruta absoluta del directorio actual
    current_directory = "resources/client"

    # Unir la ruta absoluta del directorio actual con el nombre de archivo proporcionado
    file_path = os.path.join(current_directory, file_name)

    return file_path