import matplotlib.pyplot as plt

class Plotter():
    def plot(plot_text, output, font):
        plt.title(plot_text, fontsize=font, y=0.35)
        plt.axes().set_axis_off()
        plt.savefig(f"{output}.png")
