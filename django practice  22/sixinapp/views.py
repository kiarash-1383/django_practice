from .models import Musician, Album
from django.views.generic import ListView , DetailView 


class MusicianListView(ListView):
    model = Musician
    template_name = "musician_list.html"
    context_object_name = "musicians"
    paginate_by = 1

    def get_queryset(self):
        return Musician.objects.order_by("name")

             

class AlbumDetailView(DetailView):
    
    
            model = Album
            template_name = "album_detail.html"

            def get_queryset(self):
       
               return Album.objects.filter(num_stars__gte=3)
          