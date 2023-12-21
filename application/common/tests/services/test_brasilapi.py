import requests_mock
from django.test import TestCase
from application.common.tests.test_mixins import TestMixins
from application.common.services.brasilapi import BrasilAPI


class BrasilAPITestCase(TestCase, TestMixins):

    @requests_mock.Mocker()
    def test_get_company_data(self, reqmock):
        reqmock.get(f'{BrasilAPI.BASE_URL}/api/cnpj/v1/some_company_id', 
            text='{"razao_social": "ACME S.A."}'
        )
        company_data = BrasilAPI().get_company_data("some_company_id")
        self.assertDictContainsSubset({
            "company_name": "ACME S.A."
        }, company_data)