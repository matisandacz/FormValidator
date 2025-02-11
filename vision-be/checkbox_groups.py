# TODO: In production, users would configure the groups for their form documents and store them in the database.
def get_groups():

	"""

	By convention, groups are stored consecutively from top left to bottom right.

	"""
	EXACTLY_ONE_ERROR = "Exactly one checkbox must be checked."
	AT_MOST_ONE_ERROR = "At most one checkbox must be checked."

	groups = []
	groups.append({
		"name": "Location",
		"size": 3,
		"exactlyOneMatch": True,
		"atMostOneMatch": False,
		"errorMessage": EXACTLY_ONE_ERROR
	})

	groups.append({
		"name": "Property Values",
		"size": 3,
		"exactlyOneMatch": True,
		"atMostOneMatch": False,
		"errorMessage": EXACTLY_ONE_ERROR
	})

	groups.append({
		"name": "Built-Up",
		"size": 3,
		"exactlyOneMatch": True,
		"atMostOneMatch": False,
		"errorMessage": EXACTLY_ONE_ERROR
	})

	groups.append({
		"name": "Demand/Supply",
		"size": 3,
		"exactlyOneMatch": True,
		"atMostOneMatch": False,
		"errorMessage": EXACTLY_ONE_ERROR
	})

	groups.append({
		"name": "Growth",
		"size": 3,
		"exactlyOneMatch": True,
		"atMostOneMatch": False,
		"errorMessage": EXACTLY_ONE_ERROR
	})

	groups.append({
		"name": "Marketing Time",
		"size": 3,
		"exactlyOneMatch": True,
		"atMostOneMatch": False,
		"errorMessage": EXACTLY_ONE_ERROR
	})

	groups.append({
		"name": "Zoning Compliance",
		"size": 4,
		"exactlyOneMatch": True,
		"atMostOneMatch": False,
		"errorMessage": EXACTLY_ONE_ERROR
	})

	groups.append({
		"name": "Highest Best Use",
		"size": 2,
		"exactlyOneMatch": True,
		"atMostOneMatch": False,
		"errorMessage": EXACTLY_ONE_ERROR
	})

	groups.append({
		"name": "Utilities Electricity",
		"size": 2,
		"exactlyOneMatch": True,
		"atMostOneMatch": False,
		"errorMessage": EXACTLY_ONE_ERROR
	})

	groups.append({
	"name": "Utilities Water",
		"size": 2,
		"exactlyOneMatch": True,
		"atMostOneMatch": False,
		"errorMessage": EXACTLY_ONE_ERROR
	})

	groups.append({
		"name": "Street Improvements",
		"size": 2,
		"exactlyOneMatch": False,
		"atMostOneMatch": True,
		"errorMessage": AT_MOST_ONE_ERROR
	})

	groups.append({
		"name": "Utilities Gas",
		"size": 2,
		"exactlyOneMatch": True,
		"atMostOneMatch": False,
		"errorMessage": EXACTLY_ONE_ERROR
	})

	groups.append({
		"name": "Utilities Sewer",
		"size": 2,
		"exactlyOneMatch": True,
		"atMostOneMatch": False,
		"errorMessage": EXACTLY_ONE_ERROR
	})

	groups.append({
		"name": "Alley Improvements",
		"size": 2,
		"exactlyOneMatch": False,
		"atMostOneMatch": True,
		"errorMessage": AT_MOST_ONE_ERROR
	})

	groups.append({
		"name": "FEMA Flood Hazard Area",
		"size": 2,
		"exactlyOneMatch": True,
		"atMostOneMatch": False,
		"errorMessage": EXACTLY_ONE_ERROR
	})

	groups.append({
		"name": "Utilities and Offsite Improvements Typical",
		"size": 2,
		"exactlyOneMatch": True,
		"atMostOneMatch": False,
		"errorMessage": EXACTLY_ONE_ERROR
	})
	
	groups.append({
		"name": "Adverse Conditions",
		"size": 2,
		"exactlyOneMatch": True,
		"atMostOneMatch": False,
		"errorMessage": EXACTLY_ONE_ERROR
	})

	return groups


# I am precomputing for efficiency so I dont have to iterate through all groups for each checkbox.
def checkbox_to_group_mapping():
	mapping = {}
	groups = get_groups()

	total_checkboxes = sum(group["size"] for group in groups)

	current_position = 0
	for group_index, group in enumerate(groups):
		next_position = current_position + group["size"]

		for checkbox_idx in range(current_position, next_position):
			mapping[checkbox_idx] = group_index

		current_position = next_position

	return mapping

def get_group_for_checkbox(checkbox_index):
	mapping = checkbox_to_group_mapping()
	return mapping[checkbox_index]

def get_total_checkboxes():
	groups = get_groups()
	return sum(group["size"] for group in groups)


