import pytest
pytsetmarks = pytest.mark.django_db

class TestProductModel:
    def test_product_str_returns_str(self, product_factory): 
        # product_factory is the snake case of very ProductFactory within factories.py
        product = product_factory(title='test-product')
        assert product.__str__ == 'test-product'