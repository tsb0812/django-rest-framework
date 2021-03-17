from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# To take advantage of the fact that our responses are no longer hardwired to a single content type let's add support for format suffixes to our API endpoints. Using format suffixes gives us URLs that explicitly refer to a given format, and means our API will be able to handle URLs such as http://example.com/api/items/4.json.

# urlpatterns = [
#     path('people/', views.people_list),
#     path('people/<int:pk>/', views.people_detail)
# ]

urlpatterns = [
    path('people/', views.PeopleList.as_view()),
    path('people/<int:pk>/', views.PeopleDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
