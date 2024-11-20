from flask import Blueprint, request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
)
from flasgger import swag_from

# from connectors.mysql_connectors import connection
from app.models.users import Users
from app.db import db

users_routes = Blueprint("users_routes", __name__, url_prefix="/api/v1")


@users_routes.route("/auth/register", methods=["POST"])
@swag_from("./register_user.yml")
def register_user():
    try:
        NewUser = Users(
            username=request.form["username"],
            email=request.form["email"],
            password=request.form["password"],
            phone_number=request.form["phone_number"],
        )
        # NewUser.set_password(request.form["password"])
        db.session.add(NewUser)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return {"message": "Fail to Register New User"}, 500

    return {"message": "Success to Create New User"}, 201


@users_routes.route("/auth/login", methods=["POST"])
@swag_from("./login_user.yml")
def login_user():
    try:
        email = request.form["email"]
        # user = s.query(Users).filter(Users.email == email).first()
        user = Users.query.filter_by(email=email).first()

        if user is None:
            return {"message": "User not found"}, 403

        if not user.check_password(request.form["password"]):
            return {"message": "Invalid password"}, 403

        acces_token = create_access_token(
            identity=str(user.id),
            additional_claims={
                "email": user.email,
                "id": str(user.id),
                "image_url": user.image_url,
            },
        )
        # s.flush()
        db.session.flush()

        refresh_token = create_refresh_token(identity=str(user.id))
        return {
            "email": user.email,
            "id": user.id,
            "access_token": acces_token,
            "refresh_token": refresh_token,
            "message": "Success to Login user",
        }, 200
    except Exception as e:
        print(e)
        db.session.rollback()
        return {"message": "Failed to Login User"}, 500


@users_routes.route("/auth/refresh", methods=["POST"])
@jwt_required(refresh=True)
@swag_from("./refresh_token.yml")
def refresh_token():
    try:
        # Get the user's identity from the refresh token
        current_user_id = get_jwt_identity()

        # Query the user to confirm they exist
        # user = s.query(Users).filter(Users.id == current_user_id).first()
        user = Users.query.filter_by(id=current_user_id).first()
        if not user:
            return {"message": "User not found"}, 404

        # Create a new access token
        new_access_token = create_access_token(
            identity=str(user.id),
            additional_claims={"email": user.email, "id": str(user.id)},
        )
        return {
            "access_token": new_access_token,
            "message": "Access token refreshed successfully",
        }, 200

    except Exception as e:
        print(e)
        return {"message": "Failed to refresh access token"}, 500


@users_routes.route("/auth/logout", methods=["POST"])
@jwt_required()
def logout_user():
    try:
        jti = get_jwt()["jti"]
        return {"message": "User successfully logged out"}, 200
    except Exception as e:
        print(e)
        return {"message": "Failed to logout"}, 500


@users_routes.route("/users/me", methods=["GET"])
@jwt_required()
@swag_from("./get_user.yml")
def get_current_user():
    claims = get_jwt()
    return {"claims": claims}


@users_routes.route("/users/me", methods=["PUT"])
@jwt_required()
@swag_from("./edit_user.yml")
def update_current_user():
    current_user_id = get_jwt_identity()
    print(current_user_id)
    try:
        # user = s.query(Users).filter(Users.id == current_user_id).first()
        user = Users.query.filter_by(id=current_user_id).first()
        if not user:
            return {"message": "User not found"}, 404

        if "password" in request.form:
            user.password = user.set_password(request.form["password"])

        # tidak perlu update_at, otomatis terisi kalau ada perubahan data di database
        # user.update_at = datetime.now()

        db.session.add(user)
        db.session.commit()
        return {"message": "User updated successfully"}, 200

    except Exception as e:
        print(e)
        db.session.rollback()
        return {"message": "Failed to update user"}, 500


@users_routes.route("/users/me", methods=["DELETE"])
@jwt_required()
@swag_from("./delete_user.yml")
def delete_current_user():
    current_user_id = get_jwt_identity()
    try:
        # user = s.query(Users).filter(Users.id == current_user_id).first()
        user = Users.query.filter_by(id=current_user_id).first()

        if not user:
            return {"message": "User not found"}, 404

        user.set_to_inactive()
        db.session.commit()
        # s.delete(user)
        # s.commit()
        return {"message": "User deleted successfully"}, 200

    except Exception as e:
        print(e)
        db.session.rollback()
        return {"message": "Failed to delete user"}, 500
