from app.utils.http_exceptions import not_found

def exist_user(self, user_id: int):
    if not self.repository.get_by_id(user_id):
        not_found(f"User with ID {user_id} not found")
