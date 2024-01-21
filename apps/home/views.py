from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from instagram_manager.models import Instagram


@login_required(login_url="/login/")
def index(request):
    context = {"segment": "dashboard-instagram"}

    html_template = loader.get_template("home/dashboard-instagram.html")
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request, *args, **kwargs):
    context = {}
    try:
        load_template = request.path.split("/")[-1]
        print("template -", load_template)
        if load_template == "admin":
            return HttpResponseRedirect(reverse("admin:index"))
        context["segment"] = load_template

        html_template = loader.get_template("home/" + load_template)
        if load_template == "dashboard-instagram.html":
            user = request.user
            user_instagram = Instagram.objects.filter(main_user=user)
            
            if list(user_instagram) != []:
                context["instagram"] = list(user_instagram)[0]
                context["has_instagram"] = True
            else:
                context["has_instagram"] = False

            if kwargs and kwargs['link-instagram']:
                context["page"] = 'link-instagram'
                
            print("context -", context)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template("home/page-404.html")
        return HttpResponse(html_template.render(context, request))

    except Exception as e:
        print(e)
        html_template = loader.get_template("home/page-500.html")
        return HttpResponse(html_template.render(context, request))
