# Healthy Bite

**Healthy Bite** is a blog designed to make it easier for users to discover, share, and manage healthy food recipes. Whether you're looking for nutritious meal ideas or want to contribute your own recipes, this platform offers an intuitive interface to explore a world of healthy eating.

Users can sign up, search for healthy recipes, add their own creations, and engage with others by liking and commenting on recipes. It’s the perfect place for food lovers to share their passion for nutritious and wholesome meals!

You can visit the live version of the blog here: [Healthy Bite](https://tgo-healthy-bite-bc4b5d66896a.herokuapp.com/)

![Site Mockup](docs/readme_images/mochup.png)

## Table of Contents


## User Experience (UX)

Visitors to Healthy Bite are health-conscious individuals who enjoy discovering new, nutritious recipes. They want to save time while also eating healthy, balanced meals. The platform allows users to easily search for, share, and save healthy recipes.


### User Stories

#### EPIC | User Profile
- As a User, I can sign up and log in to create, edit, and delete my recipes, as well as like and comment on others' recipes.
- As a User, I can see my login status and manage my account securely.

#### EPIC | Recipe Discovery
- As a User, I can search for healthy recipes.
- As a User, I can browse and like recipes to keep track of the ones I enjoy.
- As a User, I can view recipe details, including ingredients, preparation steps, and cooking time.

#### EPIC | Recipe Management
- As a User, I can add new recipes, including ingredients, cooking methods, and images.
- As a User, I can edit or delete my own recipes.
- As a User, I can manage my saved recipes in a personal space.

#### EPIC | Recipe Interaction
- As a User, I can like and comment on other users' recipes, helping to create a collaborative community.
- As a User, I can edit or delete my comments on others' recipes.

### Design

The website is designed to be visually appealing, with a calming and clean interface that encourages healthy living and mindful eating.

#### Colour Scheme

Colour palette from Coolors

![Colour Palette](docs/readme_images/colour%20scheme.png)

The site uses a soft, natural color palette featuring light blue, light green, and whites to reflect the healthy, organic theme of the platform.

#### Fonts
The primary font used is **Roboto**, used for headers and contents. A clean and modern font that enhance readability while providing a stylish look.


### Custom Error Pages
Custom error pages were designed for a better user experience, provinding them with butons to get them back to the site.

- 400 Bad Request - Oops! It seems there was an error with your request. Please check your input and try again
- 403 Page Forbidden - Sorry, you don't have permission to access this page.
- 404 Page Not Found - The page you're looking for doesn't exist.
- 500 Server Error - Something went wrong on our end. Please try again later.


## Features

### Future Features



## Deployment - Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

### Create the Heroku App:
- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
- On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
- Enter a unique and meaningful app name.
- Next select your region.
- Click on the Create App button

### Update Heroku Config Vars
Add the following Config Vars in Heroku:
- SECRET_KEY value 
- CLOUDINARY_URL
- PORT = 8000
- DISABLE_COLLECTSTATIC = 1

### Deploy

- NB: Ensure in Django settings, DEBUG is False
- Set up a Heroku account and create a new app.
- Attach the Heroku Postgres add-on for database support.
- Configure environment variables like `SECRET_KEY` and `DATABASE_URL`.
- Use `gunicorn` as the web server in the `Procfile`.
- Deploy the project via GitHub or manually using Heroku CLI.

## Forking this repository

1. Visit [Healthy Bite GitHub Repository](https://github.com/thiago-23/Healthy_Bite.git).
2. Click the "Fork" button in the top-right corner of the page.
3. Follow the instructions to fork the project.

## Cloning this repository

To clone this repository follow the below steps: 

1. Locate the repository at this link [Healthy Bite GitHub Repository](https://github.com/thiago-23/Healthy_Bite.git). 
2. Under **'Code'**, see the different cloning options, HTTPS, SSH, and GitHub CLI. Click the prefered cloning option, and then copy the link provided. 
3. Open **Terminal**.
4. In Terminal, change the current working directory to the desired location of the cloned directory.
5. Type **'git clone'**, and then paste the URL copied from GitHub earlier. 
6. Type **'Enter'** to create the local clone. 

## Languages

- Python
- HTML
- CSS
- Javascript

## Frameworks - Libraries - Programs Used

- [Django](https://www.djangoproject.com/): for backend functionality.
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): authentication library used to create the user accounts
- [PostgreSQL](https://www.postgresql.org/) for database management.
- [Heroku](https://dashboard.heroku.com/login) - for deployment.
- [Font Awesome](https://fontawesome.com/) - Used for icons.
- [GitHub](https://github.com/) - Used for version control and agile tool.
- [Google Fonts](https://fonts.google.com/) - Used to import and alter fonts on the page.
- [W3C](https://www.w3.org/) - Used for HTML & CSS Validation.
- [PEP8 Online](http://pep8online.com/) - used to validate all the Python code
- [Jshint](https://jshint.com/) - used to validate javascript
- [Coolors](https://coolors.co/) - Used to create colour palette.
- [Favicon](https://favicon.io/) - Used to create the favicon.
- [Lucidchart](https://lucid.app/documents#/dashboard) - used to create the database schema design
- [Summernote](https://summernote.org/): for rich text editing in forms.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to manage Django Forms
- [Cloudinary](https://cloudinary.com/): the image hosting service used to upload images
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/): for responsive design.and styling


## Credits

* [IStock](https://www.istockphoto.com/)
* [Font awesome](https://fontawesome.com/icons)
* [Iconmonstr](https://iconmonstr.com/?s=coffee)
* [Coolors](https://coolors.co/)
* [Google Fonts](https://fonts.google.com/)
* [Mockup Screenshot Generator](https://ui.dev/amiresponsive)
- [W3Schools](https://www.w3schools.com/)
- [Django Docs](https://docs.djangoproject.com/en/4.0/)
- [Bootstrap 4.6 Docs](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Stack Overflow](https://stackoverflow.com/)
- [Code Institute - Blog Walkthrough Project](https://github.com/Code-Institute-Solutions/Django3blog)

## Acknowledgments

Thanks to my mentor, Antonio for his advice and support during my project, and the Code Institute Slack community for their support.