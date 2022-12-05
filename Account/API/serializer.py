from django.contrib.auth.models import User

from Account.models import Account
from rest_framework.serializers import Serializer,FileField,CharField,ImageField,ValidationError
class AccountSerializer(Serializer):
    firstname=CharField()
    lastname=CharField()
    email=CharField()
    imageuser=ImageField(required=False,allow_null=True)
    password=CharField()
    repassword=CharField()
    def validate(self, data):
        password=data.get('password')
        repassword=data.get('repassword')
        if repassword!=password:
            raise ValidationError('Passwords Are not Match')
        print(data.get('imageuser'))
        return data
    def validate_username(self,value):

        selected_username=User.objects.filter(username=value)
        if selected_username is True:
            raise ValidationError('Choose Another Username')
        print("Firstname")
        return value
    def validate_email(self,value):
        selected_email=User.objects.filter(email=value)
        if selected_email is True:
            raise ValidationError('Choose Another Email')
        return value
    def create(self,validated_data):
        print("Create User Function")
        if self.is_valid():
            firstname=self.validated_data['firstname']
            lastname=self.validated_data['lastname']
            email=self.validated_data['email']
            image=self.validated_data['imageuser']
            password=self.validated_data['password']
            creating_user=User.objects.create_user(

                username=firstname,
                password=password,
                first_name=firstname,
                email=email,
                last_name=lastname,
                is_staff=True
            )
            create_account=Account.objects.create(
                UserAccount_id=creating_user.id,
                ImageFile=image

            )
            print(self.validated_data['imageuser'])
        return self.validated_data
class LoginSerializer(Serializer):
    UserName=CharField()
    Password=CharField()
    def validate(self, data):
        username=data.get('username')
        password=data.get('password')
        selected_user=User.objects.filter(
            username=username,
            password=password
        ).first()
        if not selected_user:
            raise ValidationError('User Doesnt Exist')
        else:
            return True
