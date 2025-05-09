from __future__ import annotations
import typing
__all__ = ['DirectoryItemType', 'File', 'IFileSystem', 'acquire_filesystem']
class DirectoryItemType:
    """
    Members:
    
      FILE
    
      DIRECTORY
    """
    DIRECTORY: typing.ClassVar[DirectoryItemType]  # value = <DirectoryItemType.DIRECTORY: 1>
    FILE: typing.ClassVar[DirectoryItemType]  # value = <DirectoryItemType.FILE: 0>
    __members__: typing.ClassVar[dict[str, DirectoryItemType]]  # value = {'FILE': <DirectoryItemType.FILE: 0>, 'DIRECTORY': <DirectoryItemType.DIRECTORY: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class File:
    pass
class IFileSystem:
    def close_file(self, arg0: File) -> None:
        ...
    def copy(self, arg0: str, arg1: str) -> bool:
        ...
    def exists(self, arg0: str) -> bool:
        ...
    def flush_file(self, arg0: File) -> None:
        ...
    def get_app_directory_path(self) -> str:
        ...
    def get_current_directory_path(self) -> str:
        ...
    def get_file_size(self, arg0: File) -> int:
        ...
    def get_mod_time(self, arg0: str) -> int:
        ...
    def is_directory(self, arg0: str) -> bool:
        ...
    def make_directory(self, arg0: str) -> bool:
        ...
    def make_temp_directory(self) -> typing.Any:
        ...
    def open_file_to_append(self, arg0: str) -> File:
        ...
    def open_file_to_read(self, arg0: str) -> File:
        ...
    def open_file_to_write(self, arg0: str) -> File:
        ...
    def remove_directory(self, arg0: str) -> bool:
        ...
    def set_app_directory_path(self, arg0: str) -> None:
        ...
    def set_current_directory_path(self, arg0: str) -> bool:
        ...
def acquire_filesystem(plugin_name: str = None, library_path: str = None) -> IFileSystem:
    ...
