# def my_middlewear(get_response):
#     print('we initialize the middle wears')
#     def my_fn(request):
#         print('this will execute before view')
#         response=get_response(request)
#         print('this is after views')
#         return response
#     return my_fn

#now lets also see the class based middlewears
class my_middlewear:
    def __init__(self,get_response):
        self.get_response=get_response
        print('one time initialization')
        
    def __call__(self,request):
        print('this is before view')
        response=self.get_response(request)
        print('this is after view')
        return response