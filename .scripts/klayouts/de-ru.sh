#!/bin/bash
setxkbmap -option 'grp:toggle' -layout de,ru
xmodmap -e 'keycode 135 = endash' 
