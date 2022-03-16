from app.todo.models import Todo
from . serializers import TodoSerializer
from rest_framework import generics

class TodoList(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Todo.objects.filter(user=pk)
        return queryset                                  

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer