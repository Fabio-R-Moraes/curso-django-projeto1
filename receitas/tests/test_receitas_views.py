from django.urls import reverse, resolve
from receitas import views
from test_receitas_base import ReceitasTestBase, Receitas


class ReceitasViewsTest(ReceitasTestBase):
    # Testes para a página HOME
    def test_receitas_home_view_esta_correta(self):
        view = resolve(reverse('receitas-home'))
        self.assertIs(view.func, views.home)

    def test_receitas_home_view_retorna_status_codigo_200_ok(self):
        response = self.client.get(reverse('receitas-home'))
        self.assertEqual(response.status_code, 200)

    def test_receitas_home_view_carrega_template_correto(self):
        # Receitas.objects.get(pk=1).delete()
        response = self.client.get(reverse('receitas-home'))
        self.assertTemplateUsed(response, 'receitas/pages/home.html')

    def test_receitas_home_mostrar_receitas_nao_encontradas(self):
        # Receitas.objects.get(pk=1).delete()
        response = self.client.get(reverse('receitas-home'))
        self.assertIn(
            '<h1>Não há receitas para mostrar...</h1>',
            response.content.decode('utf-8')
        )

    def test_receitas_home_template_carrega_receitas(self):
        self.faca_receita()
        response = self.client.get(reverse('receitas-home'))

        # Verificação por contexto
        # response_receitas = response.context['receitas']
        # self.assertEqual(response_receitas.first().titulo, 'Repolho Cremoso')

        # Verificação por conteúdo
        response_content = response.content.decode('utf-8')
        response_context_receitas = response.context['receitas']

        self.assertIn('Repolho Cremoso', response_content)
        self.assertin('15 minutos', response_content)
        self.assertIn('2 porções', response_content)
        self.assertEqual(len(response_context_receitas), 1)

    # Testes para as CATEGORIAS DE RECEITAS

    def test_receitas_categoria_view_esta_correta(self):
        view = resolve(
            reverse('categoria', kwargs={'categoria_id': 1000})
        )
        self.assertIs(view.func, views.categoria)

    def test_receitas_categoria_view_retorna_404_se_nao_encontrar_receita(self):
        response = self.client.get(
            reverse('categoria', kwargs={'categoria_id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    # Testes para os DETALHES DE UMA RECEITA
    def test_receitas_receita_view_esta_correta(self):
        view = resolve(
            reverse('receitas-receita', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.receita)

    def test_receitas_receita_view_retorna_404_se_nao_encontrar_receita(self):
        response = self.client.get(
            reverse('receitas-receita', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)
