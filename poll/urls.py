"""poll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from questions.views import (question_detail , 
save_question_result ,login_view , register_view ,
 dashboard ,create_poll , see_answers,
 
 simple_get,simple_post,register,login,register_contributor,update_password,edit_profile,
 all_contributors,all_tags,all_users,user_info,top5_contributors,total_questions_count,total_users_count,total_views_count,
 front_page_analytics,view_all_questions,view_search_questions,view_trending_questions,view_specific_question,
 add_question,add_answer,upvote_answer,upvote_question,tagwise_question,view_unanswered_questions
 )



urlpatterns = [
    path('' , login_view , name="login"),
    path('register/' , register_view , name="register_view"),
    path('dashboard/' , dashboard , name="dashboard"),
    path('create_poll/' , create_poll , name="create_poll"),
path('see_answers/' , see_answers , name="see_answers"),



    path('question/<question_uid>/' , question_detail , name="question_detail"),
    path('api/save_question_result/' , save_question_result),
    path('api/simpleget/', simple_get),
    path('api/simplepost/', simple_post),
    path('admin/', admin.site.urls),
    
    path('register',register),
	path('login',login),
	path('register_contributor',register_contributor),
	path('update_password',update_password),
	path('edit_profile',edit_profile),

	path('all_contributors',all_contributors),
	path('all_users',all_users),
	path('user_info',user_info),

	path('top5_contributors',top5_contributors),

	path('total_users_count',total_users_count),
	path('total_questions_count',total_questions_count),
	path('total_views_count',total_views_count),
	path('front_page_analytics',front_page_analytics),

    path('view_all_questions',view_all_questions),
    path('view_search_questions',view_search_questions),
    path('view_trending_questions',view_trending_questions),
    path('view_unanswered_questions',view_unanswered_questions),
	path('view_specific_question',view_specific_question),

	path('add_question',add_question),
	path('add_answer',add_answer),

	path('upvote_question',upvote_question),
	path('upvote_answer',upvote_answer),

	path('all_tags',all_tags),
	path('tagwise_question',tagwise_question),
]
