from flask import abort
from sqlalchemy.exc import SQLAlchemyError

from kirsh.model import session
from kirsh.model.store import Store
from kirsh.model.store_review import StoreReview


def create_store_review(store_id, content, score, reviewer):

    try:
        store = session.query(Store).filter(Store.id == store_id).first()

        if store:
            add_review = StoreReview(store_id=store_id, content=content, score=score, reviewer=reviewer)

            session.add(add_review)
            session.commit()

            return {
                "message": "success for create store review"
            }, 201

        else:
            abort(400, "bad request")

    except SQLAlchemyError:
        return abort(500, "database error")
