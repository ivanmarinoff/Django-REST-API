from rest_framework import status
from rest_framework.views import APIView, Response
from . models import Item
from . serilizers import ItemSerializer


class DumpItAPI(APIView):
    def get(self, request):
        items = Item.objects.all()
        items_data = ItemSerializer(items, many=True).data
        response_data = {"datas": items_data}

        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get("name")
        Item.objects.create(name=name)
        response_data = {"response": f"Item {name} created"}
        return Response(response_data, status=status.HTTP_200_OK)

    def put(self, request):
        name = request.data.get("name")
        item = Item.objects.filter(id=id).first()
        if item is None:
            response_data = {"response": f"Item {name} not found"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        item.name = name
        item.save()
        response_data = {"response": f"Item {name} updated"}
        return Response(response_data, status=status.HTTP_200_OK)


    def delete(self, request):
        id = request.data.get("id")
        item = Item.objects.filter(id=id).first()
        if item is None:
            response_data = {"response": f"Item {id} not found"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        item.delete()
        response_data = {"response": f"Item {id} deleted"}
        return Response(response_data, status=status.HTTP_200_OK)