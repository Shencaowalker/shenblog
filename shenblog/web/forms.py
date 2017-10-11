from django import forms
import os
#这是定义一个在提交时使用的表单函数
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=255,min_length=5)
    summary = forms.CharField(max_length=255,min_length=5)
    head_img = forms.ImageField()
    category_id = forms.IntegerField()
    content = forms.CharField(min_length=10)

#这是定义一个在本地存储图片的函数，在views.py 使用
def  handle_uploaded_file(request,f):
    print("---->",f.name)
    base_img_upload_path="statics/bootstrap/imgs"
    user_path="%s/%s"%(base_img_upload_path,request.user.userprofile.id)
    if not os.path.exists(user_path):
        os.mkdir(user_path)

    with open('%s/%s' %(user_path,f.name),'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return "/static/imgs/%s/%s" %(request.user.userprofile.id,f.name)
