
class A:
    def file_path(self, request, response=None, info=None, *, item=None):
        print(f'A: request={request}, response={response}, info={info}, item={item}')


class B(A):
    def file_path(self, request, response=None, info=None, *, item=None):
        print(f'B: request={request}, response={response}, info={info}, item={item}')
        path_standard = super().file_path(request, response, info)
        print(path_standard)


request_ = 'request'
response_ = 'response'
info_ = 'info'
item_ = 'item'

a = A()
b = B()

print(a, b)

# a.file_path(request_, response_, info_, item=item_)
# a.file_path(request_, response_, item=item_)
# a.file_path(request_, item=item_)
# a.file_path(request_)

a.file_path(request=request_, item=item_)

# b.file_path(request_, response_, info_, item=item_)
