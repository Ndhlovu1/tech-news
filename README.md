# A web application built to share Innovate, Inspiring News

## Project Screenshots
**ADMIN INTERFACE**
![Screenshot from 2023-07-22 00-03-21](https://github.com/Ndhlovu1/tech-news-blog/assets/46927702/9c8fa772-7a99-4a3b-9e68-a6cbcdc7cc2f)
**FRONT END**
![Screenshot from 2023-07-22 04-40-50](https://github.com/Ndhlovu1/tech-news-blog/assets/46927702/5881024c-a608-4a62-88e3-de4d5864f38c)

## Key Features To Implement:
Create the specific models and setting up the admin site for the blog

1. Share the stories to other users
2. Allow Commenting on the stories
3. Add a story tag functionality
4. Use the tags to create a recommendation system
5. Create a post feed
6. Add a search feature

## TECHNICAL INFORMATION
##### A Django Project is the main django installation with the Project Settings
##### A Django Application is often used to interact with the framework and provide specific functionalities.
An Example is a Website with multiple Functionalities such as :
1. A Blog
2. Wiki
3. Forum 

It can also be used by other projects

#### Converting THE MIGRATIONS INTO SQL
´´´shell
python manage.py sqlmigrate blog_app 0001
´´´

## QUERYSETS AND MANAGERS
### Querysets are essential for building any database driven applications

#### Implementing the Object Relational Mapper

NB: Open the Default Shell For Our Django Applications

```shell
python manage.py shell
```

```python
>>> from django.contrib.auth.models import User
>>> from blog_app.models import Post
>>> user = User.objects.get(username='phx')
>>> post = Post('title'='Post from the Terminal', slug='terminal-post', body='hello from term')
>>> post.save()
```

## Presenting data to the Application

1. Template Tags control the rendering of the template -> {% tag %}

2. Template Variables get replaced with values when the template is rendered -> {{ variable }}

3. Template filters allow you to modify variables for display -> {{ variable|filter }}
