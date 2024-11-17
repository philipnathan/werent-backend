from flask import Blueprint, request
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
)
from sqlalchemy import select

# from connectors.mysql_connectors import connection
from models.users import Users

users_routes = Blueprint("users_routes", __name__)
Session = sessionmaker(connection)
s = Session()


@users_routes.route("/api/v1/auth/register", methods=["POST"])
def register_user():
    try:
        NewUser = Users(
            username=request.form["username"],
            email=request.form["email"],
        )
        NewUser.set_password(request.form["password"])
        s.add(NewUser)
        s.commit()
    except Exception as e:
        print(e)
        s.rollback()
        return {"message": "Fail to Register New User"}, 500
    return {"message": "Success to Create New User"}, 200


@users_routes.route("/api/v1/auth/login", methods=["POST"])
def login_user():
    try:
        email = request.form["email"]
        user = s.query(Users).filter(Users.email == email).first()

        if user == None:
            return {"message": "User not found"}, 403

        if not user.check_password(request.form["password"]):
            return {"message": "Invalid password"}, 403

        acces_token = create_access_token(
            identity=user.id,
            additional_claims={"email": user.email, "id": user.id},
        )
        s.flush()
        refresh_token = create_refresh_token(identity=user.id)
        return {
            "email": user.email,
            "id": user.id,
            "access_token": acces_token,
            "refresh_token": refresh_token,
            "message": "Success to Login user",
        }, 200
    except Exception as e:
        print(e)
        s.rollback()
        return {"message": "Failed to Login User"}, 500


@users_routes.route("/api/v1/auth/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh_token():
    try:
        # Get the user's identity from the refresh token
        current_user_id = get_jwt_identity()

        # Query the user to confirm they exist
        user = s.query(Users).filter(Users.id == current_user_id).first()
        if not user:
            return {"message": "User not found"}, 404

        # Create a new access token
        new_access_token = create_access_token(
            identity=user.id,
            additional_claims={"email": user.email, "id": user.id},
        )
        return {
            "access_token": new_access_token,
            "message": "Access token refreshed successfully",
        }, 200

    except Exception as e:
        print(e)
        return {"message": "Failed to refresh access token"}, 500


@users_routes.route("/api/v1/auth/logout", methods=["POST"])
@jwt_required()
def logout_user():
    try:
        jti = get_jwt()["jti"]
        return {"message": "User successfully logged out"}, 200
    except Exception as e:
        print(e)
        return {"message": "Failed to logout"}, 500


@users_routes.route("/api/v1/users/me", methods=["GET"])
@jwt_required()
def get_current_user():
    claims = get_jwt()
    return {"claims": claims}


@users_routes.route("/api/v1/users/me", methods=["PUT"])
@jwt_required()
def update_current_user():
    current_user_id = get_jwt_identity()
    print(current_user_id)
    try:
        user = s.query(Users).filter(Users.id == current_user_id).first()
        if not user:
            return {"message": "User not found"}, 404

        if "password" in request.form:
            user.set_password(request.form["password"])
        user.update_at = datetime.now()

        s.add(user)
        s.commit()
        return {"message": "User updated successfully"}, 200

    except Exception as e:
        print(e)
        s.rollback()
        return {"message": "Failed to update user"}, 500


@users_routes.route("/api/v1/users/me", methods=["DELETE"])
@jwt_required()
def delete_current_user():
    current_user_id = get_jwt_identity()
    try:
        user = s.query(Users).filter(Users.id == current_user_id).first()

        if not user:
            return {"message": "User not found"}, 404

        s.delete(user)
        s.commit()
        return {"message": "User deleted successfully"}, 200

    except Exception as e:
        print(e)
        s.rollback()
        return {"message": "Failed to delete user"}, 500
