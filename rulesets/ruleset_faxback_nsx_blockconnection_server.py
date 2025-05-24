#!/usr/bin/env python3

from cmk.rulesets.v1 import Label, Title
from cmk.rulesets.v1.form_specs import BooleanChoice, DefaultValue, DictElement, Dictionary, Float, LevelDirection, SimpleLevels
from cmk.rulesets.v1.rule_specs import CheckParameters, HostCondition, Topic

def _parameter_form_faxback_nsx_blockconnection_server():
    return Dictionary(
        elements = {
            "login_percentage_upper": DictElement(
                parameter_form = SimpleLevels(
                    title = Title("Upper percentage threshold for Login Percentage"),
                    form_spec_template = Float(),
                    level_direction = LevelDirection.UPPER,
                    prefill_fixed_levels = DefaultValue(value=(80.0, 90.0)),
                ),
                required = True,
            ),
        }
    )

rule_spec_myhostgroups = CheckParameters(
    name = "faxback_nsx_blockconnection_server",
    title = Title("FaxBack Block Connection Thresholds"),
    topic = Topic.GENERAL,
    parameter_form = _parameter_form_faxback_nsx_blockconnection_server,
    condition = HostCondition(),
)