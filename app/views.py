from django.shortcuts import render, redirect
from .models import Producto
import pyrebase
from firebase_admin import db

from django.templatetags.static import static
from django.contrib import messages




config = {

    'apiKey': "AIzaSyBYxVbhpJsonMJ_mCIKN9apyMF1FgvwuAo",
    'authDomain': "examen-4846b.firebaseapp.com",
    'databaseURL': "https://examen-4846b-default-rtdb.firebaseio.com/",
    'projectId': "examen-4846b",
    'storageBucket': "examen-4846b.appspot.com",
    'messagingSenderId': "630813065188",
    'appId': "1:630813065188:web:d5a2a0cfe1d77f307f91f1",
   
  };

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()



# Create your views here.


def contacto(request):
    return render(request, 'app/contacto.html' )

def galeria(request):
    return render(request, 'app/galeria.html' )

def home(request):
    productos_data = {
        'producto1': {
            'nombre': database.child('productos').child('producto1').child('nombre').get().val(),
            'precio': database.child('productos').child('producto1').child('precio').get().val(),
            'imagen': 'img/guitarra.png'
        },
        'producto2': {
            'nombre': database.child('productos').child('producto2').child('nombre').get().val(),
            'precio': database.child('productos').child('producto2').child('precio').get().val(),
            'imagen': 'img/bateria.png'
        },
        'producto3': {
            'nombre': database.child('productos').child('producto3').child('nombre').get().val(),
            'precio': database.child('productos').child('producto3').child('precio').get().val(),
            'imagen': 'img/bajo.png'
        },
        'producto4': {
            'nombre': database.child('productos').child('producto4').child('nombre').get().val(),
            'precio': database.child('productos').child('producto4').child('precio').get().val(),
            'imagen': 'img/teclado.png'
        }
    }
    return render(request, 'app/home.html', {
        'productos': productos_data
    })


def productos(request):
    productos_data = {
        'producto1': {
            'nombre': database.child('productos').child('producto1').child('nombre').get().val(),
            'precio': database.child('productos').child('producto1').child('precio').get().val(),
            'imagen': 'img/guitarra.png'
        },
        'producto2': {
            'nombre': database.child('productos').child('producto2').child('nombre').get().val(),
            'precio': database.child('productos').child('producto2').child('precio').get().val(),
            'imagen': 'img/bateria.png'
        },
        'producto3': {
            'nombre': database.child('productos').child('producto3').child('nombre').get().val(),
            'precio': database.child('productos').child('producto3').child('precio').get().val(),
            'imagen': 'img/bajo.png'
        },
        'producto4': {
            'nombre': database.child('productos').child('producto4').child('nombre').get().val(),
            'precio': database.child('productos').child('producto4').child('precio').get().val(),
            'imagen': 'img/teclado.png'
        }
    }

    return render(request, 'app/productos.html', {
        'productos': productos_data
    })

def carrito(request):
    productos_carrito = request.session.get('carrito', [])
    
    total_precio = 0
    
    for producto in productos_carrito:
        nombre = producto['nombre']
        precio = producto['precio']
        imagen = f'app/img/{nombre}.png'  # Ajusta la ruta de la imagen según tu estructura de carpetas
        producto['imagen'] = imagen
        
        # Eliminar símbolos de moneda y caracteres no numéricos del precio
        precio = precio.replace('$', '').replace(',', '').replace('.', '')
        
        # Convertir el precio a float
        precio_float = float(precio)
        
        # Sumar el precio al total
        total_precio += precio_float
    
    return render(request, 'app/carrito.html', {
        'productos_carrito': productos_carrito,
        'total_precio': total_precio
    })

def agregar_al_carrito(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        
        # Agregar el producto al carrito (puedes almacenarlo en la sesión, en la base de datos, etc.)
        # Aquí puedes implementar la lógica para agregar el producto a tu estructura de datos del carrito
        
        # Ejemplo de almacenamiento en la sesión
        if 'carrito' not in request.session:
            request.session['carrito'] = []
        
        carrito = request.session['carrito']
        carrito.append({
            'producto_id': producto_id,
            'nombre': nombre,
            'precio': precio
        })
        
        request.session['carrito'] = carrito
        
        return redirect('carrito')


def limpiar_carrito(request):
    request.session['carrito'] = []  # Vacía la lista de productos del carrito en la sesión
    return redirect('carrito')  # Redirige al carrito después de limpiarlo


def carrito(request):
    productos_carrito = request.session.get('carrito', [])
    
    total_precio = 0
    
    for producto in productos_carrito:
        nombre = producto['nombre']
        precio = producto['precio']
        imagen = f'app/img/{nombre}.png'  # Ajusta la ruta de la imagen según tu estructura de carpetas
        producto['imagen'] = imagen
        
        # Eliminar símbolos de moneda y caracteres no numéricos del precio
        precio = precio.replace('$', '').replace(',', '').replace('.', '')
        
        # Convertir el precio a float
        precio_float = float(precio)
        
        # Sumar el precio al total
        total_precio += precio_float
    
    return render(request, 'app/carrito.html', {
        'productos_carrito': productos_carrito,
        'total_precio': total_precio
    })

