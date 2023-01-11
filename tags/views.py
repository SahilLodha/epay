from tags.models import Tags
from rest_framework import status
from rest_framework.views import APIView
from tags.serializer import TagSerializer
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


class TagsView(APIView):
    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        tags = Tags.objects.all()
        tags_serialized = TagSerializer(tags, many=True)
        return Response(tags_serialized.data, status=status.HTTP_200_OK)


class TagView(APIView):
    def put(self, request, id):
        try:
            tag = Tags.objects.get(id=id)
            serializer = TagSerializer(instance=tag, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        try:
            tag = Tags.objects.get(id=id)
            tag_serialized = TagSerializer(tag)
            return Response(tag_serialized.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            tag = Tags.objects.get(id=id)
            tag.delete()
            tag_serialized = TagSerializer(instance=tag)
            return Response(tag_serialized.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)