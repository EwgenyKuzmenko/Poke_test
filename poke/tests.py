from django.test import TestCase, Client
from poke.models import PokemonModel
from django.contrib.auth.models import User
from django.urls.base import reverse
from unittest import mock


class RegisterAndChoiceTest(TestCase):
    def setUp(self):
        self.client = Client()
        test_user1 = User.objects.create_user(username='testuser1', password='testuser1')
        test_user1.save()
        test_user2 = User.objects.create_user(username='testuser2', password='testuser2')
        test_user2.save()

    def test_register_GET(self):
        response = self.client.get(reverse('poke:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_POST(self):
        self.client.post(reverse('poke:register'), {
            'username': 'demouser',
            'password1': 'Qazwsxedcrfv123456789',
            'password2': 'Qazwsxedcrfv123456789',
        })
        self.assertTrue(User.objects.get(username='demouser'))

    def test_coice(self):
        self.client.login(username='testuser1', password='testuser1')
        mock_data = mock.Mock(status_code=200, return_value={'pokemon': "testpoke"})
        self.client.get('/chosen/'+mock_data.return_value['pokemon'])
        self.assertTrue(PokemonModel.objects.get(pokemon='testpoke'))
