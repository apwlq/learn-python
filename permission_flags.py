"""
권한 관리에서 사용하는 비트 단위 권한 플래그.
"""

# 권한 정의
READ        = 0x0000000000000001  # 1 << 0
WRITE       = 0x0000000000000002  # 1 << 1
EXECUTE     = 0x0000000000000004  # 1 << 2

# 권한 설정
permissions = 0x0000000000000000
permissions |= READ
permissions |= WRITE

# 권한 확인 함수
def has_permission(permissions, permission):
    return (permissions & permission) != 0

# 권한 확인
print("READ 권한:", has_permission(permissions, READ))       # True
print("WRITE 권한:", has_permission(permissions, WRITE))     # True
print("EXECUTE 권한:", has_permission(permissions, EXECUTE)) # False

# 권한 제거
permissions &= ~WRITE
print("WRITE 권한:", has_permission(permissions, WRITE))     # False
