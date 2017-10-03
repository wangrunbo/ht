"""
Jinja过滤器
"""
from .. import app


@app.template_filter()
def test(arg):
    pass
