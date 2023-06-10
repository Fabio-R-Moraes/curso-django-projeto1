from django.urls import reverse, resolve
from receitas import views
from .test_receitas_base import ReceitasTestBase


class ReceitasHomeViewsTest(ReceitasTestBase):
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
