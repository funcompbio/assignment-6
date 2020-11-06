import subprocess
import pytest
import src.smilesparser

def test_aspirine() :

    def mock_input(s) :
        return "CC(=O)OC1=CC=CC=C1C(O)=O"

    src.smilesparser.input = mock_input
    molf = src.smilesparser.main()

    assert molf == "Molecular formula: C9H8O4"

def test_ibuprofen() :

    def mock_input(s) :
        return "CC(C)CC1=CC=C(C=C1)C(C)C(O)=O"

    src.smilesparser.input = mock_input
    molf = src.smilesparser.main()

    assert molf == "Molecular formula: C13H18O2"

def test_caffeine() :

    def mock_input(s) :
        return "CN1C=NC2=C1C(=O)N(C)C(=O)N2C"

    src.smilesparser.input = mock_input
    molf = src.smilesparser.main()

    assert molf == "Molecular formula: C8H10N4O2"

def test_nevirapine() :

    def mock_input(s) :
        return "CC1=C2NC(=O)C3=C(N=CC=C3)N(C3CC3)C2=NC=C1"

    src.smilesparser.input = mock_input
    molf = src.smilesparser.main()

    assert molf == "Molecular formula: C15H14N4O1"
