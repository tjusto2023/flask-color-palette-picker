import pytest
from src.domains.picture import Picture
from faker import Faker
faker = Faker()

@pytest.fixture
def picture_fixture():
    # Given
    return {
        "name_file": faker.image_url(),
        "color_palette":  [faker.hex_color() for _ in range(5)]
    }

class TestPicture:
    def test_given_valid_inputs_when_created_then_instance_is_created(self, picture_fixture):
        # Act
        palette = Picture(**picture_fixture)

        # Assert
        assert isinstance(palette, Picture)
        assert palette.name_file == picture_fixture["name_file"]
        assert palette.color_palette == picture_fixture["color_palette"]
        assert palette.name.startswith("picture_")
        assert palette.name.endswith(".png")
        assert palette.name[15:-4].isdigit()