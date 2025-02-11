from sqlalchemy.orm import Session
from models import Producto



def create_producto(db: Session, name: str, stock: int, cost: float):
    nuevo_producto = Producto(name=name, stock=stock, cost=cost)
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

