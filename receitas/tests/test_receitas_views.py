from django.urls import reverse, resolve
from receitas import views
from .test_receitas_base import ReceitasTestBase


class ReceitasViewsTest(ReceitasTestBase):
    # Testes para a página HOME
    def test_receitas_home_view_esta_correta(self):
        view = resolve(reverse('receitas:home'))
        self.assertIs(view.func, views.home)

    def test_receitas_home_view_retorna_status_codigo_200_ok(self):
        response = self.client.get(reverse('receitas:home'))
        self.assertEqual(response.status_code, 200)

    def test_receitas_home_view_carrega_template_correto(self):
        response = self.client.get(reverse('receitas:home'))
        self.assertTemplateUsed(response, 'receitas/pages/home.html')

    def test_receitas_home_mostrar_receitas_nao_encontradas(self):
        # Receitas.objects.get(pk=1).delete()
        response = self.client.get(reverse('receitas:home'))
        self.assertIn(
            '<h1>Não há receitas para mostrar...</h1>',
            response.content.decode('utf-8')
        )

        # Aplicar para causar uma falha de propósito
        # self.fail('Para que eu possa terminar de digitá-lo!!!')

    def test_receitas_home_template_carrega_receitas(self):
        # Precisa de uma receita para fazer o teste
        self.faca_receita(autor_data={
            'first_name': 'Fábio'
        })
        response = self.client.get(reverse('receitas:home'))

        # Verificação por contexto
        # response_receitas = response.context['receitas']
        # self.assertEqual(response_receitas.first().titulo, 'Repolho Cremoso')

        # Verificação por conteúdo
        response_content = response.content.decode('utf-8')
        response_context_receitas = response.context['receitas']

        self.assertIn('Repolho Cremoso', response_content)
        self.assertIn('Fábio', response_content)
        self.assertIn('2 porções', response_content)
        self.assertEqual(len(response_context_receitas), 1)

    def test_receitas_home_nao_carrega_receitas_nao_publicadas(self):
        # Precisa de uma receita para fazer o teste
        self.faca_receita(esta_publicado=False)
        response = self.client.get(reverse('receitas:home'))

        self.assertIn(
            '<h1>Não há receitas para mostrar...</h1>',
            response.content.decode('utf-8')
        )

    # Testes para as CATEGORIAS DE RECEITAS
    def test_receitas_categoria_view_esta_correta(self):
        view = resolve(
            reverse('receitas:categoria', kwargs={'categoria_id': 1000})
        )
        self.assertIs(view.func, views.categoria)

    def test_receitas_categoria_view_retorna_404_se_nao_encontrar_receita(self):  # noqa: E501
        response = self.client.get(
            reverse('receitas:categoria', kwargs={'categoria_id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_receitas_categoria_template_carrega_receitas(self):
        titulo_necessario = 'Este é um teste de categoria'
        # Precisa de uma receita para fazer o teste
        self.faca_receita(titulo=titulo_necessario)
        response = self.client.get(reverse('receitas:categoria', args=(1,)))

        # Verificação por conteúdo
        response_content = response.content.decode('utf-8')

        self.assertIn(titulo_necessario, response_content)

    def test_receitas_categoria_nao_carrega_receitas_nao_publicadas(self):
        # Precisa de uma receita para fazer o teste
        receita = self.faca_receita(esta_publicado=False)
        response = self.client.get(
            reverse('receitas:receita', kwargs={'id': receita.categoria.id})
        )

        self.assertEqual(response.status_code, 404)

    # Testes para os DETALHES DE UMA RECEITA
    def test_receitas_receita_view_esta_correta(self):
        view = resolve(
            reverse('receitas:receita', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.receita)

    def test_receitas_receita_view_retorna_404_se_nao_encontrar_receita(self):
        response = self.client.get(
            reverse('receitas:receita', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_receitas_receita_template_carrega_a_receita_correta(self):
        titulo_necessario = 'Esta é uma página sobre modo de preparo - Carrega uma única receita'  # noqa: E501
        # Precisa de uma receita para fazer o teste
        self.faca_receita(titulo=titulo_necessario)
        response = self.client.get(
            reverse(
                'receitas:receita',
                kwargs={
                    'id': 1
                }
            ))

        # Verificação por conteúdo
        response_content = response.content.decode('utf-8')

        self.assertIn(titulo_necessario, response_content)

    def test_receitas_receita_nao_carrega_receita_nao_publicadas(self):
        # Precisa de uma receita para fazer o teste
        receita = self.faca_receita(esta_publicado=False)

        response = self.client.get(
            reverse(
                'receitas:receita',
                kwargs={
                    'id': receita.id
                }
            ))

        self.assertEqual(response.status_code, 404)

    def test_receitas_pesquisa_usando_a_view_correta(self):
        resolved = resolve(reverse('receitas:pesquisa'))
        self.assertIs(resolved.func, views.pesquisa)

    def test_receitas_pesquisa_carregue_o_template_correto(self):
        response = self.client.get(reverse('receitas:pesquisa') + '?q=teste')
        self.assertTemplateUsed(response, 'receitas/pages/pesquisa.html')

    def test_receitas_procura_sem_termo_levanta_um_404(self):
        url = reverse('receitas:pesquisa')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_receitas_termo_procurado_esta_no_titulo_da_pagina_e_com_escape(self):
        url = reverse('receitas:pesquisa') + '?q=<Teste>'
        response = self.client.get(url)
        self.assertIn(
            'Pesquisando por &quot;&lt;Teste&gt;&quot;',
            response.content.decode('utf-8')
        )
