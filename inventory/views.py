import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserMasters
from .serializers import LoginSerializer
from .models import CategoryMasters
from .serializers import CategoryListSerializer
from .models import ProductMasters, DeptMasters, CategoryMasters
from .serializers import ProductAddSerializer, ProductListSerializer
from .models import ProductMasters
from django.utils import timezone
from django.db import connection
from .models import StorageMasters
from .serializers import StorageListSerializer
from .models import LocationMasters
from .serializers import LocationListSerializer
from .models import ProductImageMasters, ProductMasters
from .models import DeptMasters
from .serializers import DepartmentListSerializer

class LoginAPIView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        mobile = serializer.validated_data['mobile']
        password = serializer.validated_data['password']

        try:
            user = UserMasters.objects.get(mobile=mobile, password=password)
        except UserMasters.DoesNotExist:
            return Response(
                {'message': 'Invalid mobile or password'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        payload = {
            'userid': user.userid,
            'name': user.name,
            'role': user.role
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return Response({
            'message': 'Login successful',
            'token': token,
            'user': {
                'userid': user.userid,
                'name': user.name,
                'role': user.role
            }
        }, status=status.HTTP_200_OK)



class CategoryListAPIView(APIView):

    def get(self, request):
        categories = CategoryMasters.objects.all()
        serializer = CategoryListSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddProductAPIView(APIView):

    def post(self, request):
        serializer = ProductAddSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data

        if not DeptMasters.objects.filter(did=data['did']).exists():
            return Response(
                {"message": "Invalid department id"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not CategoryMasters.objects.filter(cid=data['cid']).exists():
            return Response(
                {"message": "Invalid category id"},
                status=status.HTTP_400_BAD_REQUEST
            )

        product = ProductMasters.objects.create(
            name=data['name'],
            quantity=data['quantity'],
            dimensions=data.get('dimensions'),
            cid=data['cid'],
            description=data.get('description'),
            did=data['did'],
            createat=timezone.now(),
            updateat=timezone.now()
        )

        return Response(
            {
                "message": "Product added successfully",
                "productid": product.productid
            },
            status=status.HTTP_201_CREATED
        )
    
class ProductListAPIView(APIView):

    def get(self, request):
        query = """
            SELECT
                p.productid,
                p.name,
                p.quantity,
                p.dimensions,
                p.description,
                c.name AS category_name,
                d.name AS department_name
            FROM product_masters p
            JOIN category_msters c ON p.cid = c.cid
            JOIN dept_masters d ON p.did = d.did
            ORDER BY p.productid DESC
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

        products = []
        for row in rows:
            products.append({
                "productid": row[0],
                "name": row[1],
                "quantity": row[2],
                "dimensions": row[3],
                "description": row[4],
                "category_name": row[5],
                "department_name": row[6],
            })

        return Response(products, status=status.HTTP_200_OK)
    

class StorageListAPIView(APIView):

    def get(self, request):
        storages = StorageMasters.objects.all().order_by('storageid')
        serializer = StorageListSerializer(storages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ProductImageUploadAPIView(APIView):

    def post(self, request):
        productid = request.POST.get('productid')
        images = request.FILES.getlist('images')

        if not productid:
            return Response(
                {"message": "productid is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not ProductMasters.objects.filter(productid=productid).exists():
            return Response(
                {"message": "Invalid productid"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not images:
            return Response(
                {"message": "No images provided"},
                status=status.HTTP_400_BAD_REQUEST
            )

        for image in images:
            ProductImageMasters.objects.create(
                productid=productid,
                image=image,
                create_at=timezone.now()
            )

        return Response(
            {"message": "Product images uploaded successfully"},
            status=status.HTTP_201_CREATED
        )
    
class DepartmentListAPIView(APIView):

    def get(self, request):
        departments = DeptMasters.objects.all().order_by('did')
        serializer = DepartmentListSerializer(departments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class LocationListAPIView(APIView):

    def get(self, request):
        did = request.GET.get('did')

        locations = LocationMasters.objects.all().order_by('lid')

        if did:
            locations = locations.filter(did=did)

        serializer = LocationListSerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)