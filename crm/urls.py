from django.contrib.auth import views
from django.urls import include, path

app_name = 'crm'

urlpatterns = [
	path('', include('common.urls', namespace="common")),
	path('accounts/', include('accounts.urls', namespace="accounts")),
	path('leads/', include('leads.urls', namespace="leads")),
	path('contacts/', include('contacts.urls', namespace="contacts")),
	path('opportunities/', include('opportunity.urls', namespace="opportunities")),
	path('cases/', include('cases.urls', namespace="cases")),
	path('emails/', include('emails.urls', namespace="emails")),
	# path('planner/', include('planner.urls', namespace="planner")),
	path('logout/', views.logout, {'next_page': '/login/'}, name="logout"),
]
