from fastapi import HTTPException, status


def not_found(detail: str = "Resource not found"):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=detail
    )


def bad_request(detail: str = "Bad request"):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=detail
    )


def unauthorized(detail: str = "Unauthorized"):
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail
    )


def conflict(detail: str = "Conflict"):
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=detail
    )


def internal_error(detail: str = "Internal server error"):
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=detail
    )