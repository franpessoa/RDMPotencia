from flask import Flask, render_template, request, send_file, redirect
import scripts as src
import os

plotter = src.plot.Plotter()

rdmn = {
    "type1" : [],
    "type2" : [],
    "type3" : [],
    "type4" : [],
    "type5" : [],
    "type6" : [],
    "type7" : [],
    "type8" : []
}

for i in rdmn.keys():
    os.mkdir(f"./ex/{i}")
    for s in range(1250):
        rdmn[i].append(src.ex.plot(i, src.random.get_num()))
    for e, s in enumerate(rdmn[i]):
        plotter.plot(output=f"./ex/{i}/{e}.png", font=s["font"], plot=s["plot"])

app = Flask(" ")
