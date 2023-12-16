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
            coupon_instance.type = CouponType.SAT_SP
            coupon_instance.extracted_data = dict(
                amount=data_parts[2],
                user=data_parts[3],
                datatime=datetime.datetime.strptime(data_parts[1], "%Y%m%d%H%M%S").isoformat()
            )
        
        coupon_instance.save()
        return coupon_instance

        


