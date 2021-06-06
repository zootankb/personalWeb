import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.forms.models import model_to_dict
from django.views.static import serve

from local_struct import CJSONEncoder
from local_struct.page_data import PageData
from local_struct.result_client import ResultClient
from personalWeb.settings import MEDIA_ROOT, MEDIA_DIR, MEDIA_URL
from .models import *
import math

# Create your views here.
'''
页面使用的接口
'''


def index(request):
    photos = get_photo_by_page()
    return render(request, 'photoWeb/index.html', {'photos': photos})


def grid(request):
    photos = get_photo_by_page()
    return render(request, 'photoWeb/grid.html', {'photos': photos})


def masonry(request):
    photos = get_photo_by_page()
    return render(request, 'photoWeb/masonry.html', {'photos': photos})


def get_photo_page(request):
    if request.method == "GET":
        pageNumber = int(request.GET.get('pageNumber', 1))
        pageSize = int(request.GET.get('pageSize', 9))
        res = get_photo_by_page(pageNumber, pageSize)
        total_page = math.ceil(len(Blog.objects.all()) / pageSize)
        data = PageData(pageNumber, pageSize, total_page, res)
        data = json.dumps(data, default=lambda obj:obj.__dict__, sort_keys=True, indent=4, ensure_ascii=False)
        print(pageNumber)
        return HttpResponse(data)
    else:
        return HttpResponse(None)


def blog(request):
    data = {}
    blog_data = get_blog_by_page()
    data["blogs"] = blog_data
    data["categories"] = get_blog_to_num_by_categories()
    data["recent_imgs"] = get_recent_8_img()
    data["recent_cameraman"] = get_blog_by_page()

    return render(request, 'photoWeb/blog.html', {'data': data})


def get_blog_page(request):
    if request.method == "GET":
        pageNumber = int(request.GET.get('pageNumber', 1))
        pageSize = int(request.GET.get('pageSize', 3))
        res = get_blog_by_page(pageNumber, pageSize)
        total_page = math.ceil(len(Blog.objects.all()) / pageSize)
        data = PageData(pageNumber, pageSize, total_page, res)
        data = json.dumps(data, default=lambda obj: obj.__dict__, sort_keys=True, indent=4, ensure_ascii=False)
        return HttpResponse(data)
    return None


def single_post(request):
    get_recent_7_month_blog()
    if not request.GET.get('id'):
        if len(Blog.objects.all()) > 0:
            blog = Blog.objects.first()
            blog_dic = model_to_dict(blog)
            blog_dic['created_at'] = blog.created_at.strftime('%Y-%m-%d')
            blog_dic['cameraman'] = Cameraman.objects.get(id=blog_dic['cameraman']).name
            blog_dic['category'] = Category.objects.get(id=blog_dic['category']).name
            data = {}
            data['blog'] = blog_dic
            data["categories"] = get_blog_to_num_by_categories()
            data["recent_imgs"] = get_recent_8_img()
            data["recent_cameraman"] = get_blog_by_page()
            return render(request, 'photoWeb/single-post.html', {'data': data})
        else:
            return HttpResponse(None)
    else:
        blog_id = int(request.GET['id'])
        blog = Blog.objects.get(id=blog_id)
        blog_dic = model_to_dict(blog)
        blog_dic['created_at'] = blog.created_at.strftime('%Y-%m-%d')
        blog_dic['cameraman'] = Cameraman.objects.get(id=blog_dic['cameraman']).name
        blog_dic['category'] = Category.objects.get(id=blog_dic['category']).name
        data = {}
        data['blog'] = blog_dic
        data["categories"] = get_blog_to_num_by_categories()
        data["recent_imgs"] = get_recent_8_img()
        data["recent_cameraman"] = get_blog_by_page()
        return render(request, 'photoWeb/single-post.html', {'data': data})


def about(request):
    return render(request, 'photoWeb/about.html')


def get_message_from_user(request):
    """
    POST方式获取用户上传的消息
    :param request:
    name, email, message
    :return:
    true: 上传成功， false: 上传失败
    """
    res = False
    print('message')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            res = True
            fd = FeedBack(name = name, email = email, message = message)
            fd.save()
            print(fd)
    return HttpResponse(json.dumps({'result': res}))


@csrf_exempt
def post_photo_blog_from_user(request):
    """
    上传blog日志
    :param request:
    :return:
    """
    res = 'Fail'
    if request.method == 'POST':
        category = Category.objects.get(id = int(request.POST.get('category')))
        cameraman = Cameraman.objects.get(id = int(request.POST.get('cameraman')))
        title = request.POST.get('title')
        description = request.POST.get('description')
        content = request.POST.get('content')
        imgLevel1 = request.FILES.get('imgLevel1')
        imgLevel2 = request.FILES.get('imgLevel2')
        imgLevel3 = request.FILES.get('imgLevel3')
        b = Blog()
        b.category = category
        b.cameraman = cameraman
        b.title = title
        b.description = description
        b.content = content
        b.imgLevel1 = imgLevel1
        b.imgLevel2 = imgLevel2
        b.imgLevel3 = imgLevel3
        b.save()
        res = 'Succ'
    return HttpResponse(res)


def get_all_categories(request):
    """
    获取所有的风格信息
    :param request:
    :return:
    """
    rc = ResultClient()
    if request.method == 'GET':
        categories = Category.objects.values()
        rc.result = list(categories)
    else:
        rc.code = 50
        rc.msg = '请求方式错误'
    return JsonResponse(json.dumps(rc.__dict__, cls=CJSONEncoder.CJSONEncoder),safe=False)


def get_all_cameras(request):
    """
    获取所有的摄影师信息
    :param request:
    :return:
    """
    rc = ResultClient()
    if request.method == 'GET':
        cameras = Cameraman.objects.values()
        rc.result = list(cameras)
    else:
        rc.code = 50
        rc.msg = '请求方式错误'
    return HttpResponse(json.dumps(rc.__dict__, cls=CJSONEncoder.CJSONEncoder),safe=False)


'''
逻辑操作
'''


def get_photo_by_page(page_num=1, page_size=9):
    photos = Blog.objects.values_list('id', 'imgLevel1', 'title', 'category', 'description')
    p = list(photos)
    if photos:
        start_num = (page_num - 1) * page_size
        end_num = page_num * page_size
        if len(p) >= start_num:
            if len(p) >= end_num:
                pass
            else:
                end_num = len(p)
        else:
            return None
        p = p[start_num:end_num]
        keys = ['id', 'imgLevel1', 'title', 'category', 'description']
        dic = [dict(zip(keys, item)) for item in p]
        for item in dic:
            item['category'] = Category.objects.get(id=item['category']).name
        return dic
    return None


def get_blog_by_page(page_num=1, page_size=3):
    photos = Blog.objects.values_list('id', 'imgLevel1', 'imgLevel2','imgLevel3', 'cameraman', 'category', 'title', 'content', 'created_at')
    p = list(photos)
    if photos:
        start_num = (page_num - 1) * page_size
        end_num = page_num * page_size
        if len(p) >= start_num:
            if len(p) >= end_num:
                pass
            else:
                end_num = len(p)
        else:
            return None
        p = p[start_num:end_num]
        keys = ['id', 'imgLevel1', 'imgLevel2','imgLevel3', 'cameraman', 'category', 'title', 'content', 'created_at']
        dic = [dict(zip(keys, item)) for item in p]
        for item in dic:
            item['category'] = Category.objects.get(id=item['category']).name
            item['cameraman'] = Cameraman.objects.get(id=item['cameraman']).name
            item['created_at'] = item['created_at'].strftime('%Y-%m-%d')
        return dic
    return None


def get_blog_to_num_by_categories():
    """
    获取每个风格的名字以及对应的数量
    [{"id":id, "category":category,"num":num}, ...]
    """
    categories = Category.objects.all()
    categories_list = []
    for item in categories:
        num = Blog.objects.filter(category__id=item.id).count()
        dic = {}
        dic['id'] = item.id
        dic["category"] = item.name
        dic["num"] = num
        categories_list.append(dic)
    return categories_list


def get_recent_8_img():
    """
    获取最近的8张图
    :return:
    imgLevel3
    """
    imgs = Blog.objects.values('id', 'imgLevel3')
    tar_imgs = []
    if imgs:
        if len(imgs) >= 8:
            tar_imgs = list(imgs[:8])
        else:
            tar_imgs = list(imgs[:len(imgs)])
    return tar_imgs


def get_recent_7_month_blog():
    """
    获取前七个月的日志数量
    :return:
    [{}, ...]
    """
    date_arr = Blog.objects.values_list('created_at')
    date_dic = {}
    # for date_m_d in date_arr:
    #     key = date_m_d.strftime('%Y-%m-%d')
    #     if key not in date_dic.keys():
    #         date_dic[key]=key

    print(date_dic)
    return None

