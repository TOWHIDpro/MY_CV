from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('enroll/', include('signup_user.urls')),

    # app section
    path('crud/', include('app.crud.urls')),
    path('password_generator', include('app.pass_gen.urls')),
    path('food-app', include('app.food.urls')),
    path('todo/', include('app.todo.urls')),

    # game section
    path('tic-tac-toe', include('game.tic_tac_toe.urls')),
    path('rock-paper-scissors', include('game.rock_paper_scissors.urls')),
    
    # web section
    path('photo-gallery/', include('web.photo_gallery.urls')),
    path('ecommerce/', include('web.ecommerce.urls')),
    path('blog/', include('web.blog.urls')),

    # Extra
    path('froala_editor/',include('froala_editor.urls'))
]
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)