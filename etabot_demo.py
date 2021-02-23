storage = {}

def preFill():
	storage['beer'] = 'fridge'

	storage['flour'] = 'pantry'

	storage['jacket'] = 'closet'

	storage['car'] = 'garage'

assert len(storage) == 0 #dict is empty

preFill()

assert len(storage) == 4 #dict is filled

assert 'beer' in storage #check to see if key is in dict

assert 'shoes' not in storage #check to see if non-existent key not in dict

assert storage['beer'] == 'fridge' #check to see if value matches

assert storage['flour'] == 'pantry'

storage['flour'] = 'kitchen'

assert storage['flour'] == 'kitchen' #check to see if change of val happened

del storage['beer']

assert 'beer' not in storage #check to see if deletion of key successful

print("All tests passed successfully")

