with open("system.log") as file:

	error_count = 0

	for line in file:
		if "ERROR" in line:
			error_count += 1

print(f"Errors: {error_count}")

