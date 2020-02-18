from django.urls import reverse, resolve


class TestUrls:
    def test_search_url(self):
        path = reverse('search')
        assert resolve(path).view_name == 'search'

    def test_home_url(self):
        path = reverse('feed-home')
        assert resolve(path).view_name == 'feed-home'
