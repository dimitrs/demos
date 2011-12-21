from rctkdemos.demos import serve_demo, standalone
from rctk.zk.widgets import Chart

class Demo(object):
    title = "Chart"
    description = "Demonstrates the Chart control"

    def build(self, tk, parent):
        series = [('Jane', [1, 0, 4]), ('John', [5, 7, 3])]
        chart = Chart(tk, series, chart_type="bar", chart_title="Fruit")
        parent.append(chart)


Standalone = standalone(Demo)

if __name__ == '__main__':
    serve_demo(Demo)

