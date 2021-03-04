# Grub2

## Install

### Install Graphic Tool Of Grub

```sh
sudo apt install grub-customizer
```
You can change `menu` and `timeout` in the grub-customizer
```sh
grub-customizer
```

### Install Theme

Install theme on [GROME-LOOK.ORG](https://www.gnome-look.org/browse/cat/109/order/latest/)

- [Sleek GrubBootloader themes](https://www.gnome-look.org/p/1414997/)

Extract theme and run

```sh
cd 'Sleek theme-bigSur'
bash install.sh
```

Activate theme

```sh
sudo nano /etc/grub.d/00_header
```

Add two lines in the top of the `00_header` file, and save the file

```sh
# GRUB_THEME="/usr/share/grub/themes/${your_theme_name}/theme.txt"
GRUB_THEME="/usr/share/grub/themes/sleek/theme.txt"
GRUB_GFXMODE="1920x1080x32"
```

Update setting
```sh
sudo update-grub
```

**The path you might need:**
```
# Where theme install
/usr/share/grub/themes/

# Grub default setting
/etc/default/grub

# Config menu list
/etc/grub.d
```
