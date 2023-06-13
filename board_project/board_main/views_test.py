from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

# get 요청시 html파일 그대로 return
def test_html(request):
    return render(request, 'test/test.html')

# get 요청시 html+data return
def test_html_data(request):
    my_name ="hongildong"
    return render(request, 'test/test.html',{'name' : my_name})

# get 요청시 html+multi data return
def test_html_multi_data(request):
    data = {'name': 'hongildong',
            'age' : 20
            }
    return render(request, 'test/test.html',{'data' : data})


# get 요청시 data만 return

def test_json_data(request):
    data = {'name': 'hongildong',
            'age' : 20
            }
    # render라는 의미는 웹개발에서 일반적으로 화면을 return 해줄때 쓰는 용어
    # 파이썬의 dict 유사한 json형태로 변환해서 return
    return JsonResponse(data)

# Query String
# 1. 필터링 된 조건으로 리소스에 접근해야할 때
# 2. 1:1 매핑이 안되는 모든 값
# 3. 가변적으로 변하는 리소스(검색 keyword, filter...)

# Pathvariable
# 1. 특정 인덱스나 고유값으로 리소스에 접근해야할 때
# # 2. 하나의 값으로 모든 리소스의 정보를 표현할 수 있는 값(pk)

# 사용자가 get요청으로 쿼리파라미터 방식 데이터를 넣어올때
# 사용자가 get요청으로 데이터를 넣어오는 2가지 방식
#  1) 쿼리파라미터 방식 : localhosst:8000/author?id=10&name=hongildong  // http://127.0.0.1:8000/
#  2) pathvariable 방식(좀 더 현대적인 방식): localhosst:8000/author/10
def test_html_parameter_data(request):
   id = request.GET.get('id')
   name = request.GET.get('name')
   print(id)
   print(name)
   return render(request, 'test/test.html',{})





def test_html_parameter_data(request):
   name = request.GET.get('name')
   email = request.GET.get('email')
   password = request.GET.get('password')
   data = {'name': name,
            'email' : email,
            'password' : password
            }
   return render(request, 'test/test.html',{"data":data})



def test_html_parameter_data2(request, my_id):
   print(my_id)
   return render(request, 'test/test.html',{})

#form 태그를 활용한 post방식
# 먼저 화면을 rendering 해주는 method

# def test_post_form(request):
#      return render(request, 'test/test_post_form.html')
    

def test_post_kim(request):
    if request.method == 'POST':
     name = request.POST['my_name']
     email = request.POST['my_email']
     password = request.POST['my_password']
     print(name + email + password)
     return redirect('/')   # localhost:8000/
    else:
     return render(request, 'test/test_post_form.html')