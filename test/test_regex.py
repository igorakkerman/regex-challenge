from unittest import TestCase

from regex.regex import matches


class TestRegex(TestCase):

    def test_empty_empty(self):
        assert matches("", "")

    def test_a_empty(self):
        assert not matches("a", "")

    def test_a_a(self):
        assert matches("a", "a")

    def test_blank_a(self):
        assert not matches(" ", "a")

    def test_a_b(self):
        assert not matches("a", "b")

    def test_a_ab(self):
        assert not matches("a", "ab")

    def test_a_aa(self):
        assert not matches("a", "aa")

    def test_a_ba(self):
        assert not matches("a", "ba")

    def test_ab_a(self):
        assert not matches("ab", "a")

    def test_a_dot(self):
        assert matches("a", ".")

    def test_ab_adot(self):
        assert matches("ab", "a.")

    def test_adot_adot(self):
        assert matches("a.", "a.")

    def test_acb_adotb(self):
        assert matches("acb", "a.b")

    def test_cab_dotab(self):
        assert matches("cab", ".ab")

    def test_cab_dotb(self):
        assert not matches("cab", ".b")

    def x_test_empty_dotstar(self):
        assert matches("", ".*")

    def test_a_astar(self):
        assert matches("a", "a*")

    def test_ab_astar(self):
        assert not matches("ab", "a*")

    def test_ab_abstar(self):
        assert matches("ab", "ab*")

    def test_abc_astar(self):
        assert not matches("abc", "a*")

    def test_abc_abstar(self):
        assert not matches("abc", "ab*")

    def test_ac_abstarc(self):
        assert matches("ac", "ab*c")

    def test_abc_abstarc(self):
        assert matches("abc", "ab*c")

    def test_abbc_abstarc(self):
        assert matches("abbc", "ab*c")

    def test_empty_astar(self):
        assert matches("", "a*")

    def test_empty_dotstar(self):
        assert matches("", ".*")

    def test_a_dotstar(self):
        assert matches("a", ".*")

    def test_a_adotstar(self):
        assert matches("a", "a.*")

    def test_aa_adotstar(self):
        assert matches("aa", "a.*")

    def test_a_dotstara(self):
        assert matches("a", ".*a")

    def test_aa_adotstara(self):
        assert matches("aa", "a.*a")

    def test_a_dotstaraa(self):
        assert not matches("a", ".*aa")

    def test_aa_adotstaraa(self):
        assert not matches("aa", "a.*aa")

    def test_aa_adotstarb(self):
        assert not matches("aa", "a.*b")

    def test_a_dotstarab(self):
        assert not matches("a", ".*ab")

    def test_ab_adotstarbb(self):
        assert not matches("ab", "a.*bb")

    def test_cccabbbbbbc_cstarabstarbbstar(self):
        assert not matches("cccabbbbbbc", "c*ab*bb*")

