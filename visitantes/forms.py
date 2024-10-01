from django import forms
from .models import Visitante
from typing_extensions import Required


class VisitanteForm(forms.ModelForm):
    

    class Meta:
        model = Visitante
        fields = [
            'nome_completo',
            'cpf',
            'data_nascimento',
            'numero_casa',
            'placa_veiculo',
        ]

        error_menssages = {
            'nome_completo' : {
                'required' : 'O nome completo do visitante é obrigatório para o registro'
            },

            'cpf' : {
                'required' : 'O CPF é obrigatório para o registro'
            },

            'data_nascimento' : {
                'required' : 'Por favor, informe um formato válido para a data de nascimento'
            },

            'numero_casa' : {
                'required' : 'Por favor, informe o número da casa a ser visitada'
            },

            'placa_veiculo' : {
                'required' : 'Por favor, informe a placa do veículo corretamente.'
            },     
        }

class AutorizaVisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            'morador_responsavel',
        ]

        error_menssages = {
            'morador_responsavel' : {
                'required' : 'Por favor, informe o nome do morador responsável para o registro'
            },   
        }