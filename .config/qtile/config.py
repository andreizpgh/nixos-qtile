# ==============================================================================
#                            QTILE CONFIGURATION FILE                          
# ==============================================================================

from typing import List

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod1"
terminal = "alacritty"

# ------------------------------------------------------------------------------
# KEY BINDINGS 

keys = [
    # Terminal
    Key([mod], "Return", lazy.spawn("alacritty -e zsh")),
     
    # WM controls
    Key([mod, "control"], "k", lazy.layout.grow()),
    Key([mod, "control"], "j", lazy.layout.shrink()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod], "k", lazy.layout.up()),   
    Key([mod], "j", lazy.layout.down()),

    Key([mod], "a", lazy.group["a"].toscreen(toggle = False)),
    Key([mod], "s", lazy.group["s"].toscreen(toggle = False)),
    Key([mod], "d", lazy.group["d"].toscreen(toggle = False)),
    Key([mod], "f", lazy.group["f"].toscreen(toggle = False)),
    Key([mod], "u", lazy.group["u"].toscreen(toggle = False)),
    Key([mod], "i", lazy.group["i"].toscreen(toggle = False)),
    Key([mod], "o", lazy.group["o"].toscreen(toggle = False)),
    Key([mod], "p", lazy.group["p"].toscreen(toggle = False)),

    Key([mod, "shift"], "a", lazy.window.togroup("a")),
    Key([mod, "shift"], "s", lazy.window.togroup("s")),
    Key([mod, "shift"], "d", lazy.window.togroup("d")),
    Key([mod, "shift"], "f", lazy.window.togroup("f")),
    Key([mod, "shift"], "u", lazy.window.togroup("u")),
    Key([mod, "shift"], "i", lazy.window.togroup("i")),
    Key([mod, "shift"], "o", lazy.window.togroup("o")),
    Key([mod, "shift"], "p", lazy.window.togroup("p")),

    # Toggle between different layouts 
    Key([mod], "Tab", lazy.next_layout()),

    # Kill focused window
    Key([mod], "q", lazy.window.kill()),
    
    # Restart and shutdown
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),

    # Rofi
    Key([mod], "r", lazy.spawn("rofi -show run")),
    Key([mod], "w", lazy.spawn("rofi -show window")),
    #Key([mod], "z", lazy.spawn("bash /home/andrei/.scripts/rofi-file-browser.sh")),
    Key([mod], "c", lazy.spawn("bash rofi -modi 'clipboard:greenclip print' -show clipboard -run-command '{cmd}'")),

    # Sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+")), 

    # Brightness
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 15")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 15")),

    # Keyboard layouts
    Key([mod], "1", lazy.spawn("bash /home/andrei/.scripts/klayouts/us-ru.sh")),
    Key([mod], "2", lazy.spawn("bash /home/andrei/.scripts/klayouts/de-ru.sh")),
    Key([mod], "3", lazy.spawn("bash /home/andrei/.scripts/klayouts/es-ru.sh")),

    # Miscellaneous
    Key([], "Print", lazy.spawn("flameshot gui")),
    Key([mod], "v", lazy.spawn("alacritty -e vifm /home/andrei")),
    Key([mod], "m", lazy.spawn("alacritty -e sc-im /home/andrei/Documents/money.sc"))
]

# ------------------------------------------------------------------------------
# WORKSPACES
groups = [
    Group("a", layout="monadtall", spawn="emacs"),
    Group("s", layout="monadtall", spawn="firefox"),
    Group("d", layout="monadtall"),
    Group("f", layout="max", spawn="telegram-desktop"),
    Group("u", layout="monadtall"),
    Group("i", layout="monadtall"),
]

# ------------------------------------------------------------------------------
# LAYOUTS

layouts = [
    layout.MonadTall(
        margin = 7,
        border_focus = '#46D9FF',
        border_width = 1,
        single_border_width = 0,
        single_margin = 0
        ),
    layout.Max(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# ------------------------------------------------------------------------------
# BAR 

screens = [
]

# ------------------------------------------------------------------------------
# Drag floating layouts

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
])

# ------------------------------------------------------------------------------
# General
auto_fullscreen = False
focus_on_window_activation = "smart"

wmname = "LG3D"

