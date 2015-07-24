from django import forms
from blog.models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude =['post']


    def add_comment(request, pk):
        p = request.POST
        if p.has_key('body') and p['body']:
            author = 'Anonymous'
            if p['author']:
                author = p['author']
                comment = Comment(post=Post.objects.get(pk=pk))
                cf = CommentForm(p, instance=comment)
                cf.fields['author'].required = False
                comment = cf.save(commit=False)
                comment.author = author
                comment.save()
        return HttpResponseRedirect(reverse('blog/post.html', args=[pk]))
        
