from django.views.generic import View
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from bitly.models import Bitlink


class BitlinkCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                "bitly/new.html",
                {},
                )

    def post(self, request, *args, **kwargs):

        original_url = request.POST.get("original_url")

        bitlink = request.user.bitlink_set.create(
                original_url = original_url,
            )

        bitlink.save()

        return redirect(reverse("home"))

