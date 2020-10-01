from fastapi.testclient import TestClient
from faker import Faker
from api import app
from pytest import mark as m


client = TestClient(app)
fake = Faker()


@m.describe("Testing Contacts")
class TestContacts(object):
    @m.context("When a contact is posted to the API")
    @m.it("Should write the contact to the database")
    def test_post_contact(self):
        json_obj = {
                "name": fake.name(),
                "email":fake.ascii_email(),
                "phone":fake.phone_number()}
        print(json_obj)
        response = client.post(
            "/api/v1/contact",
            json=json_obj,
        )
        assert response.status_code == 200
