while True:
	if get_pos_x() == 0 and get_pos_y() == 0 and can_harvest():
		harvest()
		plant(Entities.Grass)
		move(North)
	elif get_pos_x() == 0 and get_pos_y() == 1 and can_harvest():
		harvest()
		plant(Entities.Grass)
		move(North)
	elif get_pos_x() == 0 and get_pos_y() == 2 and can_harvest():
		harvest()
		plant(Entities.Grass)
		move(North)
	elif get_pos_x() == 0 and get_pos_y() == 3 and can_harvest():
		harvest()
		plant(Entities.Grass)
		move(North)
		move(East)
	elif get_pos_x() == 1 and get_pos_y() == 0 and can_harvest():
		harvest()
		plant(Entities.Bush)
		move(North)
	elif get_pos_x() == 1 and get_pos_y() == 1 and can_harvest():
		harvest()
		plant(Entities.Bush)
		move(North)
	elif get_pos_x() == 1 and get_pos_y() == 2 and can_harvest():
		harvest()
		plant(Entities.Bush)
		move(North)
	elif get_pos_x() == 1 and get_pos_y() == 3 and can_harvest():
		harvest()
		plant(Entities.Bush)
		move(North)
		move(East)
	elif get_pos_x() == 2 and get_pos_y() == 0 and can_harvest():
		harvest()
		plant(Entities.Carrot)
		move(North)
	elif get_pos_x() == 2 and get_pos_y() == 1 and can_harvest():
		harvest()
		plant(Entities.Carrot)
		move(North)
	elif get_pos_x() == 2 and get_pos_y() == 2 and can_harvest():
		harvest()
		plant(Entities.Carrot)
		move(North)
	elif get_pos_x() == 2 and get_pos_y() == 3 and can_harvest():
		harvest()
		plant(Entities.Carrot)
		move(North)
		move(East)