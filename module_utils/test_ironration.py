import pytest
import ironration as ir

##
## Testing `dict_merge`
##
def test_dict_merge_pair():
    x1 = {'one': 1, 'two': '2'}
    x2 =  {'two': 2, 'three': 3}
    assert ir.dict_merge(x1, x2) == {
        'one': 1, 'two': 2, 'three': 3
    }

def test_dict_merge_immutable():
    """ensure dict merge is non-destructive/immutable."""
    x1 = {'one': 1, 'two': 2}
    x1_cop = x1.copy()
    ir.dict_merge(x1, {'three': 3, 'two': None})
    assert x1 == x1_cop
    ir.dict_merge({'ten': 10, 'one': '1'}, x1)
    assert x1 == x1_cop

def test_dict_merge_three():
    new_dict = ir.dict_merge(
        {'one': 1, 'two': 2}, {'three': 3}, {'four': 4, 'five': 5})
    assert new_dict == {'one':1, 'two':2, 'three': 3, 'four': 4, 'five': 5}

def test_dict_merge_precedence():
    x1 = {'one': 1, 'two': '2'}
    x2 =  {'two': 2, 'three': 3}
    assert ir.dict_merge(x1, x2)['two'] == 2
    assert ir.dict_merge(x2, x1)['two'] == '2'

def test_dict_merge_empty():
    x1 = {'one': 1, 'two': 2}
    assert ir.dict_merge(x1, {}) == x1
    assert ir.dict_merge({}, x1) == x1


##
## Testing `get_in`
##
def __get_in_testval():
    return {
        'one': {
            'two': {
                'three': 3,
                'four': {
                    'end': True
                }
            }
        },
        'topval': 133
    }

def test_get_in_topval():
    assert ir.get_in(__get_in_testval(), 'topval') == 133
    assert ir.get_in(__get_in_testval(), ['topval']) == 133

def test_get_in_nested():
    assert ir.get_in(__get_in_testval(), 'one', 'two', 'three') == 3
    assert ir.get_in(__get_in_testval(), ['one', 'two', 'three']) == 3

def test_get_in_unfound_default_top():
    assert ir.get_in(__get_in_testval(), ['non-existing-topval'], default=None) == None
    assert ir.get_in(__get_in_testval(), 'non-existing-topval', default=None) == None

def test_get_in_unfound_default_nested():
    assert ir.get_in(__get_in_testval(), ['one', 'two', '-not-present'], default='bad') == 'bad'
    assert ir.get_in(__get_in_testval(), 'one', 'two', '-not-present', default='bad') == 'bad'

