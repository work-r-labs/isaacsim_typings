from __future__ import annotations
import carb as carb
import omni.kit.usd.layers._omni_kit_usd_layers
from omni.kit.usd.layers._omni_kit_usd_layers import ILayersInstance
from omni.kit.usd.layers._omni_kit_usd_layers import acquire_specs_locking_interface
from omni.kit.usd.layers._omni_kit_usd_layers import release_specs_locking_interface
from pxr import Sdf
__all__: list = ['SpecsLocking']
class SpecsLocking:
    def __init__(self, layers_instance: omni.kit.usd.layers._omni_kit_usd_layers.ILayersInstance, usd_context) -> None:
        ...
    def _destroy(self):
        ...
    def _populate_all_paths(self, item: carb.dictionary._dictionary.Item):
        ...
    def get_all_locked_specs(self) -> typing.List[str]:
        ...
    def is_spec_locked(self, spec_path: typing.Union[str, pxr.Sdf.Path]) -> bool:
        ...
    def lock_spec(self, spec_path: typing.Union[str, pxr.Sdf.Path], hierarchy: bool = False) -> typing.List[str]:
        ...
    def unlock_all_specs(self):
        ...
    def unlock_spec(self, spec_path: typing.Union[str, pxr.Sdf.Path], hierarchy: bool = False) -> typing.List[str]:
        ...
    @property
    def usd_context(self):
        ...
