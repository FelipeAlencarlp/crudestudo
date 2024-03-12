from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Produto


def cadastrar_produto(request):
    if request.method == "GET":
        return render(request, 'cadastrar_produto.html')
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')

        produto = Produto(
            nome=nome,
            preco=preco,
            quantidade=quantidade
        )

        produto.save()

        messages.add_message(request, messages.SUCCESS, 'Produto cadastrado com sucesso')
        return render(request, 'cadastrar_produto.html')
    
    
def listar_produtos(request):
    if request.method == "GET":
        nome = request.GET.get('nome')
        produtos = Produto.objects.all().order_by('nome')

        if nome:
            produtos = produtos.filter(nome__icontains=nome)

        return render(request, 'listar_produtos.html', {'produtos': produtos})


def visualizar_produto(request, id):
    if request.method == "GET":
        produto = Produto.objects.get(id=id)
        data = produto.__dict__

        return render(request, 'visualizar_produto.html', {'data': data})


def editar_produto(request, id):
    nome = request.POST.get('nome')
    preco = request.POST.get('preco')
    quantidade = request.POST.get('quantidade')

    produto = get_object_or_404(Produto, id=id)

    produto.nome = nome
    produto.preco = preco
    produto.quantidade = quantidade
    produto.save()

    return redirect(listar_produtos)


def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()

    messages.add_message(request, messages.SUCCESS, 'Produto deletado com sucesso')
    return redirect(listar_produtos)
