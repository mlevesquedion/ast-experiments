import bouncer


def test_adding_to_list_is_illegal():
    code = "[].add(1)"
    assert not bouncer.check(code)


def test_appending_to_list_is_legal():
    code = "[].append(1)"
    assert bouncer.check(code)


def test_adding_two_lists_is_legal():
    code = "[] + []"
    assert bouncer.check(code)


def test_works_with_user_defined_classes():
    code = """\
class A:
    def __init__(self):
        self.valid = 'valid'
A().valid"""
    assert bouncer.check(code)
