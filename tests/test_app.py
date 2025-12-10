import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import *

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10
    
def test_sub():
    assert sub(5, 2) == 3

def test_sub2():
    assert sub(5, 2) != 2
    
def test_mult():
    assert mult(9, 7) == 63
    
def test_mult2():
    assert mult(9, 7) != 56
    
def test_div():
    assert div(10, 5) == 2
    
def test_div2():
    assert div(10, 5) != 1
    
def test_log():
    assert log(10) == 2.302585092994543
    
def test_log2():
    assert log(10) != 2.301585092994543
    
def test_square():
    assert square(6) == 36
    
def test_square2():
    assert square(6) != 30
    
def test_sin():
    assert round(sin(3.141592)) == 0
    
def test_sin2():
    assert round(sin(3.141592/2)) == 1
    
def test_cos():
    assert cos(0) == 1
    
def test_cos2():
    assert cos(0) != -1
    
def test_sqrt():
    assert sqrt(36) == 6
    
def test_sqrt2():
    assert sqrt(0) == 0
    
def test_percent():
    assert percent(5, 10) == 50
    
def test_percent2():
    assert percent(10, 5) == 200