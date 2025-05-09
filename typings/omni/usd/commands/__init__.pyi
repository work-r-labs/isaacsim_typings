"""

This module provides a set of pre-defined undoable USD commands to help other extensions to implement undo/redo workflow. REMINDER: For those utilities that are marked as "Internal" but opened, it means those utilities are kept for back compatibility purpose, and should not be used out of this module. They may be deprecated or removed in the future release.
"""
import OmniAudioSchema as OmniAudioSchema
from __future__ import annotations
import carb as carb
from enum import Enum
from enum import auto
import math as math
import omni as omni
from omni.kit.usd_undo.layer_undo import UsdEditTargetUndo
from omni.usd.commands.stage_helper import UsdStageHelper
from omni.usd.commands.usd_commands import AddPayloadCommand
from omni.usd.commands.usd_commands import AddReferenceCommand
from omni.usd.commands.usd_commands import AddRelationshipTargetCommand
from omni.usd.commands.usd_commands import BindMaterialCommand
from omni.usd.commands.usd_commands import ChangeAttributesColorSpaceCommand
from omni.usd.commands.usd_commands import ChangeMetadataCommand
from omni.usd.commands.usd_commands import ChangeMetadataInPrimsCommand
from omni.usd.commands.usd_commands import ChangePropertyCommand
from omni.usd.commands.usd_commands import ClearCurvesSplitsOverridesCommand
from omni.usd.commands.usd_commands import ClearRefinementOverridesCommand
from omni.usd.commands.usd_commands import CopyPrimCommand
from omni.usd.commands.usd_commands import CopyPrimsCommand
from omni.usd.commands.usd_commands import CreateAudioPrimFromAssetPathCommand
from omni.usd.commands.usd_commands import CreateDefaultXformOnPrimCommand
from omni.usd.commands.usd_commands import CreateInstanceCommand
from omni.usd.commands.usd_commands import CreateInstancesCommand
from omni.usd.commands.usd_commands import CreateMdlMaterialPrimCommand
from omni.usd.commands.usd_commands import CreateMtlxMaterialPrimCommand
from omni.usd.commands.usd_commands import CreatePayloadCommand
from omni.usd.commands.usd_commands import CreatePreviewSurfaceMaterialPrimCommand
from omni.usd.commands.usd_commands import CreatePreviewSurfaceTextureMaterialPrimCommand
from omni.usd.commands.usd_commands import CreatePrimCommand
from omni.usd.commands.usd_commands import CreatePrimCommandBase
from omni.usd.commands.usd_commands import CreatePrimWithDefaultXformCommand
from omni.usd.commands.usd_commands import CreatePrimsCommand
from omni.usd.commands.usd_commands import CreateReferenceCommand
from omni.usd.commands.usd_commands import CreateShaderPrimFromSdrCommand
from omni.usd.commands.usd_commands import CreateUsdAttributeCommand
from omni.usd.commands.usd_commands import CreateUsdAttributeOnPathCommand
from omni.usd.commands.usd_commands import DeletePrimsCommand
from omni.usd.commands.usd_commands import FramePrimsCommand
from omni.usd.commands.usd_commands import GroupPrimsCommand
from omni.usd.commands.usd_commands import MovePrimCommand
from omni.usd.commands.usd_commands import MovePrimsCommand
from omni.usd.commands.usd_commands import ParentPrimsCommand
from omni.usd.commands.usd_commands import PayloadCommandBase
from omni.usd.commands.usd_commands import ReferenceCommandBase
from omni.usd.commands.usd_commands import RelationshipTargetBase
from omni.usd.commands.usd_commands import RemovePayloadCommand
from omni.usd.commands.usd_commands import RemovePropertyCommand
from omni.usd.commands.usd_commands import RemoveReferenceCommand
from omni.usd.commands.usd_commands import RemoveRelationshipTargetCommand
from omni.usd.commands.usd_commands import RenamePrimCommand
from omni.usd.commands.usd_commands import ReplacePayloadCommand
from omni.usd.commands.usd_commands import ReplaceReferenceCommand
from omni.usd.commands.usd_commands import ReplaceReferencesCommand
from omni.usd.commands.usd_commands import SelectPrimsCommand
from omni.usd.commands.usd_commands import SetMaterialStrengthCommand
from omni.usd.commands.usd_commands import SetPayLoadLoadSelectedPrimsCommand
from omni.usd.commands.usd_commands import SetRelationshipTargetsCommand
from omni.usd.commands.usd_commands import ToggleActivePrimsCommand
from omni.usd.commands.usd_commands import TogglePayLoadLoadSelectedPrimsCommand
from omni.usd.commands.usd_commands import ToggleVisibilitySelectedPrimsCommand
from omni.usd.commands.usd_commands import TransformPrimCommand
from omni.usd.commands.usd_commands import TransformPrimSRTCommand
from omni.usd.commands.usd_commands import TransformPrimsCommand
from omni.usd.commands.usd_commands import TransformPrimsSRTCommand
from omni.usd.commands.usd_commands import UngroupPrimsCommand
from omni.usd.commands.usd_commands import UnhideAllPrimsCommand
from omni.usd.commands.usd_commands import UnparentPrimsCommand
from omni.usd.commands.usd_commands import active_edit_context
from omni.usd.commands.usd_commands import allow_prim_parenting
from omni.usd.commands.usd_commands import ensure_parents_are_active
from omni.usd.commands.usd_commands import get_child_position_in_the_parent
from omni.usd.commands.usd_commands import get_context_and_stage
from omni.usd.commands.usd_commands import get_default_camera_rotation_order_str
from omni.usd.commands.usd_commands import get_default_rotation_order_str
from omni.usd.commands.usd_commands import get_default_rotation_order_type
from omni.usd.commands.usd_commands import move_prim_to_location
from omni.usd.commands.usd_commands import post_notification
from omni.usd.commands.usd_commands import prim_can_be_removed_without_destruction
from omni.usd.commands.usd_commands import remove_prim_spec
from omni.usd.commands.usd_commands import should_keep_children_order
from omni.usd.commands.usd_commands import write_refinement_override_enabled_hint
import os as os
from pxr import Gf
from pxr import Kind
from pxr import Sdf
from pxr import Sdr
from pxr import Tf
from pxr import Trace
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdLux
from pxr import UsdShade
from pxr import UsdUtils
import sys as sys
import weakref as weakref
from . import stage_helper
from . import usd_commands
__all__: list = ['GroupPrimsCommand', 'UngroupPrimsCommand', 'CreatePrimWithDefaultXformCommand', 'CreatePrimCommand', 'CopyPrimCommand', 'CopyPrimsCommand', 'CreateInstanceCommand', 'CreateInstancesCommand', 'DeletePrimsCommand', 'CreatePrimsCommand', 'CreateDefaultXformOnPrimCommand', 'BindMaterialCommand', 'SetMaterialStrengthCommand', 'TransformPrimCommand', 'TransformPrimSRTCommand', 'TransformPrimsCommand', 'TransformPrimsSRTCommand', 'FramePrimsCommand', 'SelectPrimsCommand', 'ToggleVisibilitySelectedPrimsCommand', 'UnhideAllPrimsCommand', 'MovePrimCommand', 'MovePrimsCommand', 'RenamePrimCommand', 'ReplaceReferencesCommand', 'CreateUsdAttributeOnPathCommand', 'CreateUsdAttributeCommand', 'ChangePropertyCommand', 'RemovePropertyCommand', 'ChangeMetadataInPrimsCommand', 'ChangeMetadataCommand', 'ChangeAttributesColorSpaceCommand', 'CreateMdlMaterialPrimCommand', 'CreateMtlxMaterialPrimCommand', 'CreateShaderPrimFromSdrCommand', 'CreatePreviewSurfaceMaterialPrimCommand', 'CreatePreviewSurfaceTextureMaterialPrimCommand', 'ClearCurvesSplitsOverridesCommand', 'ClearRefinementOverridesCommand', 'RelationshipTargetBase', 'AddRelationshipTargetCommand', 'RemoveRelationshipTargetCommand', 'SetRelationshipTargetsCommand', 'ReferenceCommandBase', 'AddReferenceCommand', 'RemoveReferenceCommand', 'ReplaceReferenceCommand', 'PayloadCommandBase', 'AddPayloadCommand', 'RemovePayloadCommand', 'ReplacePayloadCommand', 'CreatePrimCommandBase', 'CreateReferenceCommand', 'CreatePayloadCommand', 'CreateAudioPrimFromAssetPathCommand', 'post_notification', 'active_edit_context', 'remove_prim_spec', 'prim_can_be_removed_without_destruction', 'write_refinement_override_enabled_hint', 'get_default_rotation_order_str', 'get_default_camera_rotation_order_str', 'get_default_rotation_order_type', 'ensure_parents_are_active', 'ToggleActivePrimsCommand', 'UsdStageHelper', 'TogglePayLoadLoadSelectedPrimsCommand', 'SetPayLoadLoadSelectedPrimsCommand', 'ParentPrimsCommand', 'UnparentPrimsCommand']
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
SETTING_NESTED_GPRIMS_AUTHORING: str = '/persistent/app/stage/nestedGprimsAuthoring'
