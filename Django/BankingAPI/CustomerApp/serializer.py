from rest_framework import serializers
from CustomerApp.models import AccountType, ClientInfo

class AccountSerializer(serializers.ModelSerializer):
    class Meta :
        model = AccountType
        fields = ('AccountId', 'AccountKind')

class ClientSerializer(serializers.ModelSerializer):
    class Meta :
        model = ClientInfo
        fields = ('clientId',
            'ClientName',
            'ClientSurname',
            'ClientEmail',
            'ClientNumber',
            'ClientIdNumber',
            'ClientPassword',
            'Account'
        )
