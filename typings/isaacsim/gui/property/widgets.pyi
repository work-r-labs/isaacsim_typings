from __future__ import annotations
from isaacsim.gui.property.array_widget import ArrayPropertiesWidget
from isaacsim.gui.property.custom_data import CustomDataWidget
import omni as omni
__all__ = ['ArrayPropertiesWidget', 'CustomDataWidget', 'IsaacPropertyWidgets', 'omni']
class IsaacPropertyWidgets(omni.ext._extensions.IExt):
    def __init__(self):
        ...
    def _register_widget(self):
        ...
    def _unregister_widget(self):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
