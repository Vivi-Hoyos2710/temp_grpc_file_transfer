from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FileDownloadRsp(_message.Message):
    __slots__ = ("buffer",)
    BUFFER_FIELD_NUMBER: _ClassVar[int]
    buffer: bytes
    def __init__(self, buffer: _Optional[bytes] = ...) -> None: ...

class FileDownloadReq(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRsp(_message.Message):
    __slots__ = ("name", "size")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    name: str
    size: int
    def __init__(self, name: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...

class FileUploadReq(_message.Message):
    __slots__ = ("buffer", "name")
    BUFFER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    buffer: bytes
    name: str
    def __init__(self, buffer: _Optional[bytes] = ..., name: _Optional[str] = ...) -> None: ...

class UploadRsp(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
