import models
import schemas.post as schemas
from config.database import session


def create_post(user_id: int, post: schemas.PostCreate):
    db_post = models.Post(user_id=user_id, content=post.content)
    session.add(db_post)
    session.commit()
    session.refresh(db_post)

    return db_post
