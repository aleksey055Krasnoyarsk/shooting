from django.shortcuts import render, get_object_or_404
from django.utils import timezone


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
# Create your views here.

def index(request):
    return render(request, 'blog/index.html', {})

def glavnaya(request):
    glav = get_object_or_404(Glavnaya)
    return render(request, 'blog/glavnaya.html', {'glav': glav})


def about_federation(request):
    ab_fed = get_object_or_404(About_federation)
    return render(request, 'blog/about_federation.html', {'ab_fed': ab_fed})



def regions(request):
    reg = get_object_or_404(Regions)
    return render(request, 'blog/regions.html', {'reg': reg})

def referee(request):
    ref = get_object_or_404(Referee)
    return render(request, 'blog/referee.html', {'ref': ref})

def instructor(request):
    instr = get_object_or_404(Instructor)
    return render(request, 'blog/instructor.html', {'instr': instr})







def rukovodstvo(request):
    ruk = get_object_or_404(Rukovodstvo)    
    return render(request, 'blog/rukovodstvo.html', {'ruk': ruk})


def inst_korpus(request):
    ins_kor = get_object_or_404(Inst_korpus)
    return render(request, 'blog/inst_korpus.html', {'ins_kor': ins_kor})


def sud_corpus(request):
    s_cor = get_object_or_404(Sud_corpus)
    return render(request, 'blog/sud_corpus.html', {'s_cor': s_cor})


def uch_corpus(request):
    u_cor = get_object_or_404(Uch_corpus)
    return render(request, 'blog/uch_corpus.html', {'u_cor': u_cor})


def in_federation(request):
    in_fed = get_object_or_404(In_federation)
    return render(request, 'blog/in_federation.html', {'in_fed': in_fed})





def docx(request):
    doc = get_object_or_404(Regions)
    return render(request, 'blog/docx.html', {'doc': doc})


def news(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/news_list.html', {'posts': posts})

def news_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/news_detail.html', {'post': post})





def turnirs(request):
    tur = get_object_or_404(Turnirs)
    return render(request, 'blog/turnirs.html', {'tur': tur})


def turnirs_result(request):
    tur_res = get_object_or_404(Turnirs_result)
    return render(request, 'blog/turnirs_result.html', {'tur_res': tur_res})

def articles(request):
    arts = Articles.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/articles_list.html', {'arts': arts})


def articles_detail(request, pk):
    art = get_object_or_404(Articles, pk=pk)
    return render(request, 'blog/articles_detail.html', {'art': art})


def contacts(request):
    cont = get_object_or_404(Contacts)
    return render(request, 'blog/contacts.html', {'cont': cont})


