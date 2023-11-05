from pathlib import Path

# Path Variables
path_home = Path.home()
path_sub = "Library/CloudStorage/Dropbox"
path_full = path_home / path_sub
path_script = rf"{path_full}/mho_scripts"
path_tex = rf"{path_full}/mho_tex/0-tex"
path_mho_tex = rf"{path_full}/mho_tex"
path_tex_main = rf"{path_full}/mho_tex"
path_org = rf"{path_full}/mho_denote"
path_assets = rf"{path_full}/assets"
path_png = rf"{path_full}/assets/png"
# Used by tex_all
path_tikz = rf"{path_full}/assets/tikz"
path_python = rf"{path_full}/assets/python"
path_pytex = rf"{path_full}/assets/pytex"
