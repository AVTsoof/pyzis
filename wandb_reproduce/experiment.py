import wandb

wandb.login()

with wandb.init(project='wandb_reproduce', dir="/tmp") as run:
    run.log_code(".")
    for i in range(10):
        wandb.log({"test": i})