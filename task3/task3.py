import json
import sys


def make_report(values_path: str, tests_path: str, report_path: str):
    with open(values_path) as f:
        data_values = json.load(f)
    values_dict = {}
    for item in data_values["values"]:
        values_dict[item['id']] = item['value']
    with open(tests_path) as f:
        data_report_values = json.load(f)
    completed_tests = get_completed_tests(data_report_values["tests"], values_dict)
    with open(report_path, 'w') as f:
        json.dump({"tests": completed_tests}, f, indent=2)


def get_completed_tests(tests: list, values_dict: dict) -> list:
    for item in tests:
        if item.get('value') or item.get('value') == '':
            item['value'] = values_dict[item['id']]
        if item.get('values') and isinstance(item['values'], list):
            get_completed_tests(item['values'], values_dict)
    return tests


if __name__ == "__main__":
    make_report(values_path=sys.argv[1],
                tests_path=sys.argv[2],
                report_path=sys.argv[3])
