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
