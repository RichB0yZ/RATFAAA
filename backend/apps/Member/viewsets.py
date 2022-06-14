from rest_framework import viewsets

from .models import Member
from .serializers import MemberSerializer



class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

# Routers provide an easy way of automatically determining the URL conf.
