# Zsh

## Install

### Install Z Shell
```sh
sudo apt-get install zsh
```

### Install oh-my-zsh

```sh
# You can use "cat /etc/shells" to check ZSH was installed.
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Change default terminal to ZSH

```sh
chsh -s /bin/zsh
```

### Install Plugins

- [zsh-autosuggestions](https://github.com/zsh-users/zsh-syntax-highlighting)

```sh
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

- [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)

```sh
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

Activate the plugin in ~/.zshrc

```sh
nano ~/.zshrc
```

Edit the line `plugins=(.....)` to

```sh
plugins=(git zsh-syntax-highlighting zsh-autosuggestions)
```

### Install Theme

- [Powerlevel10k Github](https://github.com/romkatv/powerlevel10k#meslo-nerd-font-patched-for-powerlevel10k)

```sh
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

You can use the command to change your style

```sh
p10k configure
```
