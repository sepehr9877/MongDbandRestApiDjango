from django.contrib.auth.models import User

from Account.models import Account
from rest_framework.serializers import ModelSerializer,SerializerMethodField,Serializer,FileField,CharField,ImageField,ValidationError

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'first_name', 'email', 'last_name']

class AccountSerializer(ModelSerializer):
    firstname=CharField()
    lastname=CharField()
    email=CharField()
    image=ImageField(required=False,allow_null=True)
    repassword=CharField(write_only=True)
    password=CharField(write_only=True)
    class Meta:
        model=Account
        fields=['firstname','lastname','email','image','repassword','password',]
    def validate(self, data):
        password=data.get('password')
        print(password)
        repassword=data.get('repassword')
        if password!=repassword:
            raise ValidationError('Passwords Conflict')
        print(data)
        return data
    def validate_email(self,value):
        selected_user=User.objects.filter(email=value).first()
        if selected_user:
            raise ValidationError('Choose Another Email')
        return value
    def create(self, validated_data):
        print("enter create")
        if self.is_valid():
            print("enter create")
            email, image, lastname, username = self.get_values(validated_data)
            print(email)
            password = validated_data['password']
            print(password)
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
            return validated_data

    def get_values(self, validated_data):
        image = validated_data['image'].encode('utf-8').strip()
        username = validated_data['firstname']
        email = validated_data['email']
        lastname = validated_data['lastname']
        return email, image, lastname, username

class UpdatingUserSerializer(AccountSerializer):
    repassword = None
    password = None
    class Meta:
        model=Account
        fields=['firstname','lastname','email','image']
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


