from fastapi import Header, HTTPException, Depends

def get_role(role: str = Header(...)):
    return role

def require_role(required_role: str):
    def checker(role: str = Depends(get_role)):
        hierarchy = ["viewer", "analyst", "admin"]
        if hierarchy.index(role) < hierarchy.index(required_role):
            raise HTTPException(status_code=403, detail="Not enough permissions")
    return checker