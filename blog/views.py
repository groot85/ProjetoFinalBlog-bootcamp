from django.shortcuts import render
# A view is a place where we put the "logic" of our application
def post_list (request):
    return render (request, 'blog/post_list.html',{})