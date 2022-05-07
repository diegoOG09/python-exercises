def trabajadores(empleados):
	list_to_delete=[]
	for empleado in empleados:
		if empleados[empleado]['desempeño']<50:
			list_to_delete.append(empleado)

	for key in list_to_delete:
		print('Se recomienda despedir al trabajador',key)
		empleados.pop(key)
	return empleados

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

buenos_trabajadores=dict()
buenos_trabajadores=trabajadores(staff)
print('Los trabajadores con mejor desempeño:')
for trabajador in buenos_trabajadores:
	print(trabajador)