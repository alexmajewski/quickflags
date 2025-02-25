import hou
import nodegraphview
import nodegraphutils as utils
from PySide2.QtCore import QSettings

def set_quickflag(kwargs, index):
    """Stores flag states of selected nodes and editor in Houdini session."""
    quickflag_dict = {}
    node_states = {}
    for node in hou.selectedNodes():
        path = node.path()
        state = {
            path: {
                "display": node.isGenericFlagSet(hou.nodeFlag.Display),
                "render": node.isGenericFlagSet(hou.nodeFlag.Render),
                "template": node.isGenericFlagSet(hou.nodeFlag.Template),
                "bypass": node.isGenericFlagSet(hou.nodeFlag.Bypass)
            }
        }
        
        node_states.update(state)
        
    quickflag_dict["node_states"] = node_states

    settings = QSettings(QSettings.IniFormat, QSettings.UserScope, "Quickflags", "Quickflags")
    store_editor_loc = to_bool(settings.value("store_editor_loc", True))

    if store_editor_loc:
        editor_state = get_location(kwargs, index)
        quickflag_dict["editor_state"] = editor_state

    setattr(hou.session, f"quickflag{index}", quickflag_dict)


def get_quickflag(kwargs, index):
    """Gets stored flag and editor states in Houdini session and applies them to nodes in the network and changes visible bounds of the editor."""

    if hasattr(hou.session, f"quickflag{index}"):
        
        quickflag = getattr(hou.session, f"quickflag{index}", {})

        for node_path in quickflag["node_states"]:
            if hou.node(node_path):
            
                display_val = quickflag.get("node_states", {}).get(node_path, {}).get("display")
                render_val = quickflag.get("node_states", {}).get(node_path, {}).get("render")
                template_val = quickflag.get("node_states", {}).get(node_path, {}).get("template")
                bypass_val = quickflag.get("node_states", {}).get(node_path, {}).get("bypass")
                            
                hou.node(node_path).setGenericFlag(hou.nodeFlag.Display, display_val)
                hou.node(node_path).setGenericFlag(hou.nodeFlag.Render, render_val)
                hou.node(node_path).setGenericFlag(hou.nodeFlag.Template, template_val)
                hou.node(node_path).setGenericFlag(hou.nodeFlag.Bypass, bypass_val)

        if "editor_state" in quickflag:
            settings = QSettings(QSettings.IniFormat, QSettings.UserScope, "Quickflags", "Quickflags")
            store_editor_loc = to_bool(settings.value("store_editor_loc", True))
            if store_editor_loc:
                jump_to_location(kwargs, index, quickflag["editor_state"])
            
def to_bool(value):
    """Converts lowercase booleans from settings to actual Python booleans"""
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        return value == 1
    return value.lower() == 'true' if isinstance(value, str) else False

def get_location(kwargs, index):
    """Gets current path and bounds of the editor"""
    editor = kwargs['pane']
    net = editor.pwd()
    bounds = editor.visibleBounds()

    editor_data = {
        'net': editor.pwd().path(),
        'bounds': [
            bounds.min().x(),
            bounds.min().y(),
            bounds.max().x(),
            bounds.max().y()
        ]
    }
    return editor_data
    

def jump_to_location(kwargs, index, editor_state):
    """Sets editor's path and bounds to stored state"""
    editor = kwargs['pane']
    bounding_rect = hou.BoundingRect(*editor_state['bounds'])
    
    if editor_state['net'] != editor.pwd().path():
        if hou.node(editor_state['net']):
            editor.cd(editor_state['net'])
        else:
            return

    editor.setVisibleBounds(bounding_rect, utils.getViewUpdateTime(editor))
