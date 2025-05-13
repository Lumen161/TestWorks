import sys
import json


def fill(test, values_dict):
    if 'id' in test and test['id'] in values_dict:
        test['value'] = values_dict[test['id']]
    if 'values' in test:
        for subitem in test['values']:
            fill(subitem, values_dict)


def main():
    """
    Команда для запуска
    python3 task3.py test.json values.json report.json

    """
    test_json = sys.argv[1]
    values_json = sys.argv[2]
    report_json = sys.argv[3]

    with open(values_json, 'r', encoding='cp1251') as f:
        values_data = json.load(f)

    values_dict = {item['id']: item['value'] for item in values_data['values']}

    with open(test_json, 'r') as f:
        test_data = json.load(f)

    for test in test_data['tests']:
        fill(test, values_dict)

    with open(report_json, 'w') as f:
        json.dump(test_data, f, indent=2)


main()
