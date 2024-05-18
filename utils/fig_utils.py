import os
def save_fig(fig, output_folder, title):
    save_dir = os.path.join(output_folder, title.strip() + ".png")
    fig.savefig(save_dir)
    return save_dir