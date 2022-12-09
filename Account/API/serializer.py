import os.path

from django.contrib.auth.models import User

from Account.models import Account
from rest_framework.serializers import ModelSerializer,SerializerMethodField,Serializer,FileField,CharField,ImageField,ValidationError
import  encodings
class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'first_name', 'email', 'last_name']

class AccountSerializer(Serializer):
    firstname=CharField(write_only=True)
    lastname=CharField(write_only=True)
    email=CharField(write_only=True)
    repassword=CharField(write_only=True)
    password=CharField(write_only=True)
    ImageFile=ImageField()
    def validate(self, data):
        password=data.get('password')
        print(password)
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
            request=self.context['url']
            create_user=User.objects.create_user(username=username,password=password,
                                                 first_name=username,
                                                 last_name=lastname,
                                                 email=email,
                                                 is_staff=True
                                                 )

            create_account=Account.objects.create(
                UserAccount_id=create_user.id,
                ImageFile=image
            )
            self.validated_data['ImageFile']=str(request.build_absolute_uri(create_account.ImageFile.url))
            return self.validated_data

    def get_values(self, validated_data):
        file=validated_data['ImageFile']
        username = validated_data['firstname']
        email = validated_data['email']
        lastname = validated_data['lastname']
        return email, file, lastname, username

class UpdatingUserSerializer(ModelSerializer):
    repassword = None
    password = None
    UserDetail=UserSerializer(many=True,write_only=True)
    class Meta:
        model=Account
        fields=['ImageFile','UserDetail']

    def setIntitialInstacne(self):
        id=self.context
        print(id)
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


