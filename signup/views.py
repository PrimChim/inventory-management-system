import random
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.


def signaction(request):
    if request.method == "POST":
        password = request.POST['password']
        try:
            validate_password(password)
        except ValidationError as e:
            # The password entered by the user is invalid
            # Handle the error here
            error_message = "Invalid password. Your password must contain at least 8 characters and should contain at least one uppercase letter, one lowercase letter, one digit, and one special character."
            context = {'error_message': error_message}
            return render(request, 'signup_page.html', context)
        else:
            context = {}
            # The password entered by the user is valid
            # Process the data here
            # Get the form data from the request
            full_name = request.POST['fullname']
            email = request.POST['email']

            cpassword = request.POST['cpassword']
            if cpassword.__eq__(password):
                context = {
                    'error_message': 'User account created successfully!!!'}
                # Create a new ImsAdmin instance with the form data
                hashed_password = make_password(password)
                user = User(username=full_name, email=email,
                            password=hashed_password, is_staff=1)

            # Save the new instance to the database
                status = user.save()
                return render(request, 'signup_page.html', context)
            else:
                error_message = "Password Mismatch!!"
                context = {'error_message': error_message}
                return render(request, 'signup_page.html', context)
    else:
        context = {}
        return render(request, 'signup_page.html', context)


# action for pages
def homeaction(request):
    return render(request, 'Home.html')


def aboutaction(request):
    return render(request, 'aboutus.html')


@login_required
def dashboardaction(request):
    return render(request, 'Dash.html')


@login_required
def inventorytrackaction(request):
    return render(request, 'inventorytrack.html')


@login_required
def change_password(request):

    if request.method == 'POST':

        old_password = request.POST.get('old_password')
        user = request.user
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid:
            if user.check_password(old_password):

                new_password = request.POST.get('new_password')
                confirm_password = request.POST.get('confirm_password')
                if new_password.__eq__(confirm_password):
                    try:
                        validate_password(new_password)
                    except ValidationError as e:
                        # The password entered by the user is invalid
                        # Handle the error here
                        error_message = "Invalid password. Your password must contain at least 8 characters and should contain at least one uppercase letter, one lowercase letter, one digit, and one special character."
                        context = {'error_message': error_message}
                        return render(request, 'Changepass.html', context)
                    else:
                        user.set_password(new_password)
                        user.save()
                        update_session_auth_hash(request, user)
                        return render(request, 'Changepass.html', {'error_message': 'Your password has been changed.'})
                else:

                    return render(request, 'Changepass.html', {'error_message': 'Password mismatch!!!'})
            else:
                return render(request, 'Changepass.html', {'error_message': 'Your old password was incorrect!!!'})

    return render(request, 'Changepass.html')


def verify_otp(request):
    pass


def forget_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        try:
            user = User.objects.get(email=email)
            print("two step")
        except User.DoesNotExist:
            print("step three")
            return render(request, 'forget_password.html', {"error_message": 'This email is not registered.'})

        # Generate and send OTP to user's email
        otp = str(random.randint(100000, 999999))
        # message = f'Your OTP for password reset is {otp}. Do not share it with anyone.'
        # send_mail('Password reset OTP', message,
        #           'your_email@example.com', [email], fail_silently=True)

        print("otp is: ", otp)
        print("user is : ", user)
        # Store the OTP in session and redirect to OTP verification page
        request.session['otp'] = otp
        request.session['user_id'] = user.id
        return redirect('verify_otp')

    return render(request, 'forget_password.html')
