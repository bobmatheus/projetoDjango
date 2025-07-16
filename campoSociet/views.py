from django.shortcuts import render, redirect
from .models import Campo

def cadastrar_campo(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        valor_1h = request.POST.get('valor_1h')
        valor_1h30 = request.POST.get('valor_1h30')

        Campo.objects.create(
            nome=nome,
            valor_1h=valor_1h,
            valor_1h30=valor_1h30
        )

        #return redirect('reservar_campo')  # ou onde quiser redirecionar após salvar

    return render(request, 'campo_form.html')

def reservar_campo(request):
    total = None
    campo_selecionado = None
    duracao = None

    if request.method == 'POST':
        campo_id = request.POST.get('campo')
        duracao = request.POST.get('duracao')

        campo_selecionado = Campo.objects.get(id=campo_id)

        if duracao == '1h':
            total = campo_selecionado.valor_1h
        elif duracao == '1h30':
            total = campo_selecionado.valor_1h30

        # Aqui, ao invés de voltar pro form, renderiza a página de sucesso
        return render(request, 'reserva_sucesso.html')

    campos = Campo.objects.all()
    return render(request, 'reservar.html', {
        'campos': campos,
        'total': total,
        'campo_selecionado': campo_selecionado,
        'duracao': duracao,
    })