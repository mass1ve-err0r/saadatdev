from dotenv import load_dotenv
load_dotenv()

# -*- Sanic configg 4 fest deploiment -*-
from sanic import Sanic
app = Sanic("saadatdotdev")
app.static('/static', './static')
app.config.update({
    "PROXIES_COUNT": 1,
    "REAL_IP_HEADER": "X-Real-IP",
    "FORWARDED_SECRET": "placeholder_secret"
})

# -*- Sanic Extensions -*-
from sanic_redis_ext import RedisExtension
app.config.update({
    "REDIS_HOST": "127.0.0.1",
    "REDIS_PORT": 6379,
    "REDIS_DATABASE": None,
    "REDIS_SSL": None,
    "REDIS_ENCODING": None,
    "REDIS_MIN_SIZE_POOL": 1,
    "REDIS_MAX_SIZE_POOL": 10
})
RedisExtension(app)

from sanic_motor import BaseModel
app.config.update({
    "MOTOR_URI": 'mongodb://localhost:27017/placeholder_db',
})
BaseModel.init_app(app)


class EMailObject(BaseModel):
    __coll__ = 'placeholder_collection'
    __unique_fields__ = ['date']


# -*- Jinja2 setup -*-
from jinja2 import Environment, PackageLoader, select_autoescape
J2env = Environment(loader=PackageLoader('server', './templates'),
                    autoescape=select_autoescape(['html', 'xml']),
                    enable_async=True)
J2env.globals["url_for"] = app.url_for


# -*- Custom Exception Handler -*-
from sanic.exceptions import SanicException
from sanic.response import html
@app.exception(SanicException)
async def catch_exceptions_4xx_5xx(req, excp):
    template = J2env.get_template('/pages/Error_4xx_5xx.jinja2')
    _html = await template.render_async(title="Whoops! | Saadat Baig Development")
    return html(_html)


# -*- Blueprint Registration -*-
from Blueprints.Home import HomeBP
app.blueprint(HomeBP)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, access_log=False)
