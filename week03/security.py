"""密码哈希和 JWT 工具。"""

import hashlib
import os
from datetime import datetime, timedelta, timezone

import jwt

# 签名密钥，token 真伪全靠它；现在是开发占位值，正式上线必须换成随机密钥并放环境变量
SECRET_KEY = "dev-secret-key-change-me-please-32-bytes-min"
# 对称签名算法
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 60


class TokenError(Exception):
    pass

# 密码哈希
def hash_password(password: str) -> str:
    salt = os.urandom(16).hex()
    digest = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        100_000,
    ).hex()
    return f"{salt}${digest}"

# 验证密码
def verify_password(password: str, stored: str) -> bool:
    salt, digest = stored.split("$")
    candidate = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        100_000,
    ).hex()
    return candidate == digest

# 创建 JWT 访问令牌
def create_access_token(username: str) -> str:
    payload = {
        "sub": username,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXPIRE_MINUTES),# 过期时间
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

# 解码 JWT 访问令牌
def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.PyJWTError as exc:
        raise TokenError(str(exc)) from exc
