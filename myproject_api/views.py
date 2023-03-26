from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Date
from .serializers import DateSerializer, DateWithMonthNameSerializer, \
    RankingSerializer
from .permissions import Check_API_KEY_Auth
from django.db.models import Count
from . import services


class DateListApiView(APIView):

    def get(self, *args):
        dates = Date.objects.all()
        serializer = DateWithMonthNameSerializer(dates, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {'detail': 'Currently no date present.'}, status=status.HTTP_200_OK
        )

    def post(self, request):
        month, day = request.data.values()

        if Date.objects.filter(month=month, day=day).exists():
            return Response(
                {'detail': 'Provided date was already checked.'},
                status=status.HTTP_200_OK
            )
        data = {
            'month': month,
            'day': day,
            'fact': services.get_fact(month=month, day=day)
        }
        serializer = DateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DateDetailApiView(APIView):
    permission_classes = (Check_API_KEY_Auth,)

    def delete(self, request, date_id):
        if Date.objects.filter(id=date_id).exists():
            Date.objects.get(id=date_id).delete()
            return Response(
                {'detail': 'Date deleted!'}, status=status.HTTP_200_OK
            )
        return Response(
            {'detail': 'Date with provided id does not exist.'},
            status=status.HTTP_200_OK
        )


class PopularListApiView(APIView):

    def get(self, *args):
        data = Date.objects.values('month_name').annotate(
            days_checked=Count('*')).order_by('-days_checked')
        serializer = RankingSerializer(data=list(data), many=True)
        if serializer.is_valid() and serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {'detail': 'Currently no date available to present ranking.'},
            status=status.HTTP_200_OK
        )
