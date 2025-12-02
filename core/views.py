from django.shortcuts import render, get_object_or_404, redirect
from .models import (
    GeneralSettinModel,
    ImageModel,
    SkillModel,
    SocialModel,
    Document,
    Messages,
)
from django.http import JsonResponse
from .forms import ContactForm


# Create your views here.
def get_general_setting(parameter):
    try:
        return GeneralSettinModel.objects.get(name=parameter).parameter
    except:
        return None


def get_general_setting_description(parameter):
    try:
        return GeneralSettinModel.objects.get(name=parameter).description
    except:
        return None


def get_image_setting(parameter):
    try:
        return ImageModel.objects.get(name=parameter).image
    except:
        return None


def get_skill_setting(parameter):
    try:
        return SkillModel.objects.filter(skiltype__name=parameter)
    except:
        return None


def index(request):
    site_title = get_general_setting("site_title")
    site_description = get_general_setting("site_description")
    site_keyword = get_general_setting("site_keyword")
    author_name = get_general_setting("author_name")
    author_job = get_general_setting("author_job")
    author_description = get_general_setting_description("author_description")

    # image setting
    icon = get_image_setting("icon")
    resim = get_image_setting("resim")
    logo = get_image_setting("logo")

    # skill setting
    backend = get_skill_setting("backend")
    frontend = get_skill_setting("frontend")
    devops = get_skill_setting("devops")
    other = get_skill_setting("other")

    # socials
    socials = SocialModel.objects.all()

    # documents
    documents = Document.objects.all()

    context = {
        "site_title": site_title,
        "site_description": site_description,
        "site_keyword": site_keyword,
        "author_name": author_name,
        "author_job": author_job,
        "author_description": author_description,
        "icon": icon,
        "resim": resim,
        "logo": logo,
        "backend": backend,
        "frontend": frontend,
        "devops": devops,
        "other": other,
        "socials": socials,
        "documents": documents,
    }
    return render(request, "pages/index.html", context=context)


def get_cv(request, slug):
    doc = get_object_or_404(Document, slug=slug)
    return redirect(doc.document.url)


def contact_message(request):
    if request.POST:
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            name = contact_form.cleaned_data.get("name")
            email = contact_form.cleaned_data.get("email")
            subject = contact_form.cleaned_data.get("subject")
            message = contact_form.cleaned_data.get("message")

            Messages.objects.create(
                name=name, email=email, subject=subject, message=message
            )
            # mesaj buraya eklenecek.
            contact_form.send_email()
            success = True
            message = "Mesajınız başarıyla gönderildi."
        else:
            success = False
            message = " Tekrar deneyiniz."
    context = {
        "success": success,
        "message": message,
    }
    return JsonResponse(context)
