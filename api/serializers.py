from rest_framework import  serializers
from .models import Family,Children,Parent

class ChildrenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Children
        fields = ('family_id','name','age')

class ParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parent
        fields = ('family_id','name','age','gender')

class FamilySerializer(serializers.ModelSerializer):
    parent_data = ParentSerializer(many=True)
    children_data = ChildrenSerializer(many=True)

    class Meta:
        model = Family
        fields = ('id','name','parent_data','children_data')

    def create(self, validated_data):
        parents_data = validated_data.pop('parent_data')
        childrens_data = validated_data.pop('children_data')

        family = Family.objects.create(**validated_data)

        '''
            The above created family's id is used in creation of parent and 
            children data, as the family's id is needed to create them.
            where, Family's id is the foreign key to the Family class.
        '''

        for data in parents_data:
            Parent.objects.create(family_id=family.id,**data)

        for data in childrens_data:
            Children.objects.create(family_id=family.id,**data)

        return family

    def update(self,instance,validated_data):
        parents_data = validated_data.pop('parent_data') #this is updated data of parent
        childrens_data = validated_data.pop('children_data') #this is updated data of parent

        parents = list(instance.parent_data.all())  # this is instance data of parent
        children = list(instance.children_data.all())  # this is instance data of parent

        '''
            instance.parent_data.all() returns queryset which is converted to list to 
            pop one data in every loop (the code is few lines below)
            
        '''

        # updating the family data(the actual class)
        instance.name = validated_data.get('name',instance.name)
        instance.save()

        '''
            now we work on parents data
            as parent data is many to one to family, we can have parent of same family
            so for which we need iterable for both instance and updated data.
            
            Here the for loop iterate on updated validated data
            And the list "parents" has the instance which is popped in every loop.
            
        '''
        for data in parents_data:

            parent = parents.pop(0)

            parent.name = data.get('name',parent.name)
            parent.age = data.get('age',parent.age)
            parent.gender = data.get('gender',parent.gender)
            parent.save()

        '''
            It is same logic as of parents loop above.
        '''
        for data in childrens_data:

            child = children.pop(0)

            child.name = data.get('name',child.name)
            child.age = data.get('age',child.age)
            child.save()

        return instance


