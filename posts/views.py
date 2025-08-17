from django.shortcuts import render ,get_object_or_404,redirect
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from .models import Post,Comment
from django.http import JsonResponse
# Create your views here.


@login_required
def post_create(request):
    if request.method=="POST":
        form = PostCreateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()

    else:
        form = PostCreateForm(data=request.GET)
    return render (request,'posts/create.html',{'form':form})



def feed(request):
    posts = Post.objects.all().order_by('-created')
    logged_user = request.user
    return render(request,'posts/feed.html',{'posts':posts,'logged_user':logged_user})

# def like_post(request):
#     post_id= request.POST.get('post_id')
#     post = get_object_or_404(Post,id=post_id)


#     if request.user in post.liked_by.all():
#         post.liked_by.remove(request.user)
#         liked = False
#     else:
#         post.liked_by.add(request.user)
#         liked = True
    
#     # if post.liked_by.filter(id=request.user.id).exists():
#     #     post.liked_by.remove(request.user)
#     # else:
#     #     post.liked_by.add(request.user)

#     return redirect('feed')

@login_required
def like_post(request):
    """
    This view handles the AJAX request from the template.
    """
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        user = request.user
        
        if user in post.liked_by.all():
            post.liked_by.remove(user)
            liked = False
        else:
            post.liked_by.add(user)
            liked = True
        
        likes_count = post.liked_by.count()
        first_liker_username = ""
        
        if likes_count > 0:
            first_liker_username = post.liked_by.first().username

        # This JSON response sends all necessary data back to the JavaScript
        return JsonResponse({
            'liked': liked, 
            'likes_count': likes_count,
            'first_liker_username': first_liker_username
        })
    
    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def add_comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        comment_text = request.POST.get('comment_text')
        
        if comment_text: # Ensure comment is not empty
            post = get_object_or_404(Post, id=post_id)
            new_comment = Comment.objects.create(
                post=post,
                user=request.user,
                body=comment_text
            )
            
            # Return the new comment's data for the AJAX success function
            return JsonResponse({
                'status': 'ok',
                'user': new_comment.user.username,
                'profile_photo_url': new_comment.user.profile.photo.url,
                'body': new_comment.body,
                'created': new_comment.created.strftime('%b. %d, %Y, %I:%M %p') # Formatted time
            })
            
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)