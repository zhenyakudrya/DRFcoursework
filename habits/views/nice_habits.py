from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import NiceHabit
from habits.paginations import HabitsPagination
from habits.serializers.nice_habits import NiceHabitSerializer
from users.permissions import IsOwner


class NiceHabitCreateAPIView(CreateAPIView):
    """Класс для создания новых привычек"""
    serializer_class = NiceHabitSerializer
    queryset = NiceHabit.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_nice_habit = serializer.save()
        new_nice_habit.owner = self.request.user
        new_nice_habit.save()


class NiceHabitListAPIView(ListAPIView):
    """Класс для получения списка привычек"""
    serializer_class = NiceHabitSerializer
    queryset = NiceHabit.objects.all()
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        nice_habits_list = super().get_queryset()
        return nice_habits_list.filter(owner=user)


class NiceHabitDetailAPIView(RetrieveAPIView):
    """Класс для получения конкретной привычки"""
    serializer_class = NiceHabitSerializer
    queryset = NiceHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class NiceHabitUpdateAPIView(UpdateAPIView):
    """Класс для обновления конкретной привычки"""
    serializer_class = NiceHabitSerializer
    queryset = NiceHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class NiceHabitDeleteAPIView(DestroyAPIView):
    """Класс для удаления конкретной привычки"""
    serializer_class = NiceHabitSerializer
    queryset = NiceHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]