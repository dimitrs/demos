from rctk.widgets import Window, StaticText, Panel

from all import DemoPanel

class DemoRunner(object):
    def __init__(self, demo_class):
        self.demo = demo_class()

    def run(self, tk):
        p = DemoPanel(tk)
        tk.root().append(p)
        self.demo.build(tk, p.buildpanel)

def serve_demo(demo_class):
    serve(DemoRunner, demo_class)

def standalone(demo_class):
    def factory():
        return DemoRunner(demo_class)
    return factory
