## Perl
export PLENV_ROOT=/opt/plenv
export PATH="/opt/plenv/bin:/opt/plenv/shims:$PATH"
eval "$(plenv init -)"

## Python
export PYENV_ROOT=/opt/pyenv
export PATH="/opt/pyenv/bin:/opt/pyenv/shims:$PATH"
eval "$(pyenv init -)"

## Ruby
export RBENV_ROOT=/opt/rbenv
export PATH="/opt/rbenv/bin:/opt/rbenv/shims:$PATH"
eval "$(rbenv init - zsh)"
