from rest_framework import status, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from cardapio.models import Prato
from .serializers import PratoSerializer, PratoNutriSerializer
from django.shortcuts import get_object_or_404

class PratoViewSet(viewsets.ModelViewSet):
 
    serializer_class = PratoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'valor')
    # lookup_field = 'id'

    def get_queryset(self):
        # id = self.request.query_params.get('id', None)
        # nome = self.request.query_params.get('nome', None)
        # valor = self.request.query_params.get('valor', None)
        queryset = Prato.objects.all()
        # if id:
        #     queryset = Prato.objects.filter(pk=id)
        # if nome:
        #     queryset = queryset.filter(nome__iexact=nome)
        # if valor:
        #     queryset = queryset.filter(valor__iexact=valor)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(PratoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PratoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PratoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        prato = get_object_or_404(queryset, id=pk)
        serializer = PratoNutriSerializer(prato)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        return super(PratoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PratoViewSet, self).partial_update(request, *args, **kwargs)
