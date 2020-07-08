from flask import abort
from sqlalchemy.exc import SQLAlchemyError

from kirsh.model import session
from kirsh.model.store import Store
from kirsh.model.store_review import StoreReview
from kirsh.model.product_review import ProductReview


def store_detail(store_id):

    try:
        store = session.query(Store).filter(Store.id == store_id).first()

        if store:
            store_reviews = session.query(StoreReview).filter(StoreReview.store_id == store_id).all()
            product_reviews = session.query(ProductReview).filter(ProductReview.store_id == store_id).all()

            return {
                "id": store.id,
                "ranking": store.ranking,
                "name": store.name,
                "description": store.description,
                "score": store.score,
                "average_price": store.average_score,
                "store_review": [{
                    "content": store_review.content,
                    "score": store_review.score,
                    "datetime": str(store_review.datetime),
                    "reviewer": store_review.reviewer
                }for store_review in store_reviews],
                "product_review": [{
                    "name": product_review.name,
                    "content": product_review.content,
                    "score": product_review.score,
                    "datetime": str(product_review.datetime),
                    "reviewer": product_review.reviewer,
                    "picture": product_review.picture
                }for product_review in product_reviews]
            }

        else:
            return abort(404, "not found ")

    except SQLAlchemyError:
        return abort(500, "database error")
