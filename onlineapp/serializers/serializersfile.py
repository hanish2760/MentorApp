


from rest_framework import serializers

from onlineapp.models import Student, College, MockTest1


class CollegeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)  # collegename
    location = serializers.CharField(max_length=64)
    acronym = serializers.CharField(max_length=8)
    contact = serializers.EmailField()
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return College.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.acronym = validated_data.get('acronym', instance.acronym)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.save()
        return instance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','dob','email','db_folder','dropped_out','college']




class MockTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockTest1
        fields = ['id','problem1','problem2','problem3','problem4','total']




class StudentDetailsSerializer(serializers.ModelSerializer):
    mocktest1 = MockTestSerializer()
    class Meta:
        model = Student
        fields = ('id','name','dob','email','db_folder','dropped_out','college','mocktest1')
# try this update function to update students details and amrks.
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name",instance.name)
        instance.dob = validated_data.get("dob",instance.dob)
        instance.email = validated_data.get("email",instance.email)
        instance.db_folder = validated_data.get("db_folder",instance.db_folder)
        instance.dropped_out = validated_data.get("dropped_out",instance.dropped_out)
        instance.college_id = validated_data.get("college_id", instance.college_id)


        mockdata = validated_data['mocktest1']
        if not hasattr(instance,'mocktest1'):
             # instance.mocktest1.id = 0
             # instance.mocktest1.problem1 = 0
             # instance.mocktest1.problem2 = 0
             # instance.mocktest1.problem3 = 0
             # instance.mocktest1.problem4 = 0
             # instance.mocktest1.total = 0
            mocktestData = {'problem1':0,'problem2':0,'problem3':0,'problem4':0,'total':0}
            mock = MockTest1.objects.create(students = instance , **mocktestData)
            setattr(instance,'mocktest1',mock)



        instance.mocktest1.problem1 = mockdata.get('problem1',instance.mocktest1.problem1)
        instance.mocktest1.problem2 = mockdata.get('problem1',instance.mocktest1.problem2)
        instance.mocktest1.problem3 = mockdata.get('problem1',instance.mocktest1.problem3)
        instance.mocktest1.problem4 = mockdata.get('problem1',instance.mocktest1.problem4)
        instance.mocktest1.total = instance.mocktest1.problem1 + instance.mocktest1.problem2 + instance.mocktest1.problem3 + instance.mocktest1.problem4
        instance.mocktest1.save()
        instance.save()

        return instance



# put authentication here ! JWT and BASIC Authentiation....how to do ?











