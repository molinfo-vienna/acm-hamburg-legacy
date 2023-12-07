from acm_hamburg_legacy import rule_sets


def test_rule_sets():
    rule_set_names = rule_sets.rule_set_names

    assert isinstance(rule_set_names, list)
    assert len(rule_set_names) > 0

    for rule_set_name in rule_set_names:
        rule_set = getattr(rule_sets, rule_set_name)
        assert isinstance(rule_set, (list, dict))
