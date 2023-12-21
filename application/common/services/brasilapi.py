import requests
from django.conf import settings

class BrasilAPI:

    BASE_URL = settings.BRASIL_API_URL

    def get_company_data(self, company_id: str) -> dict:
        response = requests.get(f"{self.BASE_URL}/api/cnpj/v1/{company_id}")
        if response.status_code == 200:
            data = response.json()
            return dict(
                company_name=data["razao_social"]
            )
        raise Exception(f"Unexpected error from ")