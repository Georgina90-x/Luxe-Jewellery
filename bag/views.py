from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the chosen product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    ringsize = None
# braceletsize = None
# necklacesize = None
    if 'ring_size' in request.POST:
        ringsize = request.POST['ring_size']
    bag = request.session.get('bag', {})

    """ Logic for adding sizes of rings to basket """
    if ringsize:
        if item_id in list(bag.keys()):
            if ringsize in bag[item_id]['items_by_ringsize'].keys():
                bag[item_id]['items_by_ringsize'][ringsize] += quantity
            else:
                bag[item_id]['items_by_ringsize'][ringsize] = quantity
        else:
            bag[item_id] = {'items_by_ringsize': {ringsize: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)