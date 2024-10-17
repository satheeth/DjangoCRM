from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, RecordSerializer
from .models import Record
from rest_framework.permissions import IsAuthenticated  

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"registered Successfully", "Users":serializer.data}, status = status.HTTP_201_CREATED)
        return Response({"status":"Error", "data":serializer.data}, status = status.HTTP_400_BAD_REQUEST)
    
class AddRecord(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = RecordSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Success", "Record":serializer.data}, status = status.HTTP_201_CREATED)
        return Response({"status":"Error", "Record":serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
class GetRecord(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        result = Record.objects.all()
        serializer = RecordSerializer(result, many = True)
        return Response({"status":"Success", "Record":serializer.data}, status = 200)
    
class DetailedRecord(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        try:
            record = Record.objects.get(id=id)
            serializer = RecordSerializer(record)
            return Response({"status": "success", "Record": serializer.data}, status= status.HTTP_200_OK)
        except:
            return Response({"status":"Error", "message": "Record Does'nt Found"}, status= status.HTTP_404_NOT_FOUND)
    
class DeleteRecord(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, id):
        result = Record.objects.get(id=id)
        result.delete()
        serializer = RecordSerializer(result)
        return Response({"status":"Success", "Record":serializer.data}, status = 200)
    
class UpdateRecord(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        try:
            result = Record.objects.get(id=id)
        except Record.DoesNotExist:
            return Response({"status": "Error", "message": "Record Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = RecordSerializer(result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Success", "Record": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "Error", "Data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


