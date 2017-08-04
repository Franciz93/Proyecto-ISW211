carritoCompras=[] #Lista para guardar los productos seleccionados por el cliente para posible compra
listaProductos= []#Lista para almacenar todos los productos, de todas las categorias


#Clases madre electronico, info general para las categorias
class Electronico:
    def __init__(self,pCodigo,pMarca,pModelo,pPrecio):
        self.codigo=pCodigo
        self.marca=pMarca
        self.modelo=pModelo
        self.precio=pPrecio

class Computadora(Electronico):
    __impuesto=0.10
    def __init__(self,pCodigo,pMarca,pModelo,pAnio,pProcesador,pRam,pDiscoDuro,pColor,pTamano,pPrecio):
        super().__init__(pCodigo,pMarca,pModelo,pPrecio)
        self.anio=pAnio
        self.procesador=pProcesador
        self.ram=pRam
        self.discoDuro=pDiscoDuro
        self.color=pColor
        self.tamano=pTamano

        # Traductor
    def __str__(self):
        return ("Codigo {0} Marca {1} Modelo {2} Año{3} Procesador {4} RAM {5} Disco duro {6} Color {7} Precio {8}"
                "".format(self.codigo,self.marca, self.modelo, self.anio, self.procesador, self.ram, self.discoDuro,
                          self.color,self.tamano,self.precio))

    def garantia(self):
        print('Garantia: 18 meses')


class Telefono(Electronico):
    __impuesto:0.08
    def __init__(self,pCodigo,pMarca,pColor,pModelo,pCapacidad,pRed,pMemoria,pCamara,pSO,pPrecio):
        super().__init__(pCodigo,pMarca,pModelo,pPrecio)
        self.color=pColor
        self.capacidad=pCapacidad
        self.red=pRed
        self.memoria=pMemoria
        self.camara=pCamara
        self.so=pSO

    def __str__(self):
        return ("Codigo {0} Marca {1} Modelo {2} Año{3} Procesador {4} RAM {5} Disco duro {6} Precio {7}"
                "".format(self.codigo,self.marca, self.modelo, self.capacidad, self.red, self.memoria, self.camara,
                          self.so,self.precio))

    def garantia(self):
        print('Garantia: 12 meses')

class Accesorios:
    __impuesto=0.05
    def __init__(self,pCodigo,pMarca,pPrecio):
        self.codigo=pCodigo
        self.marca=pMarca

        self.precio=pPrecio


# Herencia y superClase
class nuevoAccesorio(Accesorios):
    def __init__(self,pCodigo,pMarca,pPrecio,pConectividad,pColor,pTamano):
        super().__init__(pCodigo,pMarca,pPrecio)
        self.conectividad=pConectividad
        self.color=pColor
        self.tamano=pTamano

    def __str__(self):
        return ("Codigo {0} Marca {1}  Precio{2} Conectividad {3} Color {4} Tamaño {5}"
                "".format(self.codigo,self.marca, self.precio, self.conectividad, self.color, self.tamano))
#Polimorfismo
    def garantia(self):
        print('Garantia: 06 meses')

#Computadoras en catalogo existente
dell1=Computadora(123,'DELL','INSPIRON','2017','INTEL CORE i5','8GB','1 TB ','Negro Mate','15.6''',489)
dell2=Computadora(124,'DELL','INSPIRON','2017','INTEL CORE 17','8GB','SATA 1TB','GRIS','15.6''', 879 )
dell3=Computadora(125,'DELL',"E3421","2014","INTEL CORE i3","4GB","HDD 700GB",'NEGRO','14''',559)
mac1=Computadora(126,'MAC',"MacBook Air 15","2016","INTEL CORE i5","8GB","SSD 120GB",'GRIS','14''',1299)
mac2=Computadora(127,'MAC',"MacBook Pro 15","2017","INTEL CORE i7","16GB","SSD 1TB",'BLANCA','17''',3499)
mac3=Computadora(130,'MAC',"MacBook Pro 15","2017","INTEL CORE i7","16GB","SSD 1TB",'BLANCA','15''',3349)
toshiba1=Computadora(131,'TOSHIBA',"ZR10","2010","AMD APU A10","16GB","SSD 256GB",'GRIS','15''',829)
toshiba2=Computadora(132,'TOSHIBA',"CR7","2011","INTEL CORE i7","8GB","HDD 1TB",'NEGRO','16''',675)
asus1=Computadora(131,'ASUS','PRO GAMING Z','2017','INTEL CORE i7 HQ','24GB','1TB','BLANCA','17''',3479)
asus2=Computadora(132,'ASUS','AORUS X7 V6','2016','INTEL CORE i7','12GB','500GB SSD','NEGRO','15''',1929)
listaPc=[dell1,dell2,dell3, mac1,mac2,mac3,toshiba1,toshiba2,asus1,asus2]

#Telefonos en catalogo existente
samsung1=Telefono(333,'SAMSUNG','DORADO','S8','64GB','2G/3G/4G LTE','4GB','12MPX','ANDROID 7.0',789)
samsung2=Telefono(332,'SAMSUNG','BLANCO','J7','16GB','2G/3G/4G LTE','2GB','13MPX','ANDROID MARSMALLOW 6.0',789)
samsung3=Telefono(331,'SAMSUNG','GRIS','A9','32GB','2G/3G/4G LTE','4GB','12MPX','ANDROID MARSMALLOW 6.0',479)
apple1= Telefono(222,'APPLE','BLANCO','IPHONE 6','32GB','3G/4G','1GB','18MPX','IOS 10.3.3',479)
apple2=Telefono(223,'APPLE','ROSADO','IPHONE 7','64 GB','4G LTE','1.5GB','22MPX','IOS 10.3.3',578)
apple3=Telefono(223,'APPLE','NEGRO','IPHONE 6 SE','32 GB','4G LTE','1GB','22MPX','IOS 10.3.3',739)
huawei1=Telefono(111,'HUAWEI','GRIS','P10','32GB','2G/3G/4G LTE','4GB','12MPX','ANDROID 4.0',500)
huawei2=Telefono(121,'HUAWEI','GRIS','P9','32GB','2G/3G/4G LTE','3GB','12MPX','Android 6 + HUAWEI Emotion UI 4.1',479)
huawei3=Telefono(131,'HUAWEI','PLATEADO','MATE 9','64GB','2G/3G/4G LTE','4GB','12MPX','Android 7  + HUAWEI Emotion UI 5.0',579)
listaTelefonos=[samsung1,samsung2,samsung3,apple1,apple2,apple3, huawei1,huawei2,huawei3]

#Accesorios en catalogo existente
speaker=nuevoAccesorio(888,'MAXELL',32,'BLUETOOH/3.5','GRIS','N/A')
heatphones=nuevoAccesorio(889,'SAMSUNG',25,'3.5','NEGROS','N/A')
cargadorPortatil=nuevoAccesorio(810,'BQ',45,'m USB','NEGRO','17000 MHA')
mouse1=nuevoAccesorio(811,'GENIUS',12,'USB','GRIS','N/A')
mouse2=nuevoAccesorio(812,'GENIUS',12,'WIRELESS','GRIS','N/A')
discoExterno=nuevoAccesorio(813,'TOSHIBA',85,'USB/XSATA','NEGRO','1 TB')
cargadorTelefono=nuevoAccesorio(815,'ACC',15,'N/A','BLANCO','30CM')
cargadorPc=nuevoAccesorio(816,'UNIVERSALES',35,'VARIABLE','NEGROS','N/A')
estuchePc=nuevoAccesorio(817,'CLIP',22,'N/A','A ELEGIR','15''')
parlantes=nuevoAccesorio(818,'LOGITEC', 65, 'USB/3.5','NEGROS','N/A')
heatset=nuevoAccesorio(819,'KRACKEN',39,'USB','VARIADO','N/A')
listaAccesorios=[speaker,heatphones,cargadorPortatil,mouse1,mouse2,discoExterno,cargadorTelefono,cargadorPc,estuchePc,parlantes,heatset,]

