from scripts import random, plot, pdf, ex
import matplotlib.pyplot as plt

s = random.get_num()
p = ex.type_10(s)

plt.title(p["plot"], fontsize=p["font"], y=0.35)
plt.axes().set_axis_off()
plt.savefig("out.png")