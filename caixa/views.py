from django.shortcuts import render
from estoque.models import Produto
from caixa.forms import *
from django.views.generic.list import ListView


class Pdv(ListView):
    model = Produto
    context_object_name = 'object_list'
    template_name = "pdv.html"

    def post(self, request, *args, **kwargs):
        context = {}
        context['object_list'] = Produto.objects.all()

        if request.method == 'POST':
            form = form_cadastra_prooduto(request.POST)
            if form.is_valid():
                form.save()
        return render(request, self.template_name, context=context)
