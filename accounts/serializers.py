from rest_framework import serializers
from .models import Account
from rest_framework.validators import UniqueValidator


class AccountSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=Account.objects.all(),
                message=["A user with that username already exists."],
            )
        ],
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=Account.objects.all(),
                message=["user with this email already exists."],
            )
        ],
    )
    password = serializers.CharField(write_only=True)

    def create(self, validated_data: dict) -> Account:
        return Account.objects.create_user(**validated_data)

    def update(self, instance: Account, validated_data: dict) -> Account:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = Account
        fields = ["id", "email", "username", "password", "is_superuser"]
