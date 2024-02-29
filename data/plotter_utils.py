from matplotlib import colors 
import matplotlib.pyplot as plt

color_dict = {
    0: "grey",
    1: "black",
    2: "red",
    3: "green",
    4: "blue",
    5: "yellow",
    6: "cyan",
    7: "magenta",
    8: "white",
    9: "purple"
}

vals, colorz = zip(*color_dict.items())
cmap = colors.ListedColormap(colors=colorz)
bounds=vals
norm = colors.BoundaryNorm(bounds, cmap.N)

def display_example_list(example_list):
    f, axarr = plt.subplots(len(example_list), 2, sharey=True)

    for i, ex in enumerate(example_list):
        axarr[i, 0].imshow(ex['input'], cmap=cmap, norm=norm)
        axarr[i, 1].imshow(ex['output'], cmap=cmap, norm=norm)
        axarr[i, 0].axis('off')
        axarr[i, 1].axis('off')
        axarr[i,0].autoscale(True)
        axarr[i,1].autoscale(True)

    plt.show()