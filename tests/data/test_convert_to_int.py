import pytest
import sys
sys.path.append(r"C:\Users\anh.maciag\OneDrive - JLL\mine\week79")
from src.data.convert_to_int import convert_to_int

class TestConvertToInt:
    def test_on_convert_to_int(self):
        assert convert_to_int("3,001,150") == 3001150

    def test_on_convert_to_int2(self):
        assert convert_to_int("2,418") == 2418

    @pytest.mark.xfail(reason="Haven't created this function yet")
    def test_on_sth_else(self):
        assert sth_else("32") == 32

#def test_on_diffent():
#    assert convert_to_int("3,001150") == 340, 'Wrong conversion'
