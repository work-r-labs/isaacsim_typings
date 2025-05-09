from __future__ import annotations
import carb as carb
import omni as omni
from omni.ui import scene as sc
import pxr.Gf
from pxr import Gf
from pxr import UsdGeom
import typing
__all__: list = ['SimpleGrid', 'SimpleOrigin', 'CameraAxisLayer']
class CameraAxisLayer:
    CAMERA_AXIS_DEFAULT_SIZE: typing.ClassVar[tuple] = (60, 60)
    CAMERA_AXIS_SIZE_SETTING: typing.ClassVar[str] = '/app/viewport/defaults/guide/axis/size'
    visible = ...
    def _CameraAxisLayer__view_changed(self, viewport_api):
        ...
    def _CameraAxisLayer__viewport_axis_display_changed(self, item: carb.dictionary._dictionary.Item, event_type: carb.settings._settings.ChangeEventType):
        ...
    def _CameraAxisLayer__viewport_axis_size_changed(self, item: carb.dictionary._dictionary.Item, event_type: carb.settings._settings.ChangeEventType):
        ...
    def __init__(self, desc: dict):
        ...
    def destroy(self):
        ...
    @property
    def categories(self):
        ...
    @property
    def name(self):
        ...
class SimpleGrid:
    visible = ...
    def _SimpleGrid__view_changed(self, viewport_api):
        ...
    def _SimpleGrid__viewport_grid_display_changed(self, item: carb.dictionary._dictionary.Item, event_type: carb.settings._settings.ChangeEventType):
        ...
    def __del__(self):
        ...
    def __init__(self, vp_args, line_count: float = 100, line_step: float = 10, thicknes: float = 1, color: typing.Optional[<omni.ui.color_utils.ColorShade object>] = None):
        ...
    def destroy(self):
        ...
    @property
    def categories(self):
        ...
    @property
    def name(self):
        ...
class SimpleOrigin:
    visible = ...
    def _SimpleOrigin__viewport_origin_display_changed(self, item: carb.dictionary._dictionary.Item, event_type: carb.settings._settings.ChangeEventType):
        ...
    def __init__(self, desc: dict, visible: bool = False, length: float = 5, thickness: float = 4):
        ...
    def destroy(self):
        ...
    @property
    def categories(self):
        ...
    @property
    def name(self):
        ...
def _flatten_matrix(matrix: pxr.Gf.Matrix4d):
    ...
def _flatten_rot_matrix(matrix: pxr.Gf.Matrix3d):
    ...
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
