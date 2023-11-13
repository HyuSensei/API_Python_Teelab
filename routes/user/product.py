from fastapi import APIRouter, HTTPException, status, Query
from controllers.user import ProductController
from pydantic import BaseModel
import models

router=APIRouter()

class ProductBase(BaseModel):
    name: str
    image: str
    price: float
    category_id: int
    class Config:
        arbitrary_types_allowed = True

@router.get("/api/v1/products/ao_thun",status_code=status.HTTP_200_OK)
def getProductAoThun():
    try:
        data= ProductController.handleProductAoThun()
        print(data)
        return data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.get("/api/v1/products/polo",status_code=status.HTTP_200_OK)
def getProductPolo():
    try:
        data= ProductController.handleProductPolo()
        print(data)
        return data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.post("/api/v1/products/store",status_code=status.HTTP_201_CREATED)
def addProduct(product: ProductBase):
    try:
        data_product= models.Product(**product.dict())
        get_product= ProductController.storeProduct(data_product)
        return get_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.get("/api/v1/products/{product_id}",status_code=status.HTTP_200_OK)
def getProductDetail(product_id: int):
    try:
        get_product= ProductController.handleProductDetail(product_id)
        return get_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.get("/api/v1/products/search/{product_name}",status_code=status.HTTP_200_OK)
def getProductSearch(
    product_name: str,
    page: int = Query(1, ge=1),
):
    try:
        get_product= ProductController.handleSearchProduct(product_name,page)
        return get_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
