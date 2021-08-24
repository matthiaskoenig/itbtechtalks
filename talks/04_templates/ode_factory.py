"""
Convert ODE systems for various programming languages and formats.
This allows easy integration with existing workflows by rendering respective code templates.

Currently supported code generation:
- python: scipy
- R: desolve
- HTML
"""
import os
from pprint import pprint
import re
from collections import defaultdict
import jinja2


# template location (for language templates)
TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')


class ODESystem(object):
    """ Class for storing information about ODE system.

        Demonstrates rendering of the information to various templates.
    """
    def __init__(self, mid, pids, p, xids, x0, yids, y, dxdt, zids, z):
        """ Storing information about ODE system.

        :param mid: model id
        :param pids: parameter ids (list)
        :param p: parameter {pid: value}
        :param xids: state ids (list)
        :param x0: initial state conditions {xid: value}
        :param yids: intermediate variables ids
        :param y: intermediate variables used in odes {yid: formula}
        :param dxdt: ordinary differential equations dxd
        :param zids: post-processing variables ids
        :param z: post-processing variables {zid: formula}
        """
        self.mid = mid
        self.pids = pids
        self.p = p
        self.xids = xids
        self.x0 = x0
        self.yids = yids
        self.y = y
        self.dxdt = dxdt
        self.zids = zids
        self.z = z

    def to_python(self, py_file):
        """ Write ODEs to python.

        :param py_file:
        :return:
        """
        content = self._render_template(template="template.py", index_offset=0)
        with open(py_file, "w") as f:
            f.write(content)

    def to_R(self, r_file):
        """ Write ODEs to R.

        :param py_file:
        :return:
        """
        content = self._render_template(template="template.R", index_offset=1)
        with open(r_file, "w") as f:
            f.write(content)

    def to_HTML(self, html_file):
        """ Write ODEs to HTML report.

        :param html_file:
        :return:
        """
        content = self._render_template(template="template.html", index_offset=1)
        with open(html_file, "w") as f:
            f.write(content)

    def _render_template(self, template='template.py', index_offset=0):
        """ Renders given language template.

        :param template:
        :return:
        """
        # template environment
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR),
                                 extensions=['jinja2.ext.autoescape'],
                                 trim_blocks=True,
                                 lstrip_blocks=True)

        # load the template
        template = env.get_template(template)

        # context for rendering the template
        c = {
            'mid': self.mid,
            'xids': self.xids,
            'pids': self.pids,
            'yids': self.yids,
            'zids': self.zids,

            'x0': self.x0,
            'p': self.p,
            'y': self.y,
            'z': self.z,
            'dxdt': self.dxdt,
        }
        return template.render(c)

#####################################################################################

if __name__ == "__main__":
    # -------------------------
    # Definition of ODE system
    # -------------------------
    mid = "lorenz"
    pids = ['r', 'b', 'sigma']
    p = {
        'r': 45.92,
        'b': 4.0,
        'sigma': 16.0
    }

    xids = ['x', 'y', 'z']
    x0 = {
        'x': 1.0,
        'y': 1.0,
        'z': 1.0,
    }
    yids = []
    y = {}
    dxdt = {
        'x': "sigma * (y - x)",
        'y': "x * (r - z) - y",
        'z': "x * y - b * z",
    }

    zids = ['tot', 'xf', 'yf', 'zf']
    z = {
        'tot': "x + y + z",
        'xf': "x/tot",
        'yf': "y/tot",
        'zf': "z/tot",
    }

    odes = ODESystem(mid=mid, pids=pids, p=p, xids=xids, x0=x0, yids=yids, y=y, dxdt=dxdt, zids=zids, z=z)


    # convert xpp to sbml

    out_dir = './odefac_example/results'

    # Render templates
    py_file = os.path.join('.', 'results', "{}.py".format(mid))
    r_file = os.path.join('.', 'results', "{}.R".format(mid))
    html_file = os.path.join('.', 'results', "{}.html".format(mid))

    print('to_python')
    odes.to_python(py_file)
    print('to_R')
    odes.to_R(r_file)
    print('to_html')
    odes.to_HTML(html_file)
