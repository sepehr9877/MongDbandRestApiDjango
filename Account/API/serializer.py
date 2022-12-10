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
    ImageFile=ImageField(allow_null=True,write_only=True,default=None)
    def validate(self, data):
        password=data.get('password')
        print(password)
        repassword=data.get('repassword')
        if password!=repassword:
            raise ValidationError('Passwords Conflict')
        return data
    def validate_ImageFile(self,data):
        return data
    def validate_email(self,value):
        selected_user=User.objects.filter(email=value).first()
        if selected_user:
            raise ValidationError('Choose Another Email')
        return value
    def create(self, validated_data):
        print('create')
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
            if create_account.ImageFile:
                self.validated_data['ImageFile']=str(request.build_absolute_uri(create_account.ImageFile.url))

            return create_account

    def get_values(self, validated_data):
        file=validated_data['ImageFile']
        username = validated_data['firstname']
        email = validated_data['email']
        lastname = validated_data['lastname']
        return email, file, lastname, username
class UpdatingUserSerializer(ModelSerializer):
    UserAccount=UserSerializer()
    class Meta:
        model=Account
        fields=['ImageFile','UserAccount']

    def validate(self, data):
        UserDetail=data['UserAccount']
        lastname=UserDetail['last_name']
        username=UserDetail['first_name']
        if len(username)<4:
            raise ValidationError("UserName is invalid please try another username")
        if not lastname:
            raise ValidationError("The LastName Field SHouldnt be Empty Field ")
        return data
    def update(self, instance, validated_data):
        user=self.context['request'].user
        useridinstance=instance.UserAccount.id
        usernameinstance=instance.UserAccount.username
        request=self.context['request']
        email, image, lastname,username=self.get_value(dictionary=self.validated_data)
        User.objects.filter(id=useridinstance).update(
            username=username,
            first_name=username,
            last_name=lastname,
            email=email
        )
        if image:
            Account.objects.filter(UserAccount_id=useridinstance).update(
                ImageFile=image
            )
        selected_account=Account.objects.filter(UserAccount_id=useridinstance).first()
        if selected_account.ImageFile:
           self.validated_data['ImageFile']=str(request.build_absolute_uri(selected_account.ImageFile.url))
        return selected_account
    def get_value(self, dictionary):
        file = dictionary['ImageFile']
        userdetail=dictionary['UserAccount']
        username = userdetail['first_name']
        email = userdetail['email']
        lastname = userdetail['last_name']
        return email, file, lastname, username

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


