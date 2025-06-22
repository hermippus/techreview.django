from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect

from techrev.forms import ReviewForm
from techrev.models import Review


def index(request):
    reviews = Review.objects.order_by('-created')
    return render(request, 'techrev/index.html', {'reviews': reviews})


def review_get(request, rev_id):
    review = get_object_or_404(Review, id=rev_id)
    return render(request, 'techrev/review_detail.html', {'review': review})


def lol(request):
    return render(request, "techrev/lol.html")

@staff_member_required(login_url='/admin/login/')
def review_create(request):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save()
        return redirect(review.get_absolute_url())
    return render(request, 'techrev/review_create.html', {'form': form})