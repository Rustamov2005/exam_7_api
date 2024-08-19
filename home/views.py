from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import filters
from rest_framework.decorators import action
from .models import Category, Commites, Company, UserLogin, Ideas, Articles, Team, Xizmatlar, Message
from .serializers import XizmatlarSerializer, CategorySerializer, CommitesSerializer, CompanySerializer, UserLoginSerializer, IdeasSerializer, ArticlesSerializer, TeamSerializer, MessageSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['yourname']

    def get_queryset(self):
        return Message.objects.all()


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        return Category.objects.all()

    """Bu yirda manashu kategoryadagi bo'sh ish o'rinlari soni."""
    @action(detail=True, methods=['GET'])
    def count(self, request, *args, **kwargs):
        categorys = self.get_queryset().order_by('-count')[:2]
        serializer = CategorySerializer(categorys, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    """Bu yirda qanday kategoryadagi ish o'rinlari bo'sh emas yani ishchilar yetarli."""
    @action(detail=True, methods=['GET'])
    def null_count(self, request, *args, **kwargs):
        categorys = self.get_queryset().order_by('count')[:2]
        serializer = CategorySerializer(categorys, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET", ])
    def to_draft(self, request, *args, **kwargs):
        artists = Category.objects.all()
        for artist in artists:
            artist.pb_to_df()
        return Response(data={"message": "All category drafft"})

    @action(detail=False, methods=["GET", ])
    def to_publish(self, request, *args, **kwargs):
        artists = Category.objects.all()
        for artist in artists:
            artist.df_to_pb()
        return Response(data={"message": "All category published"})


class CommitesViewSet(ModelViewSet):
    queryset = Commites.objects.all()
    serializer_class = CommitesSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'username']

    def get_queryset(self):
        return Commites.objects.all()

    """Bu actions orqali biz kommit necha marta ko'rilganligini bilishimiz mumkun."""

    @action(detail=True, methods=["GET", ])
    def seen(self, request, *args, **kwargs):
        commit = self.get_object()
        commit.seen += 1
        commit.save()
        return Response(data=commit.seen)

    """Bu action orqali eng ko'p ko'rilgan kommitlarni ko'rishimiz mumkun."""
    @action(detail=False, methods=["GET", ])
    def top(self, request, *args, **kwargs):
        commints = self.get_queryset().order_by('-seen')[:3]
        serializer = CommitesSerializer(commints, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET", ])
    def to_draft(self, request, *args, **kwargs):
        artists = Commites.objects.all()
        for artist in artists:
            artist.pb_to_df()
        return Response(data={"message": "All category drafft"})

    @action(detail=False, methods=["GET", ])
    def to_publish(self, request, *args, **kwargs):
        artists = Commites.objects.all()
        for artist in artists:
            artist.df_to_pb()
        return Response(data={"message": "All category published"})


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'google_accaunt', 'description']

    def get_queryset(self):
        return Company.objects.all()

    """Bu method orqali biz kompaniya nechayildan buyon ishlayotganligini bilishimiz mumkun."""

    @action(detail=True, methods=["GET", ])
    def seen(self, request, *args, **kwargs):
        company = self.get_object()
        company.seen += 1
        company.save()
        return Response(data=company.seen)

    @action(detail=False, methods=["GET", ])
    def to_draft(self, request, *args, **kwargs):
        artists = Company.objects.all()
        for artist in artists:
            artist.pb_to_df()
        return Response(data={"message": "All category drafft"})

    @action(detail=False, methods=["GET", ])
    def to_publish(self, request, *args, **kwargs):
        artists = Company.objects.all()
        for artist in artists:
            artist.df_to_pb()
        return Response(data={"message": "All category published"})


class UserLoginViewSet(ModelViewSet):
    queryset = UserLogin.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user']

    def get_queryset(self):
        return UserLogin.objects.all()

    @action(detail=False, methods=["GET", ])
    def to_draft(self, request, *args, **kwargs):
        artists = UserLogin.objects.all()
        for artist in artists:
            artist.pb_to_df()
        return Response(data={"message": "All category drafft"})

    @action(detail=False, methods=["GET", ])
    def to_publish(self, request, *args, **kwargs):
        artists = UserLogin.objects.all()
        for artist in artists:
            artist.df_to_pb()
        return Response(data={"message": "All category published"})


class IdeasViewSet(ModelViewSet):
    queryset = Ideas.objects.all()
    serializer_class = IdeasSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

    def get_queryset(self):
        return Ideas.objects.all()

    """Bu actions orqali biz 1 ideadan necha marta foydalanilganligini bilish mumkun."""

    @action(detail=True, methods=["GET", ])
    def seen(self, request, *args, **kwargs):
        idea = self.get_object()
        idea.seen += 1
        idea.save()
        return Response(data=idea.seen)

    """BU action orqali biz eng ko'p qo'llanilgan fikirni ko'ramiz."""
    @action(detail=False, methods=["GET", ])
    def top(self, request, *args, **kwargs):
        idea = self.get_queryset().order_by('-seen')[:3]
        serializer = IdeasSerializer(idea, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET", ])
    def to_draft(self, request, *args, **kwargs):
        artists = Ideas.objects.all()
        for artist in artists:
            artist.pb_to_df()
        return Response(data={"message": "All category drafft"})

    @action(detail=False, methods=["GET", ])
    def to_publish(self, request, *args, **kwargs):
        artists = Ideas.objects.all()
        for artist in artists:
            artist.df_to_pb()
        return Response(data={"message": "All category published"})


class ArticlesViewSet(ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'purpose']

    def get_queryset(self):
        return Articles.objects.all()

    """Bu action orqali maqolalar necha marta o'qilganini bilish mumkun."""

    @action(detail=True, methods=["GET", ])
    def seen(self, request, *args, **kwargs):
        article = self.get_object()
        article.seen += 1
        article.save()
        return Response(data=article.seen)

    @action(detail=False, methods=["GET", ])
    def to_draft(self, request, *args, **kwargs):
        artists = Articles.objects.all()
        for artist in artists:
            artist.pb_to_df()
        return Response(data={"message": "All category drafft"})

    @action(detail=False, methods=["GET", ])
    def to_publish(self, request, *args, **kwargs):
        artists = Articles.objects.all()
        for artist in artists:
            artist.df_to_pb()
        return Response(data={"message": "All category published"})


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'jobs', 'category']

    def get_queryset(self):
        return Team.objects.all()

    """Bu actions orqali biz xodimlar necha marta xizmat ko'rsatganligini bilishimiz mumkun."""

    @action(detail=True, methods=["GET", ])
    def seen(self, request, *args, **kwargs):
        team = self.get_object()
        team.count += 1
        team.save()
        return Response(data=team.count)

    """Bu action orqali ishchilarning ish staji haqida malumot olishimiz mumkun."""
    @action(detail=False, methods=["GET", ])
    def top(self, request, *args, **kwargs):
        team = self.get_queryset().order_by('-staj')[:3]
        serializer = TeamSerializer(team, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET", ])
    def to_draft(self, request, *args, **kwargs):
        artists = Team.objects.all()
        for artist in artists:
            artist.pb_to_df()
        return Response(data={"message": "All category drafft"})

    @action(detail=False, methods=["GET", ])
    def to_publish(self, request, *args, **kwargs):
        artists = Team.objects.all()
        for artist in artists:
            artist.df_to_pb()
        return Response(data={"message": "All category published"})


class XizmatlarViewSet(ModelViewSet):
    queryset = Xizmatlar.objects.all()
    serializer_class = XizmatlarSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'commit']

    def get_queryset(self):
        return Xizmatlar.objects.all()

    """Bu action orqali biz bir xizmatdan necha marta foydalanilganligini hisoblab boramiz."""

    @action(detail=True, methods=["GET", ])
    def seen(self, request, *args, **kwargs):
        xizmat = self.get_object()
        xizmat.count += 1
        xizmat.save()
        return Response(data=xizmat.count)

    """ bu actions orqali xizmatimiz qancha vaqt davom etishi haqida malumot olishimiz mumkun."""
    @action(detail=False, methods=["GET", ])
    def top(self, request, *args, **kwargs):
        xizmat = self.get_queryset().order_by('-time')[:3]
        serializer = XizmatlarSerializer(xizmat, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET", ])
    def to_draft(self, request, *args, **kwargs):
        artists = Xizmatlar.objects.all()
        for artist in artists:
            artist.pb_to_df()
        return Response(data={"message": "All category drafft"})

    @action(detail=False, methods=["GET", ])
    def to_publish(self, request, *args, **kwargs):
        artists = Xizmatlar.objects.all()
        for artist in artists:
            artist.df_to_pb()
        return Response(data={"message": "All category published"})