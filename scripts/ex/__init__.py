def type_1(rdm):
    plot = "$({}^{})^{}$".format(rdm["a"], rdm["y"], rdm["z"])
    data = {
        "tipo" : 1,
        "plot" : plot,
        "font" : 93
    }
    return data

def type_2(rdm):
    plot = "${}^{}\cdot{}^{}$".format(rdm["a"], rdm["y"], rdm["a"], rdm["z"])
    data = {
        "tipo" : 2,
        "plot" : plot,
        "font" : 100
    }
    return data

def type_3(rdm):
    plot = "${}^{}:{}^{}$".format(rdm["a"], rdm["y"], rdm["a"], rdm["z"])
    data = {
        "tipo" : 3,
        "plot" : plot,
        "font" : 93
    }
    return data

def type_4(rdm):
    plot = "${}^{}\cdot{}^{}$".format(rdm["a"], rdm["y"], rdm["b"], rdm["y"])
    data = {
        "tipo" : 6,
        "plot" : plot,
        "font" : 100
    }
    return data

def type_7(rdm):
    plot = "${}^{}:{}^{}$".format(rdm["a"], rdm["y"], rdm["b"], rdm["y"])
    data = {
        "tipo" : 7,
        "plot" : plot,
        "font" : 93
    }
    return data

def type_8(rdm):
    plot = "${}^{}$".format(rdm["q"], rdm["y"])
    data = {
        "tipo" : 8,
        "plot" : plot,
        "font" : 93
    }
    return data
