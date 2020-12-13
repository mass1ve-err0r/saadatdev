# -*- Blueprint setup -*-
from datetime import datetime
from sanic import Blueprint
from sanic.response import html, redirect
from server import J2env, EMailObject

HomeBP = Blueprint("HomeBP")


async def createEMailObject(_mail, _subj, _mesg, _stamp):
    rv_t = dict(
    email = _mail,
    subject = _subj,
    message = _mesg,
    date = _stamp
    )
    return rv_t


async def getDateAsUTC():
    return datetime.utcnow()


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


@HomeBP.route('/contact', methods=['GET', 'POST'])
async def contact(request):
    user_ip = request.remote_addr
    with await request.app.redis as redis:
        access_nums = await redis.get(user_ip)
        if access_nums == None:
            await redis.set(user_ip, "1")
        else:
            if int(access_nums) < 250:
                await redis.incr(user_ip)
            else:
                return redirect('https://saadat.dev/safety_timeout')
    err_type = -1
    if request.method == 'POST':
        if request.form.get('emailInput') != None:
            if request.form.get('subjectInput') != None:
                if request.form.get('messageInput') != None:
                    user_mesg = request.form.get('messageInput')
                    user_subj = request.form.get('subjectInput')
                    user_mail = request.form.get('emailInput')
                    if len(user_mesg) > 1500 or len(user_subj) > 200 or len(user_mail) > 200:
                        return redirect('https://saadat.dev/safety_timeout')
                    tstamp = await getDateAsUTC()
                    new_mail = await createEMailObject(user_mail, user_subj, user_mesg, tstamp)
                    await EMailObject.insert_one(doc=new_mail)
                    err_type = 0
                else:
                    err_type = 3
            else:
                err_type = 2
        else:
            err_type = 1
    template = J2env.get_template('/pages/Contact.jinja2')
    _html = await template.render_async(title="Contact | Saadat Baig Development",
                                        bannerType=err_type)
    return html(_html)


@HomeBP.route('/privacy')
async def privacy(request):
    template = J2env.get_template('/pages/Privacy.jinja2')
    _html = await template.render_async(title="Privacy | Saadat Baig Development")
    return html(_html)
