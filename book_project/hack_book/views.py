from django.shortcuts import render
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
import json
# from hack_book.models import UserProfile
#
# # Create your views here.

def index(request):
    articles = [
        {"num": 137, "title":"논리회로", "img_url":"http://image.kyobobook.co.kr/images/book/medium/603/m9788970508603.jpg", 'price':"17000"},
        {"num": 138, "title":"광고학", "img_url":"https://books.google.co.kr/books/content?id=qZhwAgAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&imgtk=AFLRE71PVHoERkp4dX21LsFfb_92pnRM4c30gWjZ95VJcZ2MaSRaYqLzHU4ANUHJRJAncVUMlEHEQCTlpMCcXGnMkLkjnuVyaNPb4CMarQfA_TpRYM4VVNzJQBnxjsi0mf-65_Aq0kN0", 'price':"20000"},
        {"num": 139, "title":"건축학개론", "img_url":"https://books.google.co.kr/books/content?id=no-HMQAACAAJ&printsec=frontcover&img=1&zoom=1&imgtk=AFLRE71pVnEGZE02kdksiQ_W4KqUSuX0ciEq00kZei2Ks7Zge54ys3SJiNel-FCvQW2mNTWp7XtgZD3O1La0Pb51xFQVsjsXulWYeLUjKSe8zJlJ1Wue9jX0ieYX6AaSbfOzAurrwD0B", 'price':"15000"},
        {"num": 140,"title":"유체역학", "img_url":"http://bimage.interpark.com/goods_image/0/4/0/7/261950407g.jpg", 'price':"11000"},
        {"num": 141,"title":"일반기계공학", "img_url":"https://books.google.co.kr/books/content?id=NzlzRQAACAAJ&printsec=frontcover&img=1&zoom=1&imgtk=AFLRE73VglMCmlSPw1XTZwqg1nIMY7Fa-Pn23B598Q92jIbRDeiALR9joo5Zgbe8xGOJIu07RhfxPB7Z5XX2HqevKqol3QS5osdFRl3b5z6QI1m2Aj_GiRgSWSX6R7_Aoj9wIzBp6E3y", 'price':"18000"},
        {"num": 142,"title":"논리학", "img_url":"https://books.google.co.kr/books/content?id=kF4xMgAACAAJ&printsec=frontcover&img=1&zoom=1&imgtk=AFLRE727aKW1eg9eShnEzuO-tV9Jb_SansBfahxq877EhcGz5Wu_SVIDbBPhd_g5LyriyCwNADcFv-og0TCv9x9EfSTxbu6-piMj0cJcgW3ccNUs4zuHvclCZK8dRZ7i_BMT23s1GE6d", 'price':"15000"},
        {"num": 143,"title":"헌법학", "img_url":"https://books.google.co.kr/books/content?id=v6QiRQAACAAJ&printsec=frontcover&img=1&zoom=1&imgtk=AFLRE7115mRzAhHnwFPu0RbqQ8grO0hi3m-w24wj6JQ0GiY4NfewVIlB-SSQV5aCaY7HiHtbwgGa8I-1WNW5ak7wW-qchs3IKoMkNfAZnpe1lAlrVHfycfzcO7hSFybtTcH8XiPvbGp2", 'price':"11500"},
        {"num": 144,"title":"세무학", "img_url":"https://books.google.co.kr/books/content?id=_ACwMQAACAAJ&printsec=frontcover&img=1&zoom=1&imgtk=AFLRE70HCIkZrXTA2lLs8-9pH7p1Cq-A4T2_PtQECcey4XIjU8rw18iHFd_4LcwSOS26LOTHWmwuLYif9Der5Ss5Nh0_RTFZ6gVBXLMsRfd_e-qzPjVBry4W8X6zu7mtva2dPN9W24zb", 'price':"20000"},
        {"num": 145,"title":"회계학원론", "img_url":"https://books.google.co.kr/books/content?id=hbz1MQAACAAJ&printsec=frontcover&img=1&zoom=1&imgtk=AFLRE71G7XbDE3u9xUeqLVjCLzhHx3WJ8VYjLmqyrZ7YuflqhG_W1ppQunTa-mqS0F_bNiUmxT_lEfKWsqTpH03A4ku_VLtHjueh7CryiaRuThC8s9aojV2QHoYNvkRf1aDSP-pPT4tB", 'price':"19000"},
        {"num": 146,"title":"C언어", "img_url":"http://image.kyobobook.co.kr/images/book/medium/282/m9791187345282.jpg", 'price':"9000"},


    ]

    return render(request, 'pages/index.html', {"articles": articles})
# def user_check(request):
#     user = request.GET["id"]
#     password = request.GET["password"]
#
#     user_pw=list(UserProfile.objects.filter(user_id=user).values('user_pw'))
#     print(user, password, password==user_pw)
#     return HttpResponse(json.dumps(True), content_type='application/json')
#
# def login_user(request):
#     if request.method == "POST":
#         user_id = request.POST['user']
#     request.session['user_id'] = user_id
#
#     #user = authenticate(username=user_id, password=password)
#
#     return redirect(reverse_lazy('Index'))