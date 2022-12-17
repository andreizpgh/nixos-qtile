#!/bin/bash
setxkbmap -option 'grp:toggle' -layout us,ru
xmodmap -e 'keycode 135 = endash'
