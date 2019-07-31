from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from faker import Faker
from .forms import Blogpost
# Create your views here.
def index(request):
    '''
    blog = Blog.objects
    context = {'blog': blog}
    '''

   # blogs = Blog.objects

    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list,9)

    page = request.GET.get('page')

    posts = paginator.get_page(page)
    context = {'posts':posts}
    return render(request,'index.html',context)

def detail(request,blogid):
    blog = get_object_or_404(Blog, id = blogid)
    context = {'blog': blog}
    return render(request,'detail.html', context)

def new(request):
    return render(request,'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.description = request.GET['description']
    blog.pub_date = timezone.datetime.now()
    blog.save()

    return redirect('/blog/'+str(blog.id))

def faker(request):
    myfaker = Faker('ko_KR')
    for i in range(1,30):
        #myfaker.seed(i)  얘는 faker를 돌릴때마다 고정된 값을 생성하도록 해주는 애인데 이 경우에는 생성하자마자 저장을 해버리므로 굳이 seed를 사용해줄 필요는 없다.
        blog = Blog()
        blog.title = myfaker.name()
        blog.description = myfaker.address()
        blog.pub_date = timezone.datetime.now()

        blog.save()
    return redirect('index')

def new_form(request):
    if request.method =='POST':
        form = Blogpost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/blog/'+str(post.id))
    else:
        form = Blogpost()
        context = {'form': form}
        return render(request, 'new_form.html', context)
