# Quickflags

This is a Houdini tool that lets you toggle stored display flags in similar fashion to Quickmarks.

![animated-gif-of-tool-in-use](https://github.com/user-attachments/assets/395407c0-65ad-40e9-a7d7-192a9efac6df)


## Usage

#### Keybinds
Select nodes, press Ctrl+Shift+1, 2, 3, 4, or 5

Change their flags to something else

Press Shift+1, 2, 3, 4, or 5 to restore previously selected nodes to their stored flag states (they don't need to be selected anymore at this point).

NOTE: This package uses a new hotkey format introduced in H20.5. These hotkeys are set on shelf tools and can be rebound manually on older Houdini versions.

#### Radial Menu
You need to enter the radial menu panel and find the tool in the Network Editor category and assign a hotkey to it.

![screenshot-of-radial-menu-edit-panel](https://github.com/user-attachments/assets/b3f861f5-ca8e-407a-a2cd-67d0c1283bfc)

You can then use it in any network pane just like the Quickmark radial menu.

## Settings
Settings are available in the shelf tool. They allow you to disable/enable Quickflags to trigger Quickmarks as well.

## Details
Currently the tool only supports Display, Template, Bypass and Render flags.

## Installation
Download the latest release or the current source code.

Install as a package by first editing `quickflags.json` and changing the path to where you store this package (for example `"hpath": "C:/mypackages/quickflags.json"`), then copying it to your `$HOUDINI_USER_PREF_DIR/packages/quickflags.json`

If installed correctly, you should now have a Quickflags shelf tab available.

![screenshot-of-houdini-shelf](https://github.com/user-attachments/assets/1fe23577-eab8-40f3-9564-6822bdcb3ddf)
