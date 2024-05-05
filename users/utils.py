import json
from rest_framework.views import APIView
from django.http import JsonResponse

from users.models import User

        




# class TeacherView(APIView):
#     def dispatch(self, request, *args, **kwargs):
        
        
       
#         token = request.headers.get('Authorization')

#         if token:
#             try:
                 
#                 user = Token.objects.filter(key=token).first()
#                 if user.user.role == 'Teacher':
#                     return self.post(self, *args, **kwargs)
#                 else:
#                     return JsonResponse({'error': 'Unauthorized'}, status=401)
#             except User.DoesNotExist:
#                 return JsonResponse({'error': 'Invalid token'}, status=401)
#         else:
#             return JsonResponse({'error': 'Unauthenticated User'}, status=401)
    
#     def get(self,request, *args, **kwargs):
        
#         raise NotImplementedError("Subclasses must implement handle_role method")
#     def post(self, *args, **kwargs):
        
#         raise NotImplementedError("Subclasses must implement handle_role method")
