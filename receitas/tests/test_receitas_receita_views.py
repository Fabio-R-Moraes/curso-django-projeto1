from django.urls import reverse, resolve
from receitas import views
from .test_receitas_base import ReceitasTestBase


class ReceitasReceitaViewsTest(ReceitasTestBase):
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
