from __future__ import annotations
import carb as carb
import isaacsim.core.api.sensors.base_sensor
from isaacsim.core.api.sensors.base_sensor import BaseSensor
from isaacsim.core.nodes.bindings import _isaacsim_core_nodes
from isaacsim.core.utils.extensions import get_extension_path_from_name
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.prims import get_prim_type_name
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils.stage import get_stage_units
import json as json
import math as math
import numpy as np
import omni as omni
from omni.graph import core as og
from omni.isaac.IsaacSensorSchema import IsaacRtxLidarSensorAPI
from omni.replicator import core as rep
from omni.syntheticdata.scripts import sensors
import os as os
__all__ = ['BaseSensor', 'IsaacRtxLidarSensorAPI', 'LidarRtx', 'carb', 'get_extension_path_from_name', 'get_prim_at_path', 'get_prim_type_name', 'get_stage_units', 'is_prim_path_valid', 'json', 'math', 'np', 'og', 'omni', 'os', 'rep', 'sensors']
class LidarRtx(isaacsim.core.api.sensors.base_sensor.BaseSensor):
    def __del__(self):
        ...
    def __init__(self, prim_path: str, name: str = 'lidar_rtx', position: typing.Optional[numpy.ndarray] = None, translation: typing.Optional[numpy.ndarray] = None, orientation: typing.Optional[numpy.ndarray] = None, config_file_name: typing.Optional[str] = None, firing_frequency: typing.Optional[int] = None, firing_dt: typing.Optional[float] = None, rotation_frequency: typing.Optional[int] = None, rotation_dt: typing.Optional[float] = None, valid_range: typing.Optional[typing.Tuple[float, float]] = None, scan_type: typing.Optional[str] = None, elevation_range: typing.Optional[typing.Tuple[float, float]] = None, range_resolution: typing.Optional[float] = None, range_accuracy: typing.Optional[float] = None, avg_power: float = None, wave_length: float = None, pulse_time: float = None) -> None:
        ...
    def _create_flat_scan_graph_node(self):
        ...
    def _create_point_cloud_graph_node(self):
        ...
    def _create_rtx_lidar_json_file(self, file_path: str, firing_frequency: typing.Optional[int] = None, rotation_frequency: typing.Optional[int] = None, valid_range: typing.Optional[typing.Tuple[float, float]] = None, scan_type: typing.Optional[str] = None, range_resolution: typing.Optional[float] = None, range_accuracy: typing.Optional[float] = None, avg_power: float = None, wave_length: float = None, pulse_time: float = None):
        ...
    def _data_acquisition_callback(self, event: carb.events._events.IEvent):
        ...
    def _stage_open_callback_fn(self, event):
        ...
    def _timeline_timer_callback_fn(self, event):
        ...
    def add_azimuth_data_to_frame(self):
        ...
    def add_azimuth_range_to_frame(self):
        ...
    def add_elevation_data_to_frame(self):
        ...
    def add_horizontal_resolution_to_frame(self):
        ...
    def add_intensities_data_to_frame(self):
        ...
    def add_linear_depth_data_to_frame(self):
        ...
    def add_point_cloud_data_to_frame(self):
        ...
    def add_range_data_to_frame(self):
        ...
    def disable_visualization(self):
        ...
    def enable_visualization(self):
        ...
    def get_azimuth_range(self) -> typing.Tuple[float, float]:
        ...
    def get_current_frame(self) -> dict:
        ...
    def get_depth_range(self) -> typing.Tuple[float, float]:
        ...
    def get_horizontal_fov(self) -> float:
        ...
    def get_horizontal_resolution(self) -> float:
        ...
    def get_num_cols(self) -> int:
        ...
    def get_num_rows(self) -> int:
        ...
    def get_render_product_path(self) -> str:
        """
        
                Returns:
                    string: gets the path to the render product used by the lidar
                
        """
    def get_rotation_frequency(self) -> float:
        ...
    def initialize(self, physics_sim_view = None) -> None:
        ...
    def is_paused(self) -> bool:
        ...
    def pause(self) -> None:
        ...
    def post_reset(self) -> None:
        ...
    def remove_azimuth_data_from_frame(self):
        ...
    def remove_azimuth_range_from_frame(self):
        ...
    def remove_elevation_data_from_frame(self):
        ...
    def remove_horizontal_resolution_from_frame(self):
        ...
    def remove_intensities_data_from_frame(self):
        ...
    def remove_linear_depth_data_from_frame(self):
        ...
    def remove_point_cloud_data_from_frame(self):
        ...
    def remove_range_data_from_frame(self):
        ...
    def resume(self) -> None:
        ...
