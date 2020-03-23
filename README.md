# Django-To-Do-App

# To start user signup we need to make two model, once default User model with customize field & another is UserProfile model, where we put all of our need field about user profile.

# From default User Model we use " first_name, last_name, username, email, password1, password2" field

# From UserProfile model we make " bio, gender, phone, date_of_birth, address, city, country, profile_pic" field

# Next we will make username as slug


# UserProfile fieldtype

    bio = textfield 165
    gender = radio button
    phone = int15
    date_of_birth = int 8
    address = textfield 120
    city = charfiled 20
    country = charfiled 20
    profile_pic = imagefield

# 1. first we make SignupForm with our field
# 2. second disply this form at signup views & signup html template
# 3. third we make UserProfile Model with our field
# 4. four we create a model form of UserProfile
# 5. then display this form at signup views & signup template
# 6. save those two form at two model





# How to login?
# login views

def loginpage(request):
    # if request.user.is_authenticated:
    #     return redirect('user_list')
    # else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'pass ki vule gesen?')
        context = {}

        return render(request,'users/login.html',context)


# login.html code 

 {% for message in messages %}
                    <div class="alert success"> {{ message }} </div>
                {% endfor %}
               <form method="POST" action="">
                    {% csrf_token %}
						<div class="input-group mb-3">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-user"></i></span>
							</div>
							<input type="text" name="username" placeholder="Username..." class="form-control">
						</div>
						<div class="input-group mb-2">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-key"></i></span>
							</div>
								<input type="password" name="password" placeholder="Password..." class="form-control" >
						</div>

							<div class="d-flex justify-content-center mt-3 login_container">
				 				<input class="btn login_btn" type="submit" value="Login">
				   			</div>
                             
					</form>
