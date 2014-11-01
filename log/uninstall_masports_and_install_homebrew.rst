
cleanup macports
----------------------------------------

  % port installed > ~/macports.txt
  % sudo port -fp uninstall installed
  % sudo rm -rf \
      /opt/local \
      /Applications/DarwinPorts \
      /Applications/MacPorts \
      /Library/StartupItems/DarwinPortsStartup \
      /Library/Tcl/darwinports1.0 \
      /Library/Tcl/macports1.0 \
      ~/.macports

install environment
------------------------------

  % sudo mv /usr/local /usr/old.local
  % ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  % which brew
  % brew doctor
  % echo '/usr/local/bin
  /usr/bin
  /bin
  /usr/sbin
  /sbin' | sudo tee /etc/paths

install packages
------------------------------

  % brew install emacs
  % brew install tmux
  % brew install caskroom/cask/brew-cask
  % brew install rbenv
  % echo 'eval "$(rbenv init -)"' >> ~/.zshrc
  % brew install readline
  % brew install ruby-build
  % rbenv install 2.1.2
  % rbenv global 2.1.2
  % rbenv rehash
  % gem install bundler
  % gem install mysql2

  
