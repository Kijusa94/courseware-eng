import matplotlib
import matplotlib.pyplot as plt
import schemdraw
import schemdraw.elements as elm

def dc_circuit_volt_measure():
    with schemdraw.Drawing(show=False) as d:
        c1 = elm.SourceV().label("$V_{cc}$")
        c2 = elm.Line().right()
        c3 = elm.Resistor().label("R").down()
        c4 = elm.c2 = elm.Line().left()
        c5 = elm.Line().at(c3.start).right()
        c6 = elm.MeterV().down()
        c7 = elm.Line().tox(c1.end)
        elm.CurrentLabel().at(c3)
    return d

def dc_circuit_ampt_measure():
    with schemdraw.Drawing(show=False) as d:
        c1 = elm.SourceV().label("$V_{cc}$")
        c2 = elm.Resistor().label("R", loc="bottom").right()
        c3 = elm.MeterA().down()
        c4 = elm.Line().tox(c1["end"])
        elm.CurrentLabel().at(c2)
    return d

def dc_circuit_resis_measure():
    with schemdraw.Drawing(show=False) as d:
        c1 = elm.SourceV().label("$V_{cc}$")
        c2 = elm.Switch(contacts=False).right()
        c3 = elm.Resistor().label("R").down()
        c4 = elm.c2 = elm.Line().left()
        c5 = elm.Line().at(c3.start).right()
        c6 = elm.MeterOhm().down()
        c7 = elm.Line().tox(c1.end)
    return d

def dc_circuits_parallel():
    def branch(label_name):
        with schemdraw.Drawing(show=False) as d1:
            elm.Line().length(d1.unit/2)
            with d1.hold():
                elm.Resistor().down().label(f'$R_{label_name}$')
                elm.Line().left().length(d1.unit/2)
        return d1

    with schemdraw.Drawing(show=False) as d2:
        for i in range(3):
            elm.ElementDrawing(branch(str(i+1)))
            
        with d2.hold():
            elm.Line().length(d2.unit/6)
            elm.DotDotDot()
            elm.ElementDrawing(branch("n"))
        d2.move(dy=-d2.unit)
        elm.Line().right(d2.unit/6)
        elm.DotDotDot()

    return d2

def dc_circuits_series():
    def series_element(label_name):
        with schemdraw.Drawing(show=False) as d1:
            elm.Resistor().label(f'$R_{label_name}$', loc="bottom").label(["+",f"$V_{label_name}$","-"], loc="top")
        return d1

    with schemdraw.Drawing(show=False) as d2:
        for i in range(3):
            elm.ElementDrawing(series_element(str(i+1)))

        with d2.hold():
            elm.DotDotDot()
            elm.ElementDrawing(series_element("n"))
    return d2