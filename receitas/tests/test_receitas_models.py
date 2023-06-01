from .test_receitas_base import ReceitasTestBase, Receitas
from django.core.exceptions import ValidationError
from parameterized import parameterized


class ReceitaModelTest(ReceitasTestBase):
    def setUp(self) -> None:
        self.receita = self.faca_receita()
        return super().setUp()

    def test_faca_receita_sem_default(self):
        receita = Receitas(
            categoria=self.faca_categoria(nome='Almoço de Domingo'),
            autor=self.faca_autor(username='Bundinha Deliciosa'),
            titulo='Repolho Cremoso',
            descricao='Um delicioso repolho cremoso',
            slug='repolho-cremoso',
            tempo_preparo=15,
            unidade_tempo_preparo='Minutos',
            porcoes=2,
            unidade_porcoes='porções',
            modo_preparo='Modo de preparo do repolho cremoso',
        )
        receita.full_clean()
        receita.save()
        return receita

    @parameterized.expand([
        ('titulo', 65),
        ('descricao', 165),
        ('unidade_tempo_preparo', 65),
        ('unidade_porcoes', 65),
    ])
    def test_campos_da_receita_com_max_length(self, valor, max_length):
        setattr(self.receita, valor, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.receita.full_clean()

    def test_receita_campo_modo_preparo_html_default_false(self):
        receita = self.test_faca_receita_sem_default()
        self.assertFalse(
            receita.modo_preparo_html,
            msg='O campo modo de preparo deveria ser falso...'
        )

    def test_receita_campo_esta_publicado_default_false(self):
        receita = self.test_faca_receita_sem_default()
        self.assertFalse(
            receita.esta_publicado,
            msg='O campo esta_publicado deveria ser falso...'
        )
