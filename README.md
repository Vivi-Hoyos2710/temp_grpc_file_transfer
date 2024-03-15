# grpc-file-transfer

SSL secured file transfer gRPC client and server written in Python language.
Original Repo: https://github.com/r-sitko/grpc-file-transfer/blob/master/server/main.py

### Project structure

```
|-- cert - SSL certificates
|   `-- generate.sh - bash script for generating SSL certificates
|-- client - package with gRPC file transfer client code
|   |-- client.py
|   |-- __init__.py
|   `-- main.py
|-- protos - folder with gRPC interface for file transfer service
|   |-- file.proto
|   `-- __init__.py
|-- README.md
|-- requirements.txt
|-- resources
|   |-- client - example folder where files can be downloaded
|   `-- server - example folder for example files which can be downloaded
|       |-- test_file2.txt
|       `-- test_file.txt
`-- server - package with gRPC file transfer server code
    |-- __init__.py
    |-- main.py
    `-- server.py
```

### Prerequisites

* Python3
* pip3
* OpenSSL

### Example usage

1. Prepare project:
    - Go to project root directory.
    - Use the package manager for Python to install dependencies.
        ```bash
        pip3 install -r requirements.txt
        ```
    - Grant the owner of *cert/generate.sh* file execution permissions.
        ```bash
        chmod u+x cert/generate.sh
        ```
    - Generate certificate.\
        **Warning:** Don't use such created certificates for production environment.
        ```bash
        cert/generate.sh /CN=localhost
        ```
        CN (Common Name) must match server name that you connect to with the client. In this example we will use *localhost*.
1. Lauch gRPC file transfer server in first console:
    ```bash
    python3 server/main.py 
    ```
1. Lauch gRPC file transfer client in second console:
    - list available files to download from server
        ```bash
        python3 -m client.main -i localhost -p 5000 -c cert/server.crt list
        ```
    - download *test_file.txt* file from server to *resources/client* directory:
        ```bash
        python3 -m client.main -i localhost -p 5000 -c cert/server.crt download -d resources/client -f test_file.txt
        ```
    - upload file *test_file.txt* (by defaukt in a const dir)
        ```bash
        python3 -m client.main -i localhost -p 8000 -c cert/server.crt upload -f gatos.txt
        ```
## Description of client and server arguments

* server
```
```
* client
```
usage: main.py [-h] -i IP_ADRESS -p PORT -c CERT_FILE {download,list} ...

gRPC file transfer client

positional arguments:
  {download,list}       client possible actions
    download            download file from server
    list                list files on server

optional arguments:
  -h, --help            show this help message and exit
  -i IP_ADRESS, --ip_adress IP_ADRESS
                        IP address of server
  -p PORT, --port PORT  port address of server
  -c CERT_FILE, --cert_file CERT_FILE
                        certificate file path

If you use download action you must provide below paramaters:
optional arguments:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        where to save files
  -f FILE, --file FILE  file name to download
```
