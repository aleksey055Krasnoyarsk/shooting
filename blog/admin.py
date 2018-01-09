from django.contrib import admin
from .models import Glavnaya
from .models import Post
from .models import About_federation
from .models import Regions
from .models import Referee
from .models import Instructor
from .models import Rukovodstvo
from .models import Inst_korpus
from .models import Sud_corpus
from .models import Uch_corpus
from .models import In_federation
from .models import Docx
from .models import Turnirs
from .models import Turnirs_result
from .models import Articles
from .models import Contacts

# Register your models here.

admin.site.register(Glavnaya)
admin.site.register(Post)
admin.site.register(About_federation)
admin.site.register(Regions)
admin.site.register(Referee)
admin.site.register(Instructor)
admin.site.register(Rukovodstvo)
admin.site.register(Inst_korpus)
admin.site.register(Sud_corpus)
admin.site.register(Uch_corpus)
admin.site.register(In_federation)
admin.site.register(Docx)
admin.site.register(Turnirs)
admin.site.register(Turnirs_result)
admin.site.register(Articles)
admin.site.register(Contacts)
