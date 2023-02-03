def my_middlewears(get_response):
    print('we initialize the middle wears')
    def my_fn(request):
        print('this will execute before view')
        response=get_response(request)
        print('this is alfter views')
        return response
    return my_fn