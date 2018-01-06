from unittest import TestCase


class TestRouting(TestCase):

    def test_descriptor(self):
        from config.routing import Descriptor
        base_url = Descriptor(options={"site":"https://google.ru"}).get_url()
        self.assertIn("https://google.ru/moskva/audio_i_video", base_url)

