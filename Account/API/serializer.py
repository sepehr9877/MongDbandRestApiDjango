from django.contrib.auth.models import User

from Account.models import Account
from rest_framework.serializers import ModelSerializer,SerializerMethodField,Serializer,FileField,CharField,ImageField,ValidationError

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'first_name', 'email', 'last_name']
class AccountSerializer(ModelSerializer):
    repassword=CharField(write_only=True)
    password=CharField(write_only=True)
    UserAccount=UserSerializer()
    class Meta:
        model=Account
        fields=['ImageFile','repassword','UserAccount']
    def validate(self, data):
        password=data.get('password')
        repassword=data.get('repassword')
        if password!=repassword:
            raise ValidationError('Passwords Conflict')
        return data
    def validate_email(self,value):
        selected_user=User.objects.filter(email=value).first()
        if selected_user:
            raise ValidationError('Choose Another Email')
        return value
    def create(self, validated_data):
        if self.is_valid():
            email, image, lastname, username = self.get_values(validated_data)
            password = validated_data['password']
            create_user=User.objects.create(username=username,
                                            first_name=username,
                                            last_name=lastname,
                                            email=email,
                                            is_staff=True
                                            )
            create_user.set_password(password=password)
            create_account=Account.objects.create(
                UserAccount_id=create_user.id,
                ImageFile=image
            )
            return validated_data

    def get_values(self, validated_data):
        userdetail = validated_data['UserAccount']
        username = userdetail['first_name']
        email = userdetail['email']
        lastname = userdetail['last_name']
        image = validated_data['ImageFile']
        return email, image, lastname, username

class UpdatingUserSerializer(AccountSerializer):
    repassword = None
    password = None
    class Meta:
        model=Account
        fields=['ImageFile','UserAccount']
    def validate(self, data):return data
    def update(self, instance, validated_data):
        user=self.context['request'].user
        useridinstance=instance.UserAccount.id
        if (user.is_superuser or (user.id==useridinstance)):
            usernameinstance=instance.UserAccount.username
            email, image, lastname,username=self.get_values(validated_data)
            User.objects.filter(id=useridinstance).update(
                username=username,
                first_name=username,
                last_name=lastname,
                email=email
            )
            Account.objects.filter(UserAccount_id=useridinstance).update(
                ImageFile=image
            )
            return validated_data
        else:
            raise ValidationError("You have No Permission")
class LoginSerializer(Serializer):
    username=CharField()
    password=CharField()
    def validate(self, data):
        username=data.get('username')
        password=data.get('password')
        print(username,password)
        selected_user=User.objects.filter(
            username=username
        ).first()
        if not selected_user:
            raise ValidationError('User Doesnt Exist')
        else:
            return data
    def valdate_user(self):
        username=None
        password=None
        if self.is_valid():
            username=self.validated_data['username']
            password=self.validated_data['password']
        return username,password


