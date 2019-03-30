from django.shortcuts import render  # 暂时没有作用
from django.http import HttpResponse  # 从http模块中导入HttpResponse类
from MyWeb import trans  # 导入翻译模块
from django.shortcuts import render  # 创建应用时自动导入的模块

# Create your views here.
def index(request):  # 定义站点首页视图函数
    return HttpResponse('啊！~~这是我的第一个网页！')  # 返回响应内容对象


def translate(request):  # 定义视图函数
    from_lang = request.GET['from_lang']  # 获取URL中的参数
    to_lang = request.GET['to_lang']  # 获取URL中的参数
    text = request.GET['words']  # 获取URL中的参数
    return HttpResponse(trans.trans(text, from_lang, to_lang))  # 返回响应内容对象


def translate2(request, words, from_lang, to_lang):  # 定义视图函数
    return HttpResponse(trans.trans(words, from_lang, to_lang))  # 返回响应内容对象


def index(request):  # 定义站点首页视图函数
    return render(request, 'index.html')  # 调用模板返回页面内容


def news_list(request, news_type):  # 定义新闻列表视图
    news_dict = {'economic': '经济', 'sport': '体育'}  # 创建参数字典
    return render(request, 'news_list.html', {'news_type': news_dict[news_type]})  # 整合数据并返回页面内容


def fiter_test(request):
    return render(request, 'filter.html', {'letters': 'abc', 'number': 1})


def news_list(request, news_type):
    news_dict = {'economic': '经济', 'sport': '体育'}
    news_titles = []
    if news_type == 'economic':
        news_titles = [('12/5', '作者成为全国首富。'), ('12/4', '作者成为全省首富。'),
                       ('12/3', '作者成为全市首富。'), ('12/2', '作者成为全镇首富。'), ('12/1', '作者成为全村首富。')]
    return render(request, 'news_list.html', {'news_type': news_dict[news_type], 'news_titles': news_titles})


