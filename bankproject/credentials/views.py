from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('form')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    return render(request, "login.html")


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'UserName Taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email Taken')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                print('User Created')
        else:
            messages.info(request, 'Password mismatch')
            return redirect('register')
        return redirect('login')
    return render(request, "register.html")


def logout(request):
    messages.success(request, 'Data entry was successful.')
    auth.logout(request)
    return redirect('form')

def logouttomenu(request):
    messages.success(request, 'Data entry was successful.')
    auth.logout(request)
    return redirect('demo')




def form(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        district = request.POST.get('district')
        branch = request.POST.get('branch')
        account_type = request.POST.get('account_type')
        materials = request.POST.get('materials')

        # Process the data as needed (you can save it to a database or perform other actions)

        # Redirect to a different page (e.g., 'logout')
        return redirect('logout')

    return render(request, 'form.html')
# def form(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         date_of_birth = request.POST['date_of_birth']
#         age = request.POST['age']
#         gender = request.POST['gender']
#         phone_number = request.POST['phone_number']
#         email = request.POST['email']
#         address = request.POST['address']
#         district = request.POST['district']
#         branch = request.POST['branch']
#         account_type = request.POST['account_type']
#         materials = request.POST['materials']
#         user = User.objects.create_user(first_name=first_name,
#                                         last_name=last_name,
#                                         date_of_birth=date_of_birth,
#                                         age=age,
#                                         gender=gender,
#                                         phone_number=phone_number,
#                                         email=email,
#                                         address=address,
#                                         district=district,
#                                         branch=branch,
#                                         account_type=account_type,
#                                         materials=materials,
#                                         )
#         user.save()
#         print('User Created')
#         return redirect('logout')
#
#     return render(request, "form.html")


def submit_data(request):
    messages.success(request, 'Data entry was successful.')

    return redirect('demo')
