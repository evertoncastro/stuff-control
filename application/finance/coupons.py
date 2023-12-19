import datetime
from application.finance.models import Coupon as CouponDB
from application.finance.enum import CouponType
from application.authentication.models import User
from typing import List


class CouponManager:
    
    def create_from_qrcode(self, user: User, qrcode_data: str) -> CouponDB:
        data_parts: List[str] = qrcode_data.split("|")
        coupon_instance = CouponDB(
            user=user,
            raw_data=qrcode_data
        )
        if len(data_parts) == 5:
            access_key = data_parts[0]
            coupon_instance.type = CouponType.SAT_SP.value
            coupon_instance.extracted_data = dict(
                amount=data_parts[2],
                user=data_parts[3] if data_parts[3] else None,
                datetime=datetime.datetime.strptime(data_parts[1], "%Y%m%d%H%M%S").isoformat(),
                issuer=access_key[6:20]
            )
            coupon_instance.amount=float(data_parts[2])
        
        coupon_instance.save()
        return coupon_instance

        


