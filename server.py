from dotenv import load_dotenv
load_dotenv()

# -*- Sanic configg 4 fest deploiment -*-
from sanic import Sanic
app = Sanic("saadatdotdev")
app.static('/static', './static')


# -*- Jinja2 setup -*-
from jinja2 import Environment, PackageLoader, select_autoescape
J2env = Environment(loader=PackageLoader('server', './templates'),
                    autoescape=select_autoescape(['html', 'xml']),
                    enable_async=True)
J2env.globals["url_for"] = app.url_for


# -*- Blueprint Registration -*-
from Blueprints.Home import HomeBP
app.blueprint(HomeBP)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)