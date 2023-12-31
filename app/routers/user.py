from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=['User']
)

# @router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

#     #hash the password - user.password
#     user.password = utils.hash(user.password)
#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user

#----------------------------------------------------------------->
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    #hash the password - user.password
    user.password = utils.hash(user.password)
    new_user = models.User(**user.dict())
    print(new_user.email)
    user_exists = db.query(models.User).filter(models.User.email == new_user.email).first()
    if user_exists:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"User with {new_user.email} already exists")

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

#----------------------------------------------------------------->


@router.get("/{id}", response_model = schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= f"User with {id} does not exists")

    return user