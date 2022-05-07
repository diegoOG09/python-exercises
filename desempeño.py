staff = {
	'Juan': {
		'cargo': 'marketing',
		'desempeño': 71
	},
	'Sofia': {
		'cargo': 'marketing',
		'desempeño': 65
	},
	'Andres': {
		'cargo': 'marketing',
		'desempeño': 49
	},
	'Romina': {
		'cargo': 'marketing',
		'desempeño': 53
	}
}

def trabajadores(empleados):
	
	for empleado in empleados:
		if empleados[empleado]['desempeño'] < 50:
			print('Se recomienda despedir al trabajador',empleado)
			print(empleados.pop(empleado))
			return empleados
 
	print('Sale del for')
	
	print('Trabajadores de alto desempeño:')
	for trabajador in empleados:
		print(trabajador)

trabajadores(staff)