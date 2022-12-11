# `--no-tty` runs the command given in `--cmd`
# The pwd is copied to `/app` in the container by default
wandb docker --no-tty --cmd "python experiment.py" --rm fastai/jekyll
