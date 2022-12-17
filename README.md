# NIXOS INSTALLATION


### 1. Partitioning

| Partition | File System | Label | Size | Flags |
| --------- | ----------- | ----- | ---- | ----- |
| /dev/sda1 | linux-swap  | swap  | 2048 | –     |
| /dev/sda2 | ext4        | msdos | –    | boot  |

### 2. Nixos Configuration

`sudo mount /dev/disk/by-label/msdos /mnt`

`sudo nixos-generate-config --root /mnt`

```
sudo wget -P /mnt/etc/nixos/configuration.nix https://raw.githubusercontent.com/andreizpgh/nixos-qtile/main/nixos-qtile/basic-configuration.nix
```

`sudo nixos-install`

`sudo reboot`

### 3. Further Configuration

- **Log in as root and set password**
`passwd andrei`

- **Activate an internet connection**
`nmtui`

- **Clone the repo**

`git clone https://github.com/andreizpgh/nixos-qtile`

- **Rewrite configuration.nix**
```
sudo rm /etc/nixos/configuration.nix && sudo ln -s /home/andrei/nixos-qtile/nixos-qtile/configuration.nix /etc/nixos/configuration.nix 
```

- **Reboot** 
`sudo reboot`

### 4. Setting-up

- **Command**
```
mkdir .cache/zsh /home/andrei/.config/alacritty /home/andrei/.config/nvim /home/andrei/.config/rofi /home/andrei/.config/zathura && touch .cache/zsh/history .cache/greenclip.history && rm -rf /home/andrei/Desktop && rm /home/andrei/.config/vifm/vifmrc && stow -d /home/andrei/nixos-qtile . && sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim' && nix-env -iA nixos.zsh-autosuggestions && nix-env -iA nixos.zsh-syntax-highlighting && lxappearance
``` 

- **Neovim**

`PlugUpdate`

- **Install Doom Emacs**
```
git clone https://github.com/hlissner/doom-emacs ~/.emacs.d && yes | ~/.emacs.d/bin/doom install && ~/.emacs.d/bin/doom sync
```
 
- **Log in into Firefox and import 'Scroll Anywhere', 'Vimium' and 'Simple Translate' configs + userChrome.css**
