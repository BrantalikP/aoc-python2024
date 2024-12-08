from typing import Tuple


def read_file(file_name):
	with open(file_name, 'r') as f:
		return f.read().split("\n")


def get_order_rules(order_rules: list[str]) -> list[list[int]]:
	return list(map(lambda x: list(map(int, x.split('|'))), order_rules))


def get_updates(updates: list[str]) -> list[list[int]]:
	return list(map(lambda x: list(map(int, x.split(','))), updates))


def separate_text(text: list[str]) -> Tuple[list[list[int]], list[list[int]]]:
	index = text.index("")
	order_rules = text[:index]
	updates = text[index + 1:len(text) - 1]
	return get_order_rules(order_rules),get_updates(updates)


def find_middle_value(update: list[int]) -> int:
	middle_index = len(update) // 2
	return update[middle_index] if len(update) % 2 == 1 else update[middle_index - 1]


def find_correct_updates(update: list[int], all_order_rules: list[list[int]]) -> int:
	rules = list(filter(lambda rule: all(num in update for num in rule), all_order_rules))
	is_ok = all(update.index(x[0]) < update.index(x[1]) for x in rules)
	if is_ok:
		return 0
	new_update = update.copy()

	is_done = False
	while not is_done:
		its_clean = True
		for x in rules:
			index1 = new_update.index(x[0])
			index2 = new_update.index(x[1])
			if index1 > index2:
				new_update[index1], new_update[index2] = new_update[index2], new_update[index1]
				its_clean = False
		is_done = its_clean
	return find_middle_value(new_update)


def main(file_name):
	text = read_file(file_name)
	order_rules, updates = separate_text(text)
	result = list(map(lambda x: find_correct_updates(x, order_rules), updates))
	return sum(result)


if __name__ == '__main__':
	result = main("data.txt")
	print("Result:", result)