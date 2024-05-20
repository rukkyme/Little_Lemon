from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .serializers import BookingSerializer, MenuSerializer
from rest_framework.permissions import IsAuthenticated
#from rest_framework.response import Response

from .models import Booking, Menu




#Create your views here.
def home(request):
   return render(request, 'home.html', {})

 
'''USing the class based view, you have this
 #create a class BookingView that subclasses APIView
class BookingView(APIView):
    #defines the method 'get' and the method handles 
    # HTTPGET request to retrieve all objects 
    # in booking
    def get(self, request): # typically the first parameter of a method when you define methods within a class is named 'self'
        items = Booking.objects.all()
        """creates a serializer instance named serializer and  
        uses the BookingSerializer class to serialize the items queryset retrieved from the database. 
        The many=True argument shows there are multiple instances of Booking to serialize."""
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data)
    
    #This line defines a method named post within the BookingView class. 
    #The method handles HTTP POST requests to create new data entries.
    def post(self,request):
        #It uses the MenuSerializer class to deserialize the data sent in the POST request (request.data) into a format suitable for 
        #creating a new instance of the Booking model.
        serializer = BookingSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status' : "success", "data" : serializer.data})
    
class MenuView(APIView):
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data)
    def Post(self, request):
        serializer = MenuSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status' : "success", "data" :  serializer.data })
            
'''

#using the generic based view, we'll have the following
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
#class MenuItemsView(generics.ListCreateAPIView):
class MenuItemsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
#class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
#    permission_classes = [IsAuthenticated]
#    queryset = Menu.objects.all()
#    serializer_class = MenuSerializer

    
    
    
    



