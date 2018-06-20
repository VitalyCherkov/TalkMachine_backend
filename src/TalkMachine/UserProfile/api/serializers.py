from rest_framework import serializers


from ..errors import EmailAlreadyInUse, UsernameAlreadyInUse
from ..constants import USERNAME_MAX_LENGTH, PASSWORD_MAX_LENGTH, INCORRECT_CREDENTIALS
from ..models import UserProfile


class UserLoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(source='user.email', required=True)
    password = serializers.CharField(source='user.password', write_only=True, required=True)

    username = serializers.CharField(source='user.username', read_only=True)
    bio = serializers.CharField(required=False, read_only=True)
    first_name = serializers.CharField(required=False, read_only=True)
    last_name = serializers.CharField(required=False, read_only=True)

    class Meta:
        model = UserProfile
        fields = (
            'email',
            'username',
            'password',
            'bio',
            'first_name',
            'last_name'
        )

    def validate(self, data):
        print('NOT VALIDATED DATA', data)

        try:
            user = self.Meta.model.objects.get_user_by_email(email=data['user']['email'])
        except UserProfile.DoesNotExist:
            raise serializers.ValidationError(INCORRECT_CREDENTIALS)

        valid = user.user.check_password(data['user']['password'])
        if not valid:
            raise serializers.ValidationError(INCORRECT_CREDENTIALS)

        self.instance = user

        return data


class UserSignupSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(source='user.email')
    username = serializers.CharField(max_length=USERNAME_MAX_LENGTH, source='user.username')
    password = serializers.CharField(max_length=PASSWORD_MAX_LENGTH,
                                     source='user.password', write_only=True)

    bio = serializers.CharField(required=False, read_only=True)
    first_name = serializers.CharField(required=False, read_only=True)
    last_name = serializers.CharField(required=False, read_only=True)

    class Meta:
        model = UserProfile
        fields = (
            'email',
            'username',
            'password',
            'bio',
            'first_name',
            'last_name'
        )

    def validate_email(self, value):
        try:
            user = self.Meta.model.objects.get_user_by_email(email=value)
        except UserProfile.DoesNotExist:
            return value

        error = EmailAlreadyInUse(value)
        raise serializers.ValidationError(code=error.code, detail=error.detail)

    def validate_username(self, value):
        try:
            user = self.Meta.model.objects.get_user_by_username(username=value)
        except UserProfile.DoesNotExist:
            return value

        error = UsernameAlreadyInUse(value)
        raise serializers.ValidationError(code=error.code, detail=error.detail)

    def create(self, validated_data):
        print('VALIDATED DATA: ', validated_data)

        return UserProfile.objects.create(
            email=validated_data['user']['email'],
            username=validated_data['user']['username'],
            password=validated_data['user']['password']
        )


class UserUpdateSerializer:
    pass


class UserMeSerializer:
    pass


class UserDetailsSerializer:
    pass


class UserShortSerializer(serializers.ModelSerializer):
    pass
