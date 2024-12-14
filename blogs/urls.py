from django.urls import path

from blogs import views 


app_name = 'blogs'

urlpatterns = [
    #home page for the app blogs
    path('',views.index,name='index'),
    path('blogs_page/',views.blogs_page,name='blogs_page'),
    path('blogs_page/<int:blog_id>',views.blog_posts,name='blog_posts'),
    path('new_blog/',views.new_blog,name='new_blog'),
    path('new_post/<int:blog_id>/',views.new_post,name='new_post'),
    path('edit_post/<int:post_id>/',views.edit_post,name='edit_post'),
    path('delete_post/<int:post_id>/',views.delete_post,name='delete_post'),
    path('delete_blog/<int:blog_id>/',views.delete_blog,name='delete_blog'),
    
]