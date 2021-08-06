class Carro:
    def __init__(self, request): #constructor, request.
        self.request=request
        self.sessions=request.sessions
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        else:
            self.carro=carro
    
    def agregar(self, producto): #agregar producto al carro
        if(str(producto.id) not in self.carro.keys()): #si producto.id no esta en el key de carro
            self.carro[producto.id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }   #si el producto.id no esta en carro que se agregue
        else:
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    break
                #recorremos los items de carro y si el key es igual al id del producto. se suma la cantidad
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True
        
    def eliminar(self, producto):
            producto.id=str(producto.id)
            if producto.id in self.carro:
                del self.carro[producto.id]
                self.guardar_carro()
        
    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key==str(producto.id):
                value["cantidad"]=value["cantidad"]-1
                if value["cantidad"]<1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        carro=self.session["carro"]={}
        self.session.modified=True


