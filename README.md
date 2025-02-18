# Quickflags

This tool lets you toggle stored display flags.

## Usage

#### Keybinds
Select nodes, press Ctrl+Shift+1, 2, 3, 4, or 5

Change their flags to something else

Press Shift+1, 2, 3, 4, or 5 to restore previously selected nodes to their stored flag states (they don't need to be selected anymore at this point).

#### Radial Menu
You need to enter the radial menu panel and find the tool in the Network Editor category and assign a hotkey to it.

![image](https://github.com/user-attachments/assets/b3f861f5-ca8e-407a-a2cd-67d0c1283bfc)

You can then use it in any network pane just like the Quickmark radial menu.

## Details
Currently the tool only supports Display, Template, Bypass and Render flags.

## Installation
Download the latest release or the current source code.

Install as a package by first editing `quickflags.json` and changing the path to where you store this package, for example `"hpath": "C:/mypackages/quickflags"`, to your `$HOUDINI_USER_PREF_DIR/packages/quickflags.json`

If installed correctly, you should now have a Quickflags shelf tab available.

![image](https://github.com/user-attachments/assets/3c51ed68-d5dc-4b1f-bac0-75c0b0de8407)
