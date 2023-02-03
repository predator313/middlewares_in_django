class Brother_middleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print('brother  initialization')
    
    def __call__(self,request):
        print('brother befor view')
        response=self.get_response(request)
        print('brother after view')
        return response

#now create the father middleware
class Father_middleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print('father initialization')

    def __call__(self,request):
        print('father before view')
        response=self.get_response(request)
        print('father after view')
        return response

#creating mother middleweare
class Mother_middleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print('mother initialization')
        
    def __call__(self,request):
        print('mother before view')
        response=self.get_response(request)
        print('mother after view')
        return response