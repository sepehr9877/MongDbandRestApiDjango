from django.contrib.auth.models import User

from Account.models import Account
from rest_framework.serializers import Serializer,CharField,ImageField,ValidationError
class AccountSerializer(Serializer):
    FirstName=CharField()
    LastName=CharField()
    Email=CharField()
    ImageUser=ImageField(allow_null=True,allow_empty_file=True,default=None)
    Password=CharField()
    Repassword=CharField()
    def validate(self, data):
        password=data.get('Password')
        repassword=data.get('Repassword')
        if repassword!=password:
            raise ValidationError('Passwords Are not Match')
        return password
    def validate_Firstname(self,value):

        selected_username=User.objects.filter(username=value).first()
        if selected_username is True:
            raise ValidationError('Choose Another Username')
        return value
    def validate_Email(self,value):
        selected_email=User.objects.filter(email=value)
        if selected_email is True:
            raise ValidationError('Choose Another Email')
        return value

    def create(self,validated_data):
        if self.is_valid():
            username=validated_data['FirstName']
            firstname=validated_data['FirstName']
            lastname=validated_data['LastName']
            email=validated_data['Email']
            image=validated_data['ImageUser']
            password=validated_data['Password']
            creating_user=User.objects.create_user(

                username=username,
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
            return create_account
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
