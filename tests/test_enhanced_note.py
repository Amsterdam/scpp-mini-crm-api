from fastapi.testclient import TestClient
from faker import Faker
from api import app
from pytest import mark as m


client = TestClient(app)
fake = Faker()


@m.describe("Testing the Enhanced Note")
class TestEnhancedNotes(object):
    @m.context("Given the new relations introduced for advanced notes:")
    @m.it("Should write a note without relations to the database")
    def test_post_note_without_relations(self):
        json_obj = {
                "note": fake.paragraph(nb_sentences=3),
                "start": fake.date_time().isoformat(),
                "end": fake.date_time().isoformat()}
        print(json_obj)
        response = client.post(
            "/api/v2/note",
            json=json_obj,
        )
        assert response.status_code == 200

    @m.it("Should write a note with given tags to the database, grabbing tag id's")
    def test_post_note_with_fixed_tags(self):
        json_obj = {
                "note": "#foo #bar #fuf",
                "start": fake.date_time().isoformat(),
                "end": fake.date_time().isoformat(),
                "tags": ["foo", "bar", "fuf"]}
        print(json_obj)
        response = client.post(
            "/api/v2/note",
            json=json_obj,
        )
        assert response.status_code == 200

    @m.it("Running a second time with the same tags")
    def test_post_note_with_fixed_tags(self):
        json_obj = {
                "note": "Now there is more text with #foo #bar #fuf, that still needs to get written. " + fake.paragraph(nb_sentences=1),
                "start": fake.date_time().isoformat(),
                "end": fake.date_time().isoformat(),
                "tags": ["foo", "bar", "fuf"]}
        print(json_obj)
        response = client.post(
            "/api/v2/note",
            json=json_obj,
        )
        assert response.status_code == 200

    @m.it("Should write a note with tags to the database, grabbing tag id's")
    def test_post_note_with_tags(self):
        json_obj = {
                "note": fake.paragraph(nb_sentences=3),
                "start": fake.date_time().isoformat(),
                "end": fake.date_time().isoformat(),
                "tags": fake.words(4)}
        print(json_obj)
        response = client.post(
            "/api/v2/note",
            json=json_obj,
        )
        assert response.status_code == 200