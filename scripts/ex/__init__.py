def plot(type, rdm):
    if type == "type1"(rdm):
        plot = "$({}^{})^{}$".format(rdm["a"], rdm["y"], rdm["z"])
        data = {
            "tipo" : 1,
            "plot" : plot,
            "font" : 93
        }
        return data

    if type == "type2"(rdm):
        plot = "${}^{}\cdot{}^{}$".format(rdm["a"], rdm["y"], rdm["a"], rdm["z"])
        data = {
            "tipo" : 2,
            "plot" : plot,
            "font" : 100
        }
        return data

    if type == "type3"(rdm):
        plot = "${}^{}:{}^{}$".format(rdm["a"], rdm["y"], rdm["a"], rdm["z"])
        data = {
            "tipo" : 3,
            "plot" : plot,
            "font" : 93
        }
        return data

    if type == "type4"(rdm):
        plot = "${}^{}\cdot{}^{}$".format(rdm["a"], rdm["y"], rdm["b"], rdm["y"])
        data = {
            "tipo" : 6,
            "plot" : plot,
            "font" : 100
        }
        return data

    if type == "type7"(rdm):
        plot = "${}^{}:{}^{}$".format(rdm["a"], rdm["y"], rdm["b"], rdm["y"])
        data = {
            "tipo" : 7,
            "plot" : plot,
            "font" : 93
        }
        return data

    if type == "type8"(rdm):
        plot = "${}^{}$".format(rdm["q"], rdm["y"])
        data = {
            "tipo" : 8,
            "plot" : plot,
            "font" : 93
        }
        return data
