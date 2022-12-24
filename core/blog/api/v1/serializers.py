from rest_framework import serializers
from blog.models import Post , Category
from accounts.models import Profile

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class PostSerializers(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    abs_url = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Post
        fields = ['id','title','author','category','content','status','category','abs_url','snippet','created_date','published_date',]
        read_only_fields = ['author']


    def get_abs_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.id)
    

    def to_representation(self, instance):
        request = self.context.get('request')
        rep =  super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet')
            rep.pop('abs_url')
        else :
            rep.pop('content')
        rep['category'] = CategorySerializers(instance.category,context={'request':request}).data
        return rep

    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)
