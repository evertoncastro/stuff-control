from django.test import TestCase
from application.finance.models import Coupon as CouponDB
from application.finance.coupons import CouponManager
from application.finance.enum import CouponType
from application.finance.tests import stubs
from application.common.tests.test_mixins import TestMixins


class CouponManagerTestCase(TestCase, TestMixins):

    def setUp(self) -> None:
        self.user = self.create_user()

    def test_create_coupon_from_qrcode_sat_sp_1(self):
        qrcode = stubs.QRCD_SAT_SP_1
        coupon_db: CouponDB = CouponManager().create_from_qrcode(self.user, qrcode)
        self.assertEqual(coupon_db.type, CouponType.SAT_SP.value)
        self.assertDictContainsSubset(dict(
            amount="192.34",
            datetime="2023-12-09T21:41:10",
            user="25786106063",
            issuer="10583267000102"
        ), coupon_db.extracted_data)
        self.assertEqual(coupon_db.amount, 192.34)
        self.assertEqual(coupon_db.raw_data, stubs.QRCD_SAT_SP_1)

    def test_create_coupon_from_qrcode_sat_sp_2(self):
        qrcode = stubs.QRCD_SAT_SP_2
        coupon_db: CouponDB = CouponManager().create_from_qrcode(self.user, qrcode)
        self.assertEqual(coupon_db.type, CouponType.SAT_SP.value)
        self.assertDictContainsSubset(dict(
            amount="192.34",
            datetime="2023-12-09T21:41:10",
            user=None,
            issuer="10583267000102"
        ), coupon_db.extracted_data)
        self.assertEqual(coupon_db.amount, 192.34)
        self.assertEqual(coupon_db.raw_data, stubs.QRCD_SAT_SP_2)
