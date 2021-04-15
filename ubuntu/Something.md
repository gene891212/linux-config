# Something May Need

> Get something you may need here

## Something

```bash
sudo apt install curl
```

## Change User Dir Name To English

```bash
export LANG=en_US
xdg-user-dirs-gtk-update
```

## Install gnome tweak tool

```bash
sudo apt install gnome-tweak-tool
sudo apt install gnome-shell-extensions
```

## Some alias and function in .zshrc

```bash
alias cat='batcat --paging=never'
alias catn='batcat --paging=never -p'
alias '\cat'='batcat --paging=never -p'

alias aria='aria2c -x 16 -s 16 --retry-wait=1'

alias mrpi='sudo sshfs -o allow_other pi@raspberrypi.local:/home/pi/ /home/gene/RaspberryPi'

# Using 'open <fileName or url>' command like macOS
function open() { xdg-open $1 &> /dev/null; }
```

- In [Chrome Web Store](https://chrome.google.com/webstore/category/extensions) install [GNOME Shell integration](https://chrome.google.com/webstore/detail/gnome-shell-integration/gphhapmejobijbbhgpjhcjognlahblep)
- In [GNOME Shell Extensions](https://extensions.gnome.org) install [Sound Input & Output Device Chooser](https://extensions.gnome.org/extension/906/sound-output-device-chooser/)
