# -*- Blueprint setup -*-
from sanic import Blueprint
from sanic.response import html, redirect
from server import J2env

HomeBP = Blueprint("HomeBP")


# -*- Routes -*-
@HomeBP.route('/')
async def home(request):
    template = J2env.get_template('/pages/Index.jinja2')
    _html = await template.render_async(title="Saadat Baig Development")
    return html(_html)


@HomeBP.route('/projects')
async def projects(request):
    template = J2env.get_template('/pages/Projects.jinja2')
    _html = await template.render_async(title="Projects | Saadat Baig Development")
    return html(_html)


@HomeBP.route('/github')
async def github(request):
    return redirect('https://github.com/mass1ve-err0r')


@HomeBP.route('/blog')
async def blog(request):
    return redirect('https://blog.saadat.dev/')


@HomeBP.route('/contact')
async def contact(request):
    template = J2env.get_template('/pages/Contact.jinja2')
    _html = await template.render_async(title="Contact | Saadat Baig Development")
    return html(_html)


@HomeBP.route('/privacy')
async def privacy(request):
    template = J2env.get_template('/pages/Privacy.jinja2')
    _html = await template.render_async(title="Privacy | Saadat Baig Development")
    return html(_html)
