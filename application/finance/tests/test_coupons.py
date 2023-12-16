from django.test import TestCase
from application.finance.models import Coupon as CouponDB
from application.finance.coupons import CouponManager
from application.finance.enum import CouponType
from application.finance.tests import stubs
from application.common.tests.test_mixins import TestMixins


class CouponManagerTestCase(TestCase, TestMixins):

    def setUp(self) -> None:
        self.user = self.create_user()

    def test_create_coupon_from_qrcode(self):
        qrcode = stubs.QRCD_SAT_SP_1
        coupon_db: CouponDB = CouponManager().create_from_qrcode(self.user, qrcode)
        self.assertEqual(coupon_db.type, CouponType.SAT_SP)
