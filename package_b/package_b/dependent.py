from package_a import plot_robinson, plot_mollweide


def plot_all(name:str):
    if name == "rob":
        plot_robinson()
    else:
        plot_mollweide()
