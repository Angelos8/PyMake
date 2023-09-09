import pytest

from PyMake.exceptions import UndefinedVariableError


@pytest.mark.parametrize(
    "parser, args, output", [
        ("parser_1", "input_1", "parser1_input1_output"),
        ("parser_1", "input_2", "parser1_input2_output"),
        ("parser_1", "input_3", "parser1_input3_output"),
        ("parser_1", "input_4", "parser1_input4_output"),
        ("parser_1", "input_5", "parser1_input5_output"),
        ("parser_1", "input_6", "parser1_input6_output"),
        ("parser_1", "input_7", "parser1_input7_output"),
        ("parser_1", "input_8", "parser1_input8_output"),
        ("parser_2", "input_6", "parser2_input6_output"),
        ("parser_2", "input_7", "parser2_input7_output"),
        ("parser_2", "input_8", "parser2_input8_output"),
    ]
)
def test_parser_valid(parser, args, output, request):
    parser = request.getfixturevalue(parser)
    arg = request.getfixturevalue(args)
    output = request.getfixturevalue(output)
    parser.parse(arg)
    assert parser.namespace == output


@pytest.mark.parametrize(
    "parser, args", [
        ("parser_2", "input_1"),
        ("parser_2", "input_2"),
        ("parser_2", "input_3"),
        ("parser_2", "input_4"),
        ("parser_2", "input_5"),
    ]
)
def test_parser_invalid(parser, args, request):
    parser = request.getfixturevalue(parser)
    arg = request.getfixturevalue(args)
    with pytest.raises(UndefinedVariableError):
        parser.parse(arg)
