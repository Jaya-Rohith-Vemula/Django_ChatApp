from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import ChatBoard
# Create your views here.

# def homepage(request):
#     return HttpResponse("Hi")

# def home(request):
#     chatBoard = ChatBoard.objects.all()
#     chatBoard_names = list()

#     for board in chatBoard:
#         chatBoard_names.append(board.name)
    
#     response_html = '<br>'.join(chatBoard_names)

#     return HttpResponse(response_html)

def home(request):
    chatBoard = ChatBoard.objects.all()
    return render(request, 'home.html', {'chatBoard':chatBoard})

def board_topic(request, pk):
    chat_board = ChatBoard.objects.get(pk = pk)
    return render(request, 'chat_board_topics.html', {'chat_board':chat_board})
