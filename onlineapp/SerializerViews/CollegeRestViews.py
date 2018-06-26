
# view function!!
# class CollegeDetailsRestView(View):
#     def get(self,request, *args, **kwargs):
#         try:
#             col=College.objects.get(id=kwargs['pk'])
#             d=CollegeSerializer(col)
#
#         except:
#             return {}
#
#         return HttpResponse(json.dumps(dict(d.data)),content_type='application/json')
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from rest_framework.parsers import JSONParser

from onlineapp.serializers.serializersfile import CollegeSerializer
from onlineapp.models import College

from rest_framework.response import Response
@csrf_exempt
def CollegeListRestView(request):

    if request.method == 'GET':

        clg = College.objects.all()
        clglist=[]
        dictdata=dict()
        for c in clg:
            ser=CollegeSerializer(c)
            clglist.append(ser.data)
            dictdata[c.id]=ser.data
        # serializer = CollegeSerializer(clg, many=True)
        return JsonResponse(clglist,safe=False)
        #return Response(ser.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CollegeSerializer(data=request.POST)
        #CollegeSerializer.create(serializer)
        if (serializer.is_valid()):
            serializer.save()

            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse("Not Found", status=400)


#@api_view(['GET','PUT','DELETE'])
@csrf_exempt
def CollegeDetailsRestView(request,*args,**kwargs):

    id = kwargs['pk']
    if request.method == "GET":
        clg = College.objects.all().get(id = id)
        if(clg):
            serliazer = CollegeSerializer(clg)
            return JsonResponse(serliazer.data)
        else:
            return JsonResponse({'error':'403'},status = status.HTTP_403_FORBIDDEN)

    elif request.method == "PUT":
        data=JSONParser().parse(request)
        clg = College.objects.all().get(id=id)
        #why not this ?
        #serializer = CollegeSerializer(clg,data=request.data)
        serializer = CollegeSerializer(clg, data=data)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        College.objects.get(id=id).delete()


# @api_view(['GET','PUT','DELETE'])
@csrf_exempt
def test(request,*args,**kwargs):
    if request.method == "POST":
        print("hello there")
        return HttpResponse({"ok": "dengei"}, status=status.HTTP_201_CREATED)

