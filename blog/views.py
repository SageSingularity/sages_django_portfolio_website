from django.http import HttpResponse
from django.shortcuts import render


# The main landing page for the blog.
#
# The [render] method renders the Django Templates,
# and data can be passed in via the third variable
# which is a dictionary. The Template can then consume
# this dictionary and dynamically change what is
# delivered to the user.
def blog_landing_page(request):
    blogs = [
        {
            'title': 'Blog 1',
            'date': 'Jan 5th 2023',
            'slug': 'first-blog'},  # SEO Optimized / Human Readable
        {
            'title': 'Blog 2',
            'date': 'Jan 10th 2023',
            'slug': 'second-blog'  # SEO Optimized / Human Readable
        }
    ]
    return render(request, 'blog/index.html', {
        'show_blogs': True,
        'blogs': blogs,
    })


def blog_details(request, blog_slug):
    selected_blog = {
        'title': 'a first blog',
        'summary': 'The first of many blogs.'
    }
    return render(request, 'blogs/blog-details.html', {
        'selected_blog': selected_blog,
    })
