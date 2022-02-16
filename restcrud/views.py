from django.shortcuts import render
from rest_framework import viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from restcrud.serializers import MoviesSerializer, RentalsSerializer, UsersSerializer
from restcrud.models import Movies, Rentals, Users


class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed/created/edited/deleted.
    """
    queryset = Users.objects.all().order_by('id')
    serializer_class = UsersSerializer
    update_data_pk_field = 'id'

    def create(self, request, *args, **kwargs):
        kwarg_field: str = self.lookup_url_kwarg or self.lookup_field
        self.kwargs[kwarg_field] = request.data[self.update_data_pk_field]

        try:
            return self.update(request, *args, **kwargs)
        except Http404:
            return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class MoviesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed/created/edited/deleted.
    """
    queryset = Movies.objects.all().order_by('name')
    serializer_class = MoviesSerializer
    update_data_pk_field = 'name'

    def create(self, request, *args, **kwargs):
        kwarg_field: str = self.lookup_url_kwarg or self.lookup_field
        self.kwargs[kwarg_field] = request.data[self.update_data_pk_field]

        try:
            return self.update(request, *args, **kwargs)
        except Http404:
            return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class RentalsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed/created/edited/deleted.
    """
    queryset = Rentals.objects.all().order_by('id')
    serializer_class = RentalsSerializer
    update_data_pk_field = 'id'

    """def create(self, request, *args, **kwargs):
        kwarg_field: str = self.lookup_url_kwarg or self.lookup_field
        self.kwargs[kwarg_field] = request.data[self.update_data_pk_field]

        try:
            return self.update(request, *args, **kwargs)
        except Http404:
            return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
"""