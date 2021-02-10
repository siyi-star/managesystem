# course/adminx.py

import xadmin

from .models import Course, Lesson,Video, CourseResource,BannerCourse


class LessonInline(object):
    model = Lesson
    extra = 0

class CourseResourceInline(object):
    model = CourseResource
    extra = 0



#Course部分管理
class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_times','students','get_zj_nums','go_to']    #设置默认显示的字段
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']    #设置搜索
    list_filter = ['name','desc','detail','degree','learn_times','students']    #设置过滤
    model_icon = 'fa fa-book'    #设置图标
    ordering = ['-click_nums']    #倒序排列
    readonly_fields = ['click_nums']    #只读字段
    exclude = ['fav_nums']    #不显示的字段
    refresh_times = [3, 5]    #刷新频率，单位是秒
    style_fields = {"detail": "ueditor"}    # “课程详情”添加编辑功能



#轮播课程设置
class BannerCourseAdmin(object):
    '''轮播课程'''

    list_display = [ 'name','desc','detail','degree','learn_times','students']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = [ 'name','desc','detail','degree','learn_times','students']
    model_icon = 'fa fa-bookmark-o'
    ordering = ['-click_nums']
    readonly_fields = ['click_nums']
    exclude = ['fav_nums']
    is_execute = True
    inlines = [LessonInline,CourseResourceInline]



#章节设置
class LessonAdmin(object):
    '''章节'''

    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    #这里course__name是根据课程名称过滤
    list_filter = ['course__name', 'name', 'add_time']
    model_icon = 'fa fa-bookmark'      # 设置章节图标



#视频设置
class VideoAdmin(object):
    '''视频'''

    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']
    model_icon = 'fa fa-video-camera'     # 设置视频图标



#课程资源设置
class CourseResourceAdmin(object):
    '''课程资源'''

    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course__name', 'name', 'download', 'add_time']
    model_icon = 'fa fa-tasks'   # 设置“视频资源图标”






#将各个部分的管理器进行注册
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)





