import cartopy.crs as ccrs
import matplotlib.pyplot as plt

def plot_mollweide():
    ax = plt.axes(projection=ccrs.Mollweide())
    ax.stock_img()
    plt.savefig("mollwide.png")

def plot_robinson():
    ax = plt.axes(projection=ccrs.Robinson())
    ax.stock_img()
    plt.savefig("robinson.png")

